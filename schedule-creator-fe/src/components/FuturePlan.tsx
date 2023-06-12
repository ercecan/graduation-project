import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import Left from './TRIO/Left';
import Mid from './TRIO/Mid';
import Right from './TRIO/Right';
import { Spin } from 'antd';

const StyledContainer = styled.div`
  display: flex;
  justify-content: space-between;
  height: 220px;
  border: 2px solid black;
  border-radius: 10px;

  .loading-component {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`;

const StyledLeft = styled(Left)`
  flex: 1;
`;

const StyledMid = styled(Mid)`
  flex: 1;
`;

const StyledRight = styled(Right)`
  flex: 1;
`;

const FuturePlan = (props: any): JSX.Element => {
  const [valid, setValid] = useState(true);
  const [counter, setCounter] = useState(0);

  return (
    <StyledContainer>
      <StyledLeft preferences={props.schedule.preferences} />
      <StyledMid
        courses={props.openedCourses}
        schedule={props.schedule}
        setLoading={props.setLoading}
      />
      <StyledRight plan={props.schedule.future_plan} loading={props.loading} />
    </StyledContainer>
  );
};

export default FuturePlan;
