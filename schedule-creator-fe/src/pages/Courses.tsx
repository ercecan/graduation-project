import React, { useEffect, useState } from 'react';
import { Button, List } from 'antd';
import { DeleteOutlined, EditOutlined } from '@ant-design/icons';
import axios from 'axios';
import ModalComponent from '../components/ModalComponent';

interface Course {
  id: string;
  name: string;
  description: string;
  grade: string;
  code: string;
  term: string;
  year: string;
  semester: string;
}

const Courses = (): JSX.Element => {
  const [modalOpen, setModalOpen] = useState(false);
  const [data, setData] = useState<Course[]>([]);
  const [isEdit, setIsEdit] = useState<boolean>();
  const [modalData, setModalData] = useState({
    id: '',
    code: '',
    name: '',
    grade: '',
    term: '',
    description: '',
  });

  const fetchItems = () =>
    axios
      .post(
        'http://34.107.96.1:8000/api/student/taken?student_id=' +
          sessionStorage.getItem('student_db_id'),
      )
      .then((res) => {
        setData(
          res.data.map((item: any) => {
            const course: Course = {
              id: item.id,
              name: item.course.name,
              description: item.course.description,
              grade: item.grade,
              code: item.course.code,
              term: item.term.year + ' ' + item.term.semester.toUpperCase(),
              year: item.term.year,
              semester: item.term.semester,
            };
            return course;
          }),
        );
      });

  useEffect(() => {
    fetchItems();
  }, []);

  const handleEdit = (item: Course) => {
    setModalData(item);
    setIsEdit(true);
    setModalOpen(true);
    console.log('Edit -> ' + item.code);
    // edit taken
    // fetchItems();
  };

  const handleAdd = () => {
    setIsEdit(false);
    setModalOpen(true);
  };

  const handleDelete = (itemID: string) => {
    axios.delete(
      `http://34.107.96.1:8000/api/course/taken?student_id=${sessionStorage.getItem(
        'student_db_id',
      )}&course_id=${itemID}`,
    );
    fetchItems();
  };

  return (
    <div>
      <div
        id="scrollableDiv"
        style={{
          height: '85vh',
          overflow: 'auto',
          padding: '0 16px',
          border: '1px solid rgba(140, 140, 140, 0.35)',
        }}
      >
        <div>
          <List
            dataSource={data}
            renderItem={(item) => (
              <div>
                <List.Item key={item.code}>
                  <div style={{ width: '70px' }}>{item.code}</div>
                  <div style={{ width: '280px' }}>{item.name}</div>
                  <div style={{ width: '60px' }}>{item.grade}</div>
                  <div style={{ width: '100px' }}>{item.term}</div>
                  <div style={{ width: '200px' }}>
                    {item.description
                      ? item.description.slice(0, 20) + '...'
                      : 'No Content :('}
                  </div>

                  <div>
                    <button onClick={() => handleEdit(item)}>
                      <EditOutlined />
                    </button>
                    <button
                      style={{ marginLeft: '20px' }}
                      onClick={() => handleDelete(item.id)}
                    >
                      <DeleteOutlined />
                    </button>
                  </div>
                </List.Item>
              </div>
            )}
          />
        </div>
      </div>
      {modalOpen && (
        <ModalComponent
          isEdit={isEdit}
          modalOpen={modalOpen}
          setModalOpen={setModalOpen}
          modalData={modalData}
          fetchItems={fetchItems}
        />
      )}
      <Button
        onClick={() => {
          handleAdd();
        }}
        type="primary"
        style={{ margin: '8px' }}
      >
        Add Course
      </Button>
    </div>
  );
};

export default Courses;
function setEditableFields(arg0: (prevFields: any) => any[]) {
  throw new Error('Function not implemented.');
}
