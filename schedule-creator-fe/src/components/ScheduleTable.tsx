import React, { useEffect, useState } from 'react';
import { Modal, Space, Table, Tag } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import CreateScheduleComponent from './CreateScheduleComponent';
import styled from 'styled-components';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 80vh;
  .ant-spin-nested-loading {
    width: 100%;
  }
`;

const schedules = [
  {
    id: '644fe06deb6497fd5807c7f2',
    name: 'Schedule 0',
    courses: [
      {
        id: '644fbd35ed40cb871392f17b',
        course: {
          _id: '644fb5dccddb3dc51acfa068',
          name: 'Database Systems',
          code: 'BLG232E',
          crn: '23150',
          ects: 8,
          credits: 4,
          language: 'English',
          major_restrictions: ['BLG', 'BLGE'],
          prereqs: null,
          year_restrictions: [2, 3],
          description: 'db mock description',
          semester: 'fall',
          recommended_semester: 5,
          instructor: 'Ali Çakmak',
          is_elective: false,
          tag: null,
        },
        time_slot: [
          {
            day: 'Monday',
            start_time: '08:30',
            end_time: '11:30',
          },
          {
            day: 'Wednesday',
            start_time: '12:30',
            end_time: '14:30',
          },
        ],
        capacity: 70,
        classroom: null,
        teaching_method: 'online',
      },
    ],
    term: {
      semester: 'fall',
      year: 2023,
    },
    score: 5,
    future_plan: [
      {
        course_names: ['Son dönemden ders - I', 'Son dönemden ders - II'],
        term: { semester: 'fall', year: 2023 },
      },
      {
        course_names: ['Son dönemden ders - III', 'Son dönemden ders - IV'],
        term: { semester: 'spring', year: 2024 },
      },
    ],
    preferences: [
      {
        type: 'day',
        value: 'TUESDAY',
        priority: 5,
      },
      {
        type: 'day',
        value: 'FRIDAY',
        priority: 1,
      },
      {
        type: 'sample',
        value: 'sample',
        priority: 3,
      },
    ],
    student_id: '644fd664138dd370b4eec6ac',
  },
  {
    id: '644fe1c0c36690706b9a21b1',
    name: 'Schedule 0',
    courses: [
      {
        id: '644fbd35ed40cb871392f17b',
        course: {
          _id: '644fb5dccddb3dc51acfa068',
          name: 'Database Systems',
          code: 'BLG232E',
          crn: '23150',
          ects: 8,
          credits: 4,
          language: 'English',
          major_restrictions: ['BLG', 'BLGE'],
          prereqs: null,
          year_restrictions: [2, 3],
          description: 'db mock description',
          semester: 'fall',
          recommended_semester: 5,
          instructor: 'Ali Çakmak',
          is_elective: false,
          tag: null,
        },
        time_slot: [
          {
            day: 'Monday',
            start_time: '08:30',
            end_time: '11:30',
          },
          {
            day: 'Wednesday',
            start_time: '12:30',
            end_time: '14:30',
          },
        ],
        capacity: 70,
        classroom: null,
        teaching_method: 'online',
      },
    ],
    term: {
      semester: 'fall',
      year: 2023,
    },
    score: 5,
    future_plan: null,
    preferences: [
      {
        type: 'day',
        value: 'TUESDAY',
        priority: 5,
      },
    ],
    student_id: '644fd664138dd370b4eec6ac',
  },
  {
    id: '644fe1cac36690706b9a21b2',
    name: 'Schedule 0',
    courses: [
      {
        id: '644fbd35ed40cb871392f17b',
        course: {
          _id: '644fb5dccddb3dc51acfa068',
          name: 'Database Systems',
          code: 'BLG232E',
          crn: '23150',
          ects: 8,
          credits: 4,
          language: 'English',
          major_restrictions: ['BLG', 'BLGE'],
          prereqs: null,
          year_restrictions: [2, 3],
          description: 'db mock description',
          semester: 'fall',
          recommended_semester: 5,
          instructor: 'Ali Çakmak',
          is_elective: false,
          tag: null,
        },
        time_slot: [
          {
            day: 'Monday',
            start_time: '08:30',
            end_time: '11:30',
          },
          {
            day: 'Wednesday',
            start_time: '12:30',
            end_time: '14:30',
          },
        ],
        capacity: 70,
        classroom: null,
        teaching_method: 'online',
      },
    ],
    term: {
      semester: 'fall',
      year: 2023,
    },
    score: 5,
    future_plan: null,
    preferences: [
      {
        type: 'day',
        value: 'TUESDAY',
        priority: 5,
      },
    ],
    student_id: '644fd664138dd370b4eec6ac',
  },
  {
    id: '644fe1d2c36690706b9a21b3',
    name: 'Schedule 0',
    courses: [
      {
        id: '644fbd35ed40cb871392f17b',
        course: {
          _id: '644fb5dccddb3dc51acfa068',
          name: 'Database Systems',
          code: 'BLG232E',
          crn: '23150',
          ects: 8,
          credits: 4,
          language: 'English',
          major_restrictions: ['BLG', 'BLGE'],
          prereqs: null,
          year_restrictions: [2, 3],
          description: 'db mock description',
          semester: 'fall',
          recommended_semester: 5,
          instructor: 'Ali Çakmak',
          is_elective: false,
          tag: null,
        },
        time_slot: [
          {
            day: 'Monday',
            start_time: '08:30',
            end_time: '11:30',
          },
          {
            day: 'Wednesday',
            start_time: '12:30',
            end_time: '14:30',
          },
        ],
        capacity: 70,
        classroom: null,
        teaching_method: 'online',
      },
    ],
    term: {
      semester: 'fall',
      year: 2023,
    },
    score: 5,
    future_plan: null,
    preferences: [
      {
        type: 'day',
        value: 'TUESDAY',
        priority: 5,
      },
    ],
    student_id: '644fd664138dd370b4eec6ac',
  },
];

interface DataType {
  id: string;
  key: string;
  name: string;
  date: Date;
  preferences: string[];
}

const ScheduleTable = () => {
  const [scheduleData, setScheduleData] = useState<DataType[]>();
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  const handlePreviewClick = (id: string) => {
    navigate(`/schedule/${id}`);
  };

  const columns: ColumnsType<DataType> = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      render: (text) => <a>{text}</a>,
    },
    {
      title: 'Date',
      dataIndex: 'date',
      key: 'date',
      render: (date) => <span>{date.toLocaleString()}</span>,
    },
    {
      title: 'Preferences',
      key: 'preferences',
      dataIndex: 'preferences',
      render: (_, { preferences }) => (
        <>
          {preferences.map((preference) => {
            let color = preference.length > 5 ? 'geekblue' : 'green';
            if (preference === 'Time Preference') {
              color = 'green';
            }
            return (
              <Tag color={color} key={preference}>
                {preference.toUpperCase()}
              </Tag>
            );
          })}
        </>
      ),
    },
    {
      title: 'Preview',
      key: 'preview',
      render: (data, record) => (
        <Space size="middle">
          <a onClick={() => handlePreviewClick(record.id)}>
            Preview {record.name}
          </a>
        </Space>
      ),
    },
    {
      title: 'Delete',
      key: 'delete',
      render: (_, record) => (
        <Space size="middle">
          <a>Delete</a>
        </Space>
      ),
    },
  ];

  const student_id = sessionStorage.getItem('student_db_id');
  useEffect(() => {
    axios
      .post('http://0.0.0.0:8000/api/schedule/all', {
        student_id: student_id,
        term: { semester: 'fall', year: 2023 },
      })
      .then((response) => {
        sessionStorage.setItem(
          'schedules',
          JSON.stringify(
            // response.data
            schedules,
          ),
        );
        setScheduleData(
          // response.data.
          schedules.map((data: any, index: any) => {
            return {
              id: data.id,
              key: index,
              name: data.name,
              date: new Date(),
              preferences: data.preferences.map(
                (pref: any) =>
                  pref.type.charAt(0).toUpperCase() +
                  pref.type.slice(1) +
                  ' Preference',
              ),
            } as DataType;
          }),
        );
      })
      .then(() => setLoading(false));
  }, []);

  return (
    <Container>
      <CreateScheduleComponent />
      <Table
        columns={columns}
        pagination={{ pageSize: 5 }}
        dataSource={scheduleData}
        loading={loading}
        style={{ display: 'flex', width: '100%' }}
      />
    </Container>
  );
};

export default ScheduleTable;
