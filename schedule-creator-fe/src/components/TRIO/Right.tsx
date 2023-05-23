import React, { useEffect, useState } from 'react';
import styled from 'styled-components';

const StyledContainer = styled.div`
  width: 100%;
  padding: 20px;
  overflow-y: auto;
  .schedule-item {
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 20px;
    padding: 20px;
  }

  h2 {
    margin-bottom: 10px;
  }

  ul {
    padding: 0;
    list-style-type: none;
  }

  .course-item {
    background-color: #f4f4f4;
    padding: 10px;
    margin-bottom: 5px;
    width: 160px;
  }
`;

const Right = (props: any): JSX.Element => {
  const [valid, setValid] = useState(true);
  const [counter, setCounter] = useState(0);
  console.log(props);
  return (
    <StyledContainer>
      {props.plan.map((planItem: any, index: any) => (
        <div className="schedule-item" key={index}>
          <h2>
            Schedule for {planItem.term.semester} {planItem.term.year}
          </h2>
          <ul>
            {planItem.course_names.map((course: any, courseIndex: any) => (
              <li className="course-item" key={courseIndex}>
                {course}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </StyledContainer>
  );
};

export default Right;
