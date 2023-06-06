import React from 'react';
import './App.css';
import Login from './pages/Login';
import Panel from './pages/Panel';
import { Route, Routes } from 'react-router-dom';
import Signup from './pages/Signup';
import MyLayout from './components/Layout';
import Profile from './components/Profile';
import ScheduleTable from './components/ScheduleTable';
import Schedule from './pages/Schedule';
import Courses from './pages/Courses';

function App() {
  return (
    <div className="App">
      <MyLayout>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route path="/register" element={<Signup />} />
          <Route path="/panel" element={<Panel />} />
          <Route path="/home" element={<ScheduleTable />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/schedule/:id" element={<Schedule />} />
        </Routes>
      </MyLayout>
    </div>
  );
}

export default App;
