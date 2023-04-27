import React from "react";
import styled from "styled-components";
import { useNavigate } from "react-router-dom";
import { StyledCommonContainer } from "../GeneralStyle";

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
    navigate("/");
  };
  return (
    <StyledCommonContainer>
      <StyledContainer>
        <StyledHeader>Welcome to Schedule Creator Website</StyledHeader>
        {/* Profile - Settings (tc yükle, öğrenci bilgileri)
        HomePage (Schedule'lar (gözat butonu, sil butonu), Yeni shcedule olıuştur butonu Modal olacak)
        Schedule_Detail -> 1 schedule için her türlü ayrıntı  */}
      </StyledContainer>
    </StyledCommonContainer>
  );
};

export default Panel;
