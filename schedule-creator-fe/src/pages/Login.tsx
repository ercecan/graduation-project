import React from "react";
import styled from "styled-components";
import LoginCard from "../components/LoginCard";
import { StyledCommonContainer } from "../GeneralStyle";

const LoginContainer = styled.div`
  width: 100%;
  height: 100%;
`;

const Login = (): JSX.Element => {
  return (
    <StyledCommonContainer>
      <LoginContainer>
        <LoginCard />
      </LoginContainer>
    </StyledCommonContainer>
  );
};

export default Login;
