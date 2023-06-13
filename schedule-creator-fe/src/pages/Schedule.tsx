import React, { useEffect, useMemo, useState } from 'react';
import styled from 'styled-components';
import ScheduleDetail from '../components/ScheduleDetail';
import FuturePlan from '../components/FuturePlan';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const StyledContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 800px;
`;

const StyledText = styled.p`
  color: #333;
  font-family: Arial, sans-serif; /* Font family */
  font-size: 18px; /* Font size */
  font-weight: bold; /* Font weight */
  text-decoration: underline; /* Text decoration */
  text-align: center; /* Text alignment */
  text-transform: uppercase; /* Text transform */
`;

function timeStringToFloat(timeString: string): number {
  const [hoursStr, minutesStr] = timeString.split(':');
  const hours = parseInt(hoursStr);
  const minutes = parseInt(minutesStr);
  return hours + minutes / 60;
}

function getDayIndex(dayName: string): number {
  switch (dayName) {
    case 'Monday':
      return 0;
    case 'Tuesday':
      return 1;
    case 'Wednesday':
      return 2;
    case 'Thursday':
      return 3;
    case 'Friday':
      return 4;
    default:
      return -1;
  }
}

const Schedule = (): JSX.Element => {
  const [valid, setValid] = useState(true);
  const [schedule, setSchedule] = useState<{
    courses: any[];
  } | null>(null);
  const [loading, setLoading] = useState(false);

  const jsonString = sessionStorage.getItem('schedules');
  const schedules = jsonString ? JSON.parse(jsonString) : '';
  const { id } = useParams<{ id: string }>();

  useEffect(() => {
    axios
      .get(`http://34.107.96.1:8000/api/schedule?schedule_id=${id}`)
      .then((res) => {
        setSchedule(res.data);
      });
  }, [loading]);

  const data: {
    name: string;
    events: {
      startTime: number;
      endTime: number;
      title: string;
      description: string;
    }[];
  }[] = [
    {
      name: 'Monday',
      events: [],
    },
    {
      name: 'Tuesday',
      events: [],
    },
    {
      name: 'Wednesday',
      events: [],
    },
    {
      name: 'Thursday',
      events: [],
    },
    {
      name: 'Friday',
      events: [],
    },
  ];

  useEffect(() => {
    if (loading) {
      const intervalId = setInterval(() => {
        axios
          .get(
            `http://34.107.96.1:8000/api/status?type=recommendation&id=${sessionStorage.getItem(
              'student_db_id',
            )}&name=${sessionStorage.getItem('sch_name')}`,
          )
          .then((res) => {
            console.log(res.data);
            if (
              res.data === 'completed' ||
              res.data === null ||
              res.data === ''
            ) {
              clearInterval(intervalId);
              setLoading(false);
            }
          })
          .catch((error) => {
            console.log(error);
          });
      }, 3000);
    }
  });

  const openedCourses: any[] = [];

  if (schedule && schedule.courses) {
    schedule.courses.map((course: any) => {
      openedCourses.push(course);
      course.time_slot.map((slot: any) => {
        const day = slot.day;
        const elem = {
          startTime: timeStringToFloat(slot.start_time),
          endTime: timeStringToFloat(slot.end_time),
          title: course.course.name,
          description:
            course.course.description.length > 150
              ? course.course.description.substring(0, 150) + '...'
              : course.course.description,
        };
        data[getDayIndex(day)].events.push(elem);
      });
    });
  }

  return (
    <StyledContainer>
      <ScheduleDetail data={data} />
      <div
        style={{
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'space-around',
        }}
      >
        <StyledText style={{ marginLeft: 120 }}>Preferences</StyledText>
        <StyledText style={{ marginLeft: 260 }}>Fail Scenarios</StyledText>
        <StyledText style={{ marginLeft: 100 }}>Future Plan</StyledText>
      </div>
      {schedule && (
        <FuturePlan
          openedCourses={openedCourses}
          schedule={schedule}
          loading={loading}
          setLoading={setLoading}
        />
      )}
    </StyledContainer>
  );
};

export default Schedule;
