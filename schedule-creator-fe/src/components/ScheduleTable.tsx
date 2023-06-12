import React, { useEffect, useMemo, useState } from 'react';
import { Modal, Space, Table, Tag } from 'antd';
import type { ColumnsType } from 'antd/es/table';
import CreateScheduleComponent from './CreateScheduleComponent';
import styled from 'styled-components';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import LoadingSpinner from './common/LoadingSpinner';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 80vh;
  .ant-spin-nested-loading {
    width: 100%;
  }
`;

// const data: DataType[] = [
//   {
//     date: new Date('Mon May 29 2023 16:26:49 GMT+0300 (GMT+03:00)'),
//     id: '6474a8193ec517cb55eb21c5',
//     key: '0',
//     name: 'Robotics and Dance',
//     preferences: ['Time Preference', 'Day Preference'],
//   },
//   {
//     date: new Date('Mon May 23 2023 16:22:44 GMT+0300 (GMT+03:00)'),
//     id: '6474a8193ec517cb55eb21c5',
//     key: '1',
//     name: 'Extreme Cryptography',
//     preferences: ['Day Preference', 'Campus Preference'],
//   },
//   {
//     date: new Date('Mon May 27 2023 23:22:49 GMT+0300 (GMT+03:00)'),
//     id: '6474a8193ec517cb55eb21c5',
//     key: '2',
//     name: 'Advanced Theoretical Physics',
//     preferences: ['Campus Preference', 'Language Preference'],
//   },
//   {
//     date: new Date('Mon May 21 2023 18:31:41 GMT+0300 (GMT+03:00)'),
//     id: '6474a8193ec517cb55eb21c5',
//     key: '2',
//     name: 'Quantum Mechanics at Dawn',
//     preferences: ['Time Preference', 'Language Preference'],
//   },
// ];

const preferenceColors: { [key: string]: string } = {
  'Time Preference': 'purple',
  'Day Preference': 'teal',
  'Campus Preference': 'magenta',
  'Language Preference': 'gold',
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
  const [loading, setLoading] = useState(false);
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
                (pref: any, idx: number) =>
                  (idx === 1
                    ? pref.type.charAt(0).toUpperCase() + pref.type.slice(1)
                    : 'TIME') + ' Preference',
              ),
            } as DataType;
          }),
        );
      })
      .then(() => setLoading(false));
  }, [showSuccessNotification]);

  useEffect(() => {
    if (loading) {
      const intervalId = setInterval(() => {
        // console.log('finish', finish);
        // if (finish) return;
        axios
          .get(
            `http://0.0.0.0:8000/api/status?type=schedule&id=${sessionStorage.getItem(
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
  }, [loading]);

  return (
    <div>
      {!loading ? (
        <Container>
          <CreateScheduleComponent setLoading={setLoading} />
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
          )}
          <Table
            columns={columns}
            pagination={{ pageSize: 5 }}
            dataSource={scheduleData}
            loading={loading}
            style={{ display: 'flex', width: '100%' }}
          />
        </Container>
      ) : (
        <LoadingSpinner
          style={{ width: 200 }}
          text={'Your Schedule is Creating...'}
        />
      )}
    </div>
  );
};

export default ScheduleTable;
