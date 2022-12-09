import React from "react";
import styled from "styled-components";
import SignupCard from "../components/SignupCard";
import { StyledCommonContainer } from "../GeneralStyle";

const LoginContainer = styled.div`
  width: 100%;
  height: 100%;
`;

const Signup = (): JSX.Element => {
  return (
    <StyledCommonContainer>
      <LoginContainer>
        <SignupCard />
      </LoginContainer>
    </StyledCommonContainer>
  );
};

export default Signup;
