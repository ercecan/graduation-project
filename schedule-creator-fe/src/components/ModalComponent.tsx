import React, { useEffect, useRef, useState } from 'react';
import { Avatar, Divider, List, Modal, Skeleton } from 'antd';
import InfiniteScroll from 'react-infinite-scroll-component';
import axios from 'axios';
import styled from 'styled-components';
import { isAwaitExpression } from 'typescript';

const StyledModal = styled(Modal)`
  .my-form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 0 auto;
  }

  .form-group {
    margin-bottom: 10px;
  }

  label {
    font-weight: bold;
  }

  input[type='text'] {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    padding: 8px 16px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #45a049;
  }
`;

interface UpdateType {
  student_id: string;
  course_id: string;
  grade: string;
  term: { year: string; semester: string };
}

interface AddType {
  name: string;
  code: string;
  description: string;
  grade: string;
  term: { year: string; semester: string };
}

const ModalComponent = (props: any): JSX.Element => {
  const [updateData, setUpdateData] = useState<UpdateType>();
  const [addData, setAddData] = useState<AddType>();
  const [courses, setCourses] = useState();
  const [selected, setSelected] = useState<string>();

  const addRequest = () => {
    axios
      .post('http://34.107.96.1:8000/api/course/update/taken', updateData)
      .then(() => {
        console.log('Success');
      });
  };

  useEffect(() => {
    axios
      .get(
        `http://34.107.96.1:8000/api/course/remaining?student_id=` +
          sessionStorage.getItem('student_db_id'),
      )
      .then((res) => {
        setCourses(res.data);
      });
  }, []);

  const handleUpdateModalSave = () => {
    if (!(gradeRef.current && yearRef.current && semesterRef.current)) return;
    axios
      .post('http://34.107.96.1:8000/api/course/update/taken', {
        student_id: sessionStorage.getItem('student_db_id') || '',
        course_id: props.modalData.id,
        grade: gradeRef.current.value,
        term: {
          semester: semesterRef.current.value.toLowerCase(),
          year: yearRef.current.value,
        },
      })
      .then(() => {
        props.fetchItems();
      });
    props.setModalOpen(false);
  };

  const handleAddModalSave = () => {
    if (!(gradeRef.current && yearRef.current && semesterRef.current)) return;
    axios
      .post('http://34.107.96.1:8000/api/course/add/taken', {
        student_id: sessionStorage.getItem('student_db_id') || '',
        course_id: selected,
        grade: gradeRef.current.value,
        term: {
          semester: semesterRef.current.value.toLowerCase(),
          year: yearRef.current.value,
        },
      })
      .then(() => {
        props.fetchItems();
      });
    props.setModalOpen(false);
  };

  useEffect(() => {
    if (codeRef.current)
      codeRef.current.value = props.isEdit ? props.modalData.code : '';
    if (nameRef.current)
      nameRef.current.value = props.isEdit ? props.modalData.name : '';
    if (gradeRef.current)
      gradeRef.current.value = props.isEdit ? props.modalData.grade : '';
    if (yearRef.current)
      yearRef.current.value = props.isEdit ? props.modalData.year : '';
    if (semesterRef.current)
      semesterRef.current.value = props.isEdit
        ? props.modalData.semester.toUpperCase()
        : '';
    if (descriptionRef.current)
      descriptionRef.current.value = props.isEdit
        ? props.modalData.description
        : '';
  }, []);

  const codeRef = useRef<HTMLInputElement>(null);
  const nameRef = useRef<HTMLInputElement>(null);
  const gradeRef = useRef<HTMLInputElement>(null);
  const yearRef = useRef<HTMLInputElement>(null);
  const semesterRef = useRef<HTMLInputElement>(null);
  const descriptionRef = useRef<HTMLInputElement>(null);

  return (
    <StyledModal
      open={props.modalOpen}
      onCancel={() => props.setModalOpen(false)}
      onOk={() =>
        props.isEdit ? handleUpdateModalSave() : handleAddModalSave()
      }
    >
      {props.isEdit && (
        <form className="my-form" onSubmit={handleUpdateModalSave}>
          <h2
            style={{
              fontSize: '20px',
              fontWeight: 'bold',
              marginBottom: '16px',
            }}
          >
            Edit Course
          </h2>
          <div className="form-group">
            <label htmlFor="grade">Grade:</label>
            <input id="grade" type="text" ref={gradeRef} />
          </div>
          <div className="form-group">
            <label htmlFor="year">Year:</label>
            <input id="year" type="text" ref={yearRef} />
          </div>
          <div className="form-group">
            <label htmlFor="semester">Semester:</label>
            <input id="semester" type="text" ref={semesterRef} />
          </div>
        </form>
      )}

      {!props.isEdit && (
        <form className="my-form" onSubmit={handleAddModalSave}>
          <h2
            style={{
              fontSize: '20px',
              fontWeight: 'bold',
              marginBottom: '16px',
            }}
          >
            Add Course
          </h2>
          <div className="form-group">
            <label htmlFor="course">Course:</label>
            <select
              id="course"
              onChange={(e) => {
                console.log(e.target.value);
                setSelected(e.target.value);
              }}
            >
              {(courses || []).map((course: { _id: string; name: string }) => (
                <option key={course._id} value={course._id}>
                  {course.name}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="grade">Grade:</label>
            <input id="grade" type="text" ref={gradeRef} />
          </div>
          <div className="form-group">
            <label htmlFor="year">Year:</label>
            <input id="year" type="text" ref={yearRef} />
          </div>
          <div className="form-group">
            <label htmlFor="semester">Semester:</label>
            <input id="semester" type="text" ref={semesterRef} />
          </div>
        </form>
      )}
    </StyledModal>
  );
};

export default ModalComponent;
