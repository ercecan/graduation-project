import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import {
  FormControl,
  FormControlLabel,
  Checkbox,
  FormGroup,
  FormLabel,
  Input,
  Button,
} from '@mui/material';
import axios from 'axios';

const StyledContainer = styled.div`
  width: 100%;
  border-right: 2px solid black;
  overflow: auto;
`;

const StyledForm = styled.form`
  margin: 5px;
`;

const Mid = (props: any): JSX.Element => {
  const [items, setItems] = useState({});
  const [term, setTerm] = useState<string | undefined>(undefined);

  const handleChange = (event: any) => {
    setItems({
      ...items,
      [event.target.name]: event.target.checked,
    });
  };

  const name_to_id = new Map([]);
  const schedule = props.schedule;
  schedule.courses.map((course: { course: { name: unknown }; id: unknown }) => {
    name_to_id.set(course.course.name, course.id);
  });

  const handleSubmit = (event: any) => {
    event.preventDefault();
    // console.log(term);
    // console.log(
    //   Object.keys({
    //     ...items,
    //     course_name: false,
    //     course_name_2: true,
    //   })
    //     .filter((key: any) => items[key as keyof typeof items] === true)
    //     .map((name) => name_to_id.get(name)),
    // );

    axios
      .post('http://0.0.0.0:8000/api/recommendation', {
        message: 'create recommendation',
        schedule_id: schedule.id,
        student_id: sessionStorage.getItem('student_id'),
        semester: schedule.term.semester,
        year: schedule.term.year,
        term_number: term,
        failed_courses: Object.keys({
          ...items,
          course_name: false,
          course_name_2: true,
        })
          .filter((key: any) => items[key as keyof typeof items] === true)
          .map((name) => name_to_id.get(name)),
      })
      .then((res) => {
        console.log(res);
      });
  };

  const formItems = props.courses.map((course: any) => {
    return (
      <FormControlLabel
        control={<Checkbox onChange={handleChange} name={course.course.name} />}
        label={course.course.name}
        className="checkbox-item"
      />
    );
  });

  return (
    <StyledContainer>
      <StyledForm onSubmit={handleSubmit}>
        <FormControl component="fieldset">
          <FormLabel component="legend" className="form-label">
            Potential Fails
          </FormLabel>
          <FormGroup>{formItems}</FormGroup>
          <FormGroup>
            <FormControlLabel
              control={
                <Input
                  onChange={(event) => {
                    setTerm(event.target.value);
                  }}
                  value={term}
                  name="term"
                  style={{ width: 20, marginLeft: 'auto' }}
                />
              }
              label="Term"
              className="input-item"
            />
          </FormGroup>
          <br />
          <Button variant="contained" type="submit" className="submit-button">
            Submit
          </Button>
        </FormControl>
      </StyledForm>
    </StyledContainer>
  );
};

export default Mid;
