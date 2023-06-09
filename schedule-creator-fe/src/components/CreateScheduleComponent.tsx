import React, { useState } from 'react';
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons';
import { Button, Form, Input, Modal, Select, Space } from 'antd';
import styled from 'styled-components';
import SelectionComponent from './SelectionComponent';
import axios from 'axios';

const StyledForm = styled(Form)`
  display: flex;
  overflow-y: auto;
  max-height: 350px;
  margin-left: auto;
  margin-right: auto;
  .ant-form-item {
    width: 100%;
  }
`;

const CreateScheduleComponent = (): JSX.Element => {
  const [currentFilled, setCurrentFilled] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [scheduleName, setScheduleName] = useState('');
  const [preferences, setPreferences] = useState();

  const handleFormSubmit = (values: any) => {
    setPreferences(values.preferences);
    if (scheduleName === '') {
      setModalVisible(true);
    } else {
      submitForm();
    }
  };

  const submitForm = () => {
    axios
      .post('http://0.0.0.0:8000/api/schedule/', {
        message: 'create schedule',
        semester: 'spring',
        year: 2023,
        school_name: 'Istanbul Technical University',
        major: 'Computer Engineering',
        preferences: preferences,
        _id: sessionStorage.getItem('student_db_id'),
        schedule_name: scheduleName,
      })
      .then((res) => {
        // Handle response and any success logic
      })
      .catch((error) => {
        // Handle error
      });
  };

  const handleModalOk = () => {
    setModalVisible(false);
    submitForm();
  };

  const handleModalCancel = () => {
    setModalVisible(false);
  };

  const handleFieldRemoved = (b: boolean) => {
    setCurrentFilled(b);
  };

  return (
    <StyledForm
      name="dynamic_form_nest_item"
      onFinish={handleFormSubmit}
      style={{ maxWidth: 620, minWidth: 600, flexDirection: 'column' }}
      autoComplete="off"
    >
      <Modal
        title="Enter Schedule Name"
        visible={modalVisible}
        onOk={handleModalOk}
        onCancel={handleModalCancel}
      >
        <Input
          value={scheduleName}
          onChange={(e) => setScheduleName(e.target.value)}
          placeholder="Enter schedule name"
        />
      </Modal>
      <Form.List name="preferences">
        {(fields, { add, remove }) => {
          if (fields.length === 0) {
            handleFieldRemoved(true);
          }
          return (
            <>
              {fields.map(({ key, name, ...restField }) => (
                <SelectionComponent
                  key={key}
                  name={name}
                  restField={restField}
                  remove={remove}
                  onFieldRemoved={handleFieldRemoved}
                />
              ))}
              <Form.Item>
                <Button
                  type="dashed"
                  onClick={() => {
                    add();
                    handleFieldRemoved(false);
                  }}
                  block
                  disabled={!currentFilled}
                  icon={<PlusOutlined />}
                >
                  Add field
                </Button>
              </Form.Item>
            </>
          );
        }}
      </Form.List>
      <Form.Item>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </StyledForm>
  );
};

export default CreateScheduleComponent;
