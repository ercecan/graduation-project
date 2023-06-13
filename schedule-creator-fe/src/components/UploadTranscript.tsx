import React from 'react';
import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';
import axios from 'axios';
import type { RcFile, UploadFile } from 'antd/es/upload/interface';

const UploadTranscript = () => {
  const beforeUpload = (file: any) => {
    if (file.type !== 'application/pdf') {
      message.error('Only PDF files are allowed');
      return false;
    }
    return true;
  };

  const handleUpload = (file: any) => {
    const formData = new FormData();
    console.log(file);
    formData.append('transcript', file.file.originFileObj);
    axios.post(
      'http://34.107.96.1:8000/api/transcript?student_id=' +
        sessionStorage.getItem('student_db_id'),
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      },
    );
  };

  return (
    <Upload
      name="file"
      headers={{
        authorization: 'authorization-text',
      }}
      onChange={handleUpload}
      action={undefined}
    >
      <Button icon={<UploadOutlined />}>Click to Upload</Button>
    </Upload>
  );
};

export default UploadTranscript;
