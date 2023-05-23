import React, { useState } from 'react';
import styled from 'styled-components';
import { ScheduleView, createTheme } from 'react-schedule-view';

const StyledScheduleView = styled(ScheduleView)`
  width: 500px;
  heigth: 400px;
`;

const ScheduleDetail = (props: any): JSX.Element => {
  const theme = createTheme('apple', {
    hourHeight: '53px',
    style: {
      dayLabels: {
        fontWeight: 'bold',
      },
    },
  });

  return (
    <StyledScheduleView
      daySchedules={props.data}
      viewStartTime={8}
      viewEndTime={17}
      theme={theme}
    />
  );
};

export default ScheduleDetail;
