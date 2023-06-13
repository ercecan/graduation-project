import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import { Button, Col, Form, Input, Row, Select } from 'antd';
import { useNavigate } from 'react-router-dom';
import logo from '../icon.png';
import axios from 'axios';

const StyledErrorMessage = styled.div``;
const StyledImage = styled.img`
  margin-left: 50px;
  padding-bottom: 30px;
  width: 150px;
`;
const StyledContainer = styled.div`
  width: 1000px;
  position: absolute;
  left: 10%;
  overflow-y: auto;

  .ant-row {
    gap: 16px;
  }
`;

const SignupCard = (): JSX.Element => {
  const [valid, setValid] = useState(true);
  const [counter, setCounter] = useState(0);
  const navigate = useNavigate();
  const url = 'http://34.107.96.1:8000/api/student/register';

  const onFinish = async (values: any) => {
    console.log(values);
    const response = await axios.post(url, values);
    console.log(response);
    if (response.status === 200) {
      setValid(true);
      navigate('/home');
    } else {
      setValid(false);
    }
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <StyledContainer>
      <StyledImage src={logo} alt="Logo" />
      <StyledErrorMessage>
        {!valid && <p>Please try again</p>}
      </StyledErrorMessage>
      <Form
        name="basic"
        labelCol={{ span: 8 }}
        wrapperCol={{ span: 16 }}
        initialValues={{ remember: true }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        <Row>
          <Col span={10}>
            <Form.Item
              label="Name"
              name="name"
              rules={[{ required: true, message: 'Please input your name!' }]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="Surname"
              name="surname"
              rules={[{ required: true, message: 'Please input your name!' }]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="Student ID"
              name="student_id"
              rules={[
                { required: true, message: 'Please input your student id!' },
              ]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="Email"
              name="email"
              rules={[{ required: true, message: 'Please input your email!' }]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="Password"
              name="password"
              rules={[
                { required: true, message: 'Please input your password!' },
              ]}
            >
              <Input.Password />
            </Form.Item>

            <Form.Item
              label="School"
              name="school"
              rules={[
                { required: true, message: 'Please input your password!' },
              ]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="Year"
              name="year"
              rules={[
                { required: true, message: 'Please input your password!' },
              ]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="GPA"
              name="gpa"
              rules={[
                { required: true, message: 'Please input your password!' },
              ]}
            >
              <Input />
            </Form.Item>
          </Col>
          <Col span={10}>
            <Form.List name="major">
              {(fields, { add, remove }) => (
                <>
                  {fields.map((field, index) => (
                    <div key={field.key}>
                      <Form.Item
                        {...field}
                        name={[field.name, 'name']}
                        rules={[
                          { required: true, message: 'Please enter a name' },
                        ]}
                      >
                        <Input placeholder="Name" />
                      </Form.Item>
                      <Form.Item
                        {...field}
                        name={[field.name, 'code']}
                        rules={[
                          { required: true, message: 'Please enter a code' },
                        ]}
                      >
                        <Input placeholder="Code" />
                      </Form.Item>
                      <Form.Item
                        {...field}
                        name={[field.name, 'language']}
                        rules={[
                          {
                            required: true,
                            message: 'Please enter a language',
                          },
                        ]}
                      >
                        <Input placeholder="Language" />
                      </Form.Item>
                      <Button
                        style={{ marginRight: '10px' }}
                        type="dashed"
                        onClick={() => {
                          remove(field.name);
                          setCounter(counter - 1);
                        }}
                      >
                        Remove
                      </Button>
                    </div>
                  ))}
                  {counter < 2 && (
                    <Button
                      type="dashed"
                      onClick={() => {
                        add();
                        setCounter(counter + 1);
                      }}
                    >
                      Add major
                    </Button>
                  )}
                </>
              )}
            </Form.List>
          </Col>
        </Row>
        <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
    </StyledContainer>
  );
};

export default SignupCard;
