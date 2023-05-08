import React, { useState } from 'react';
import styled from 'styled-components';
import { ScheduleView, createTheme } from 'react-schedule-view';
import { useParams } from 'react-router-dom';

const StyledScheduleView = styled(ScheduleView)`
  width: 500px;
  heigth: 400px;
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
  const jsonString = sessionStorage.getItem('schedules');
  const schedules = jsonString ? JSON.parse(jsonString) : '';
  const { id } = useParams<{ id: string }>();
  const schedule = schedules.find(
    (schedule: { id: string | undefined }) => schedule.id === id,
  );

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

  schedule.courses.map((course: any) => {
    course.time_slot.map((slot: any) => {
      const day = slot.day;
      const elem = {
        startTime: timeStringToFloat(slot.start_time),
        endTime: timeStringToFloat(slot.end_time),
        title: course.course.name,
        description: course.course.description,
      };
      data[getDayIndex(day)].events.push(elem);
    });
  });

  const theme = createTheme('apple', {
    hourHeight: '53px',
    style: {
      dayLabels: {
        fontWeight: 'bold',
      },
    },
  });

  return (
    <StyledScheduleView
      daySchedules={data}
      viewStartTime={8}
      viewEndTime={17}
      theme={theme}
    />
  );
};

export default Schedule;
