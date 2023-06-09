import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import Left from './TRIO/Left';
import Mid from './TRIO/Mid';
import Right from './TRIO/Right';

const StyledContainer = styled.div`
  display: flex;
  justify-content: space-between;
  height: 220px;
  border: 2px solid black;
  border-radius: 10px;
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
      <StyledMid courses={props.openedCourses} schedule={props.schedule} />
      <StyledRight plan={props.schedule.future_plan} />
    </StyledContainer>
  );
};

export default FuturePlan;
