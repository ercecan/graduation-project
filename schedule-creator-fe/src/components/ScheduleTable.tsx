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

const preferenceColors: { [key: string]: string } = {
  'Time Preference': 'green',
  'Day Preference': 'geekblue',
  // Add more preferences and their corresponding colors as needed
};

function wait(delay: number) {
  return new Promise((resolve) => setTimeout(resolve, delay));
}

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
  const [showSuccessNotification, setShowSuccessNotification] = useState(false);

  const navigate = useNavigate();

  const handlePreviewClick = (id: string) => {
    navigate(`/schedule/${id}`);
  };

  const handleDeleteClick = (id: string) => {
    axios
      .delete('http://0.0.0.0:8000/api/schedule/delete/' + id)
      .then(async (res) => {
        if (res.status === 200) {
          setShowSuccessNotification(true);
          await wait(4000);
          setShowSuccessNotification(false);
        }
      });
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
          {preferences.map((preference: string, index: number) => {
            const color = preferenceColors[preference] || 'green';
            return (
              <Tag color={color} key={preference + index}>
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
          <a
            onClick={() => {
              handleDeleteClick(record.id);
            }}
          >
            Delete
          </a>
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
        sessionStorage.setItem('schedules', JSON.stringify(response.data));
        setScheduleData(
          response.data.map((data: any, index: any) => {
            return {
              id: data.id,
              key: index,
              name: data.name,
              date: new Date(data.time),
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
  }, [showSuccessNotification]);

  const handleTimeOut = () => {
    setShowSuccessNotification(false);
  };

  return (
    <Container>
      <CreateScheduleComponent />
      {showSuccessNotification && (
        <div
          style={{
            backgroundColor: 'blue',
            color: 'white',
            padding: '10px',
            borderRadius: '5px',
            textAlign: 'center',
            width: '150px',
            marginLeft: 'auto',
            marginRight: 'auto',
          }}
        >
          Schedule Deleted
        </div>
      )}{' '}
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
