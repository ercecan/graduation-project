import React, { useState } from "react";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
import { Button, Form, Input, Select, Space } from "antd";
import styled from "styled-components";
import SelectionComponent from "./SelectionComponent";

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

const onFinish = (values: any) => {
  console.log("Received values of form:", values);
};

const App: React.FC = () => {
  const [currentFilled, setCurrentFilled] = useState(false);

  return (
    <StyledForm
      name="dynamic_form_nest_item"
      onFinish={onFinish}
      style={{ maxWidth: 620, minWidth: 600, flexDirection: "column" }}
      autoComplete="off"
    >
      <Form.List name="users">
        {(fields, { add, remove }) => {
          if (fields.length === 0) {
            setCurrentFilled(true);
          }
          return (
            <>
              {fields.map(({ key, name, ...restField }) => (
                <SelectionComponent
                  key={key}
                  name={name}
                  restField={restField}
                  remove={remove}
                  setCurrentFilled={setCurrentFilled}
                />
              ))}
              <Form.Item>
                <Button
                  type="dashed"
                  onClick={() => {
                    add();
                    setCurrentFilled(false);
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

export default App;
