import React, { useEffect, useState } from "react";
import styled from "styled-components";
import { Button, Checkbox, Form, Input } from "antd";
import { useNavigate } from "react-router-dom";
import logo from "../icon.png";
import axios from "axios";

const StyledErrorMessage = styled.div``;
const StyledImage = styled.img`
  margin-left: 120px;
  padding-bottom: 30px;
  width: 150px;
`;
const StyledContainer = styled.div`
  width: 500px;
  position: absolute;
  left: 28%;
  top: 25%;
`;

const SignupCard = (): JSX.Element => {
  const [valid, setValid] = useState(true);
  const navigate = useNavigate();
  const url = "http://localhost:8000/api/user/login";

  const onFinish = async (values: any) => {
    console.log(values);
    // email: str
    // password: str
    // name: str
    // student_id: str
    const response = await axios.post(url, values);
    console.log(response);
    if (response.status === 200) {
      setValid(true);
      navigate("/panel");
    } else {
      setValid(false);
    }
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log("Failed:", errorInfo);
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
        <Form.Item
          label="Email"
          name="email"
          rules={[{ required: true, message: "Please input your email!" }]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Student ID"
          name="id"
          rules={[{ required: true, message: "Please input your student id!" }]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Name"
          name="name"
          rules={[{ required: true, message: "Please input your name!" }]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: "Please input your password!" }]}
        >
          <Input.Password />
        </Form.Item>

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
