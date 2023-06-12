import { Typography, Spin } from 'antd';
import { LoadingOutlined } from '@ant-design/icons';
import React from 'react';

const { Title } = Typography;

const LoadingSpinner = (props: any) => {
  return (
    <div style={{ marginTop: '3%', marginBottom: '3%', textAlign: 'center' }}>
      <Spin size="large" indicator={<LoadingOutlined />} />
      <Title level={1} style={{ marginTop: '0.5%' }}>
        {props.text}
      </Title>
    </div>
  );
};

export default LoadingSpinner;
