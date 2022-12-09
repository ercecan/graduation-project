import React from "react";
import styled from "styled-components";
import LoginCard from "../components/LoginCard";
import { useNavigate } from "react-router-dom";
import { StyledCommonContainer } from "../GeneralStyle";

const LoginContainer = styled.div`
  width: 100%;
  height: 100%;
`;
const StyledText = styled.p`
  position: absolute;
  bottom: 50px;
  left: 35%;
`;

const Login = (): JSX.Element => {
  const navigate = useNavigate();
  const handleClick = () => {
    navigate("/register");
  };
  return (
    <StyledCommonContainer>
      <LoginContainer>
        <LoginCard />
        <StyledText>
          If you have no account, please{" "}
          <button onClick={handleClick}>click here</button> to registeration
        </StyledText>
      </LoginContainer>
    </StyledCommonContainer>
  );
};

export default Login;
