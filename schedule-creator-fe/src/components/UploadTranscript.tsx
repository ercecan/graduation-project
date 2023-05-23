import React from 'react';
import { UploadOutlined } from '@ant-design/icons';
import { Button, message, Upload } from 'antd';

const UploadTranscript = (props: any) => {
  const beforeUpload = (file: any) => {
    if (file.type !== 'application/pdf') {
      message.error('Only PDF files are allowed');
      return false;
    }
    return true;
  };

  const handleUpload = (info: any) => {
    props.setTranscriptData({
      '2018-2019 Bahar Dönemi': [
        {
          code: 'ING 112',
          name: 'English I',
          letter_grade: 'AA',
        },
        {
          code: 'MAT 103E',
          name: 'Mathematics I',
          letter_grade: 'AA',
        },
      ],
      '2019-2020 Güz Dönemi': [
        {
          code: 'FIZ 101EL',
          name: 'Physics I Laboratory',
          letter_grade: 'AA',
        },
        {
          code: 'BLG 223E',
          name: 'Data Structures',
          letter_grade: 'BA',
        },
      ],
      '2019-2020 Bahar Dönemi': [
        {
          code: 'BLG 242E',
          name: 'Logic Circuits Laboratory',
          letter_grade: 'BA',
        },
        {
          code: 'FIZ 102EL',
          name: 'Physics II Laboratory',
          letter_grade: 'AA',
        },
      ],
    });
  };

  return (
    <Upload
      name="file"
      headers={{
        authorization: 'authorization-text',
      }}
      onChange={handleUpload}
    >
      <Button icon={<UploadOutlined />}>Click to Upload</Button>
    </Upload>
  );
};

export default UploadTranscript;
