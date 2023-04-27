import React, { useState } from "react";
import styled from "styled-components";
import { useNavigate, useParams } from "react-router-dom";
import { ScheduleView, createTheme } from "react-schedule-view";

const StyledScheduleView = styled(ScheduleView)`
  width: 500px;
  heigth: 400px;
`;
const Schedule = (): JSX.Element => {
  const navigate = useNavigate();
  const { id } = useParams();
  const routeLogin = () => {
    navigate("/");
  };

  const theme = createTheme("apple", {
    hourHeight: "53px",
    style: {
      dayLabels: {
        fontWeight: "bold",
      },
    },
  });

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
        <StyledScheduleView
          daySchedules={data}
          viewStartTime={8}
          viewEndTime={17}
          theme={theme}
        />
  );
};

export default Schedule;
