import React from 'react';
import { Space, Table, Tag } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import CreateScheduleComponent from './CreateScheduleComponent';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 80vh;
  .ant-spin-nested-loading{
    width: 100%;
  }
`;

interface DataType {
  key: string;
  name: string;
  date: Date;
  preferences: string[];
}

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
    render: (_, record) => (
      <Space size="middle">
        <a>Preview {record.name}</a>
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

const data: DataType[] = [
  {
    key: '1',
    name: 'Ömer Schedule',
    date: new Date('2023-04-12T09:30:00'),
    preferences: ['Day Preference', 'Time Preference'],
  },
  {
    key: '2',
    name: 'Barış Schedule',
    date: new Date('2023-03-12T07:30:00'),
    preferences: ['Day Preference'],
  },
  {
    key: '3',
    name: 'Erce Schedule',
    date: new Date('2022-12-05T15:30:00'),
    preferences: ['Time Preference'],
  },
];

const ScheduleTable = () => {
  // TODO
  return (
  <Container>
    <CreateScheduleComponent />
    <Table columns={columns} dataSource={data} style={{display: "flex", width: "100%"}}/>
  </Container>
  )
}

export default ScheduleTable;