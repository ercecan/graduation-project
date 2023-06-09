import React from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import { StyledCommonContainer } from '../GeneralStyle';

const StyledContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
`;

const StyledHeader = styled.header`
  position: absolute;
  top: 20px;
`;

const Panel = (): JSX.Element => {
  const navigate = useNavigate();
  const routeLogin = () => {
    navigate('/');
  };
  return (
    <StyledCommonContainer>
      <StyledContainer>
        <StyledHeader>Welcome to Schedule Creator Website</StyledHeader>
      </StyledContainer>
    </StyledCommonContainer>
  );
};

export default Panel;
