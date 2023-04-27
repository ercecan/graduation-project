import React, { useState } from "react";
import styled from "styled-components";
import { useNavigate, useParams } from "react-router-dom";
import { StyledCommonContainer } from "../GeneralStyle";
import { ScheduleView } from "react-schedule-view";

const StyledContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
`;

const StyledScheduleView = styled(ScheduleView)`
  width: 700px;
  heigth: 400px;
`;
const Schedule = (): JSX.Element => {
  const navigate = useNavigate();
  const { id } = useParams();
  const routeLogin = () => {
    navigate("/");
  };

  const data = [
    {
      name: "Monday",
      events: [
        {
          startTime: 12,
          endTime: 14,
          title: "",
          description:
            "Follow the signs to the registration desk inside the north entrance",
        },
        {
          startTime: 14.5,
          endTime: 15.75,
          title: "",
          description: "Lecture",
        },
        {
          startTime: 9,
          endTime: 10,
          title: "",
        },
      ],
    },
    {
      name: "Tuesday",
      events: [
        {
          startTime: 12.5,
          endTime: 15.75,
          title: "",
          description: "Lecture",
        },
        {
          startTime: 15,
          endTime: 17,
          title: "",
          description: "Lecture",
        },
      ],
    },
    {
      name: "Wednesday",
      events: [
        {
          startTime: 9,
          endTime: 10,
          title: "",
          description: "Lecture",
        },
        {
          startTime: 11.5,
          endTime: 12,
          title: "",
          description: "Lecture",
        },
        {
          startTime: 13,
          endTime: 14,
          title: "",
          description: "Lecture",
        },
      ],
    },
    {
      name: "Thursday",
      events: [
        {
          startTime: 12,
          endTime: 15,
          title: "",
          description: "Lecture",
        },
        {
          startTime: 9,
          endTime: 11,
          title: "",
          description: "Lecture",
        },
      ],
    },
    {
      name: "Friday",
      events: [
        {
          startTime: 15,
          endTime: 16,
          title: "",
          description: "Lecture",
        },
      ],
    },
  ];

  return (
    <StyledCommonContainer>
      <StyledContainer>
        <StyledScheduleView
          daySchedules={data}
          viewStartTime={9}
          viewEndTime={15}
        />
      </StyledContainer>
    </StyledCommonContainer>
  );
};

export default Schedule;
