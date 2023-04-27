import { Typography, Spin } from "antd";
import { LoadingOutlined } from "@ant-design/icons";
import React from "react";

const { Title } = Typography;

const LoadingSpinner = () => {
  return (
    <div style={{ marginTop: "3%", marginBottom: "3%", textAlign: "center" }}>
      <Spin size="large" indicator={<LoadingOutlined />} />
      <Title level={4} style={{ marginTop: "0.5%" }}>
        Loading...
      </Title>
    </div>
  );
};

export default LoadingSpinner;
