import React, { useEffect, useState } from 'react';
import styled from 'styled-components';

const StyledContainer = styled.div`
  width: 100%;
  border-right: 2px solid black;
  overflow-y: auto;

  .data-list {
    background-color: #f4f4f4;
    padding: 10px;
  }

  .list-item {
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 10px;
    padding: 10px;
  }

  .list-item strong {
    font-weight: bold;
  }
`;

const Left = (props: any): JSX.Element => {
  const [valid, setValid] = useState(true);
  const [counter, setCounter] = useState(0);

  return (
    <StyledContainer>
      <div className="data-list">
        {props.preferences.map((item: any, index: any) => (
          <div className="list-item" key={index}>
            <div>
              <strong>Type:</strong> {item.type}
            </div>
            <div>
              <strong>Value:</strong> {item.value}
            </div>
            <div>
              <strong>Priority:</strong> {item.priority}
            </div>
          </div>
        ))}
      </div>
    </StyledContainer>
  );
};

export default Left;
