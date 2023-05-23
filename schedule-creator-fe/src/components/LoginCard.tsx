import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import { Button, Checkbox, Form, Input } from 'antd';
import { useNavigate } from 'react-router-dom';
import logo from '../icon.png';
import axios from 'axios';

const StyledErrorMessage = styled.div``;
const StyledImage = styled.img`
  display: flex;
  margin-left: 120px;
  padding-bottom: 30px;
  width: 150px;
`;

const StyledForm = styled(Form)`
  display: flex;
  flex-direction: column;
  width: 400px;
`;

const StyledContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const LoginCard = (): JSX.Element => {
  const [valid, setValid] = useState(true);
  const navigate = useNavigate();
  const url = 'http://localhost:8000/api/student/login';

  const onFinish = async (values: any) => {
    const response = await axios.post(url, values);
    sessionStorage.setItem('email', response.data.email);
    sessionStorage.setItem('student_db_id', response.data.user_id);
    sessionStorage.setItem('student_id', response.data.user_student_id);
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
      <StyledForm
        name="basic"
        labelCol={{ span: 8 }}
        wrapperCol={{ span: 16 }}
        initialValues={{ remember: true }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
      >
        <Form.Item
          label="Email"
          name="email"
          rules={[{ required: true, message: 'Please input your username!' }]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: 'Please input your password!' }]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </StyledForm>
    </StyledContainer>
  );
};

export default LoginCard;
