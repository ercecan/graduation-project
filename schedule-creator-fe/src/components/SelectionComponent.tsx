import React, { useEffect, useState } from "react";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
import { Form, FormItemProps, Select, Space } from "antd";

const SelectionComponent = (props: {
  key: React.Key | null | undefined;
  name: string | number;
  restField: JSX.IntrinsicAttributes & FormItemProps<any>;
  remove: Function;
  setCurrentFilled: Function;
}) => {
  const [isFirstFilled, setIsFirstFilled] = useState(false);
  const [isSecondFilled, setIsSecondFilled] = useState(false);
  const [isThirdFilled, setIsThirdFilled] = useState(false);

  useEffect(() => {
    if (isThirdFilled) {
      props.setCurrentFilled(true);
    }
  }, [isThirdFilled]);

  return (
    <Space
      key={props.key}
      style={{ display: "flex", marginBottom: 8 }}
      align="baseline"
    >
      <Form.Item
        {...props.restField}
        name={[props.name, "first"]}
        rules={[{ required: true, message: "Missing first name" }]}
      >
        <Select
          placeholder="Select Preference"
          style={{ width: 190 }}
          onChange={() => {
            setIsFirstFilled(true);
          }}
        >
          <Select.Option value="Day Preference">Day Preference</Select.Option>
          <Select.Option value="XXX Preference">XXX Preference</Select.Option>
          <Select.Option value="YYY Preference">YYY Preference</Select.Option>
        </Select>
      </Form.Item>
      {isFirstFilled && (
        <Form.Item
          {...props.restField}
          name={[props.name, "second"]}
          rules={[{ required: true, message: "Missing first name" }]}
        >
          <Select
            placeholder="Select Day"
            style={{ width: 190 }}
            onChange={() => {
              setIsSecondFilled(true);
            }}
          >
            <Select.Option value="Monday">Monday</Select.Option>
            <Select.Option value="Tuesday">Tuesday</Select.Option>
            <Select.Option value="Wednesday">Wednesday</Select.Option>
            <Select.Option value="Thursday">Thursday</Select.Option>
            <Select.Option value="Friday">Friday</Select.Option>
          </Select>
        </Form.Item>
      )}
      {isSecondFilled && (
        <Form.Item
          {...props.restField}
          name={[props.name, "third"]}
          rules={[{ required: true, message: "Missing first name" }]}
        >
          <Select
            placeholder="Select Priority"
            style={{ width: 190 }}
            onChange={() => {
              setIsThirdFilled(true);
            }}
          >
            <Select.Option value="1">1</Select.Option>
            <Select.Option value="2">2</Select.Option>
            <Select.Option value="3">3</Select.Option>
            <Select.Option value="4">4</Select.Option>
            <Select.Option value="5">5</Select.Option>
          </Select>
        </Form.Item>
      )}
      <MinusCircleOutlined onClick={() => props.remove(name)} />
    </Space>
  );
};

export default SelectionComponent;
