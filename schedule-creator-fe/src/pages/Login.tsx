import React from 'react';
import styled from 'styled-components';
import LoginCard from '../components/LoginCard';
import { useNavigate } from 'react-router-dom';
import { StyledCommonContainer } from '../GeneralStyle';

const StyledLoginContainer = styled.div`
  display: flex;
  flex-direction: column;
  width: fit-content;
  margin-left: auto;
  margin-right: auto;
  align-items: center;
  padding-top: 10%;
  padding-right: 20%;
`;

const StyledText = styled.p`
  display: flex;
  padding-left: 40px;
`;

const Login = (): JSX.Element => {
  const navigate = useNavigate();
  const handleClick = () => {
    navigate('/register');
  };
  return (
    <StyledCommonContainer>
      <StyledLoginContainer>
        <LoginCard />
        <StyledText>
          If you have no account,&nbsp;
          <button onClick={handleClick}>click here</button>&nbsp;to
          registration.
        </StyledText>
      </StyledLoginContainer>
    </StyledCommonContainer>
  );
};

export default Login;
