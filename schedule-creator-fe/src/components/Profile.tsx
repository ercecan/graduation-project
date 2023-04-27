import React, { SetStateAction, useState } from "react";
import { Form, Input, Button, Upload, message, Row, Col } from "antd";
import { UploadOutlined } from "@ant-design/icons";

const { TextArea } = Input;

const ProfilePage = () => {
  const [form] = Form.useForm();
  const [remainingCourses, setRemainingCourses] = useState("");
  const [takenCourses, setTakenCourses] = useState("");
  const [transcriptFile, setTranscriptFile] = useState(null);

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

  const handleTranscriptUpload = (file: SetStateAction<null>) => {
    setTranscriptFile(file);
  };

  const handleTranscriptRemove = () => {
    setTranscriptFile(null);
  };

  const handleSubmit = (values: any) => {
    console.log(values);
  };

  return (
    <Form
      form={form}
      onFinish={handleSubmit}
      layout="vertical"
      initialValues={{
        name: "",
        surname: "",
        studentId: "",
        year: "",
      }}
    >
      <Row gutter={24}>
        <Col span={6}>
          <Form.Item
            label="Name"
            name="name"
            rules={[{ required: true, message: "Please enter your name" }]}
          >
            <Input />
          </Form.Item>
        </Col>
        <Col span={6}>
          <Form.Item
            label="Surname"
            name="surname"
            rules={[{ required: true, message: "Please enter your surname" }]}
          >
            <Input />
          </Form.Item>
        </Col>
        <Col span={6}>
          <Form.Item
            label="Student ID"
            name="studentId"
            rules={[
              { required: true, message: "Please enter your student ID" },
            ]}
          >
            <Input />
          </Form.Item>
        </Col>
        <Col span={6}>
          <Form.Item
            label="Year"
            name="year"
            rules={[{ required: true, message: "Please enter your year" }]}
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
            <Upload
              fileList={transcriptFile ? [transcriptFile] : []}
              beforeUpload={(file) => {
                if (file.type !== "application/pdf") {
                  message.error("Only PDF files are allowed");
                  return false;
                }
                return true;
              }}
              onRemove={handleTranscriptRemove}
              onChange={(info) => {
                if (info.fileList.length > 1) {
                  message.error("You can only upload one file");
                  return;
                }

                const { status, response } = info.file;
                if (status === "done") {
                  //   setTranscriptFile("");
                } else if (status === "error") {
                  message.error("Failed to upload transcript file");
                }
              }}
            >
              <Button icon={<UploadOutlined />}>Upload</Button>
            </Upload>
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
