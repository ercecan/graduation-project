import React from "react";
import "./App.css";
import Login from "./pages/Login";
import Panel from "./pages/Panel";
import { Route, Routes } from "react-router-dom";
import Signup from "./pages/Signup";
import MyLayout from "./components/Layout";
import Profile from "./components/Profile";
import ScheduleTable from "./components/ScheduleTable";
import Schedule from "./pages/Schedule";

function App() {
  return (
    <div className="App">
      <MyLayout>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route exact path="/register" element={<Signup />} />
          <Route exact path="/panel" element={<Panel />} />
          <Route exact path="/home" element={<ScheduleTable />} />
          <Route exact path="/profile" element={<Profile />} />
          <Route exact path="/schedule/:id" element={<Schedule />} />
        </Routes>
      </MyLayout>
    </div>
  );
}

export default App;
