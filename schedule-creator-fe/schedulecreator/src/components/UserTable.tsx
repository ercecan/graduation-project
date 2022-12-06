import React from 'react';
import { Space, Table, Tag } from 'antd';
import type { ColumnsType } from 'antd/es/table';

interface DataType {
  key: string;
  nickname: string;
  role: string;
  address: string;
  actions: string[];
}

const columns: ColumnsType<DataType> = [
  {
    title: 'Name',
    dataIndex: 'nickname',
    key: 'nickname',
    render: (text) => <a>{text}</a>,
  },
  {
    title: 'Role',
    dataIndex: 'role',
    key: 'role',
  },
  {
    title: 'Address',
    dataIndex: 'address',
    key: 'address',
  },
  {
    title: 'Actions',
    key: 'action',
    dataIndex: 'action',
    render: (_, { actions }) => (
      <>
        {actions.map((action) => {
          let color = action.length > 6 ? 'geekblue' : 'green';
          if (action === 'Ban') {
            color = 'volcano';
          }
          return (
            <Tag color={color} key={action}>
              {action.toUpperCase()}
            </Tag>
          );
        })}
      </>
    ),
  },
  {
    title: 'Action',
    key: 'action',
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
    nickname: 'John Brown',
    role: "Junior",
    address: 'New York No. 1 Lake Park',
    actions: ['Promote', 'Ban'],
  },
  {
    key: '2',
    nickname: 'Jim Green',
    role: "Senior",
    address: 'London No. 1 Lake Park',
    actions: ['Demote', 'Ban'],
  },
  {
    key: '3',
    nickname: 'Joe Black',
    role: "Junior",
    address: 'Sidney No. 1 Lake Park',
    actions: ['Promote', 'Ban'],
  },
];

const UserTable = ():JSX.Element => <Table columns={columns} dataSource={data} />;

export default UserTable;