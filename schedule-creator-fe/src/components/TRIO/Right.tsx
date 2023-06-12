import { Spin } from 'antd';
import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import LoadingSpinner from '../common/LoadingSpinner';

const StyledContainer = styled.div`
  width: 600px;
  padding: 20px;
  overflow-y: auto;
  .schedule-item {
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 20px;
    padding: 20px;
  }

  .no-data {
    text-align: center;
    color: gray;
    font-style: italic;
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
  const [loading, setLoading] = useState(true);

  return (
    <StyledContainer>
      {props.loading ? (
        <LoadingSpinner />
      ) : props.plan && props.plan.length > 0 ? (
        props.plan.map((planItem: any, index: any) => (
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
        ))
      ) : (
        <div className="no-data">No data available</div>
      )}
    </StyledContainer>
  );
};

export default Right;
