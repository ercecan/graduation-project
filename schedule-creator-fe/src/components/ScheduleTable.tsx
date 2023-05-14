import React, { useEffect, useState } from 'react';
import { Space, Table, Tag } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import CreateScheduleComponent from './CreateScheduleComponent';
import styled from 'styled-components';
import axios from 'axios';

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

const ScheduleTable = () => {
  const [scheduleData, setScheduleData] = useState<DataType[]>();
  const [loading, setLoading] = useState(true);
  const student_id = sessionStorage.getItem("student_db_id");
  useEffect(() => {
    axios.post("http://0.0.0.0:8000/api/schedule/all", {
    student_id: student_id, "term" : {"semester": "fall", "year": 2023}}).then((response) => {
      sessionStorage.setItem("schedules", JSON.stringify(response.data));
      setScheduleData(response.data.map((data:any, index: any) => {
        return ({
          key: index,
          name: data.name,
          date: new Date(),
          preferences: data.preferences.map((pref:any) => pref.type.charAt(0).toUpperCase() + pref.type.slice(1) + " Preference")
        } as DataType)
      }))
    }).then(() => setLoading(false));
  }, []);

  return (
  <Container>
    <CreateScheduleComponent />
    <Table columns={columns} pagination={{pageSize: 5}}  dataSource={scheduleData} loading={loading}  style={{display: "flex", width: "100%"}}/>
  </Container>
  )
}

export default ScheduleTable;