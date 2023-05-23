import React, { useEffect, useState } from 'react';
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons';
import { Form, FormItemProps, Select, Space } from 'antd';

export const preferences = {
  'Day Preferences': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
  'Time Preferences': [
    '08: 30',
    '09: 30',
    '10: 30',
    '11: 30',
    '12: 30',
    '13: 30',
    '14: 30',
    '15: 30',
    '16: 30',
    '17: 30',
  ],
};

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
  const [preference, setPreference] = useState('');
  const [placeholder, setPlaceholder] = useState('');
  const [options, setOptions] = useState<string[]>([]);

  useEffect(() => {
    if (isThirdFilled) {
      props.setCurrentFilled(true);
    }
  }, [isThirdFilled]);
  const s = 'Day Preferences';
  const dayPreferences = preferences[s];
  return (
    <Space
      key={props.key}
      style={{ display: 'flex', marginBottom: 8 }}
      align="baseline"
    >
      <Form.Item
        {...props.restField}
        name={[props.name, 'first']}
        rules={[{ required: true, message: 'Missing first name' }]}
      >
        <Select
          placeholder="Select Preference"
          style={{ width: 190 }}
          onChange={(key: keyof typeof preferences) => {
            setIsFirstFilled(true);
            setPreference(key);
            setPlaceholder('Select ' + key.split(' ')[0]);
            setOptions(preferences[key]);
          }}
        >
          {Object.keys(preferences).map((key) => (
            <Select.Option key={key} value={key}>
              {key}
            </Select.Option>
          ))}
        </Select>
      </Form.Item>
      {isFirstFilled && (
        <Form.Item
          {...props.restField}
          name={[props.name, 'second']}
          rules={[{ required: true, message: 'Missing first name' }]}
        >
          <Select
            placeholder={placeholder}
            style={{ width: 190 }}
            onChange={() => {
              setIsSecondFilled(true);
            }}
          >
            {options.map((key) => (
              <Select.Option key={key} value={key}>
                {key}
              </Select.Option>
            ))}
            {/* <Select.Option value="Monday">Monday</Select.Option>
            <Select.Option value="Tuesday">Tuesday</Select.Option>
            <Select.Option value="Wednesday">Wednesday</Select.Option>
            <Select.Option value="Thursday">Thursday</Select.Option>
            <Select.Option value="Friday">Friday</Select.Option> */}
          </Select>
        </Form.Item>
      )}
      {isSecondFilled && (
        <Form.Item
          {...props.restField}
          name={[props.name, 'third']}
          rules={[{ required: true, message: 'Missing first name' }]}
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
