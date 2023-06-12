import React, { SetStateAction, useEffect, useState } from 'react';
import { Form, Input, Button, Upload, message, Row, Col } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import UploadTranscript from './UploadTranscript';
import axios from 'axios';

const { TextArea } = Input;

const ProfilePage = () => {
  const [form] = Form.useForm();
  const [remainingCourses, setRemainingCourses] = useState('');
  const [takenCourses, setTakenCourses] = useState('');
  const [transcriptData, setTranscriptData] = useState(null);

  const handleRemainingCoursesChange = (event: {
    target: { value: SetStateAction<string> };
  }) => {
    setRemainingCourses(event.target.value);
  };

  const handleTakenCoursesChange = (event: {
    target: { value: SetStateAction<string> };
  }) => {
    setTakenCourses(event.target.value);
  };

  const handleSubmit = (values: any) => {
    console.log(transcriptData);
    axios
      .post('http://0.0.0.0:8000/api/student/update', {
        student_db_id: sessionStorage.getItem('student_db_id'),
        email: sessionStorage.getItem('email'),
        name: values.name,
        surname: values.surname,
        student_id: values.studentId,
        year: values.year,
      })
      .then((res) => {
        //
      });
  };

  return (
    <Form
      form={form}
      onFinish={handleSubmit}
      layout="vertical"
      initialValues={{
        name: '',
        surname: '',
        studentId: '',
        year: '',
      }}
    >
      <Row gutter={24}>
        <Col span={6}>
          <Form.Item
            label="Name"
            name="name"
            rules={[{ required: true, message: 'Please enter your name' }]}
          >
            <Input />
          </Form.Item>
        </Col>
        <Col span={6}>
          <Form.Item
            label="Surname"
            name="surname"
            rules={[{ required: true, message: 'Please enter your surname' }]}
          >
            <Input />
          </Form.Item>
        </Col>
        <Col span={6}>
          <Form.Item
            label="Student ID"
            name="studentId"
            rules={[
              { required: true, message: 'Please enter your student ID' },
            ]}
          >
            <Input />
          </Form.Item>
        </Col>
        <Col span={6}>
          <Form.Item
            label="Year"
            name="year"
            rules={[{ required: true, message: 'Please enter your year' }]}
          >
            <Input />
          </Form.Item>
        </Col>
      </Row>

      <Row gutter={24}>
        <Col span={12}>
          <Form.Item label="Taken Courses">
            <TextArea
              value={takenCourses}
              onChange={handleTakenCoursesChange}
            />
          </Form.Item>
        </Col>
        <Col span={12}>
          <Form.Item label="Remaining Courses (Add-Drop)">
            <TextArea
              value={remainingCourses}
              onChange={handleRemainingCoursesChange}
            />
          </Form.Item>
        </Col>
      </Row>
      <Row gutter={24}>
        <Col span={12}>
          <Form.Item label="Transcript">
            <UploadTranscript />
          </Form.Item>
        </Col>
      </Row>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Save
        </Button>
      </Form.Item>
    </Form>
  );
};

export default ProfilePage;
