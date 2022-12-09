import React from "react";
import "./App.css";
import Login from "./pages/Login";
import Panel from "./pages/Panel";
import { Route, Routes } from "react-router-dom";
import Signup from "./pages/Signup";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route exact path="/" element={<Login />} />
        <Route exact path="/register" element={<Signup />} />
        <Route exact path="/panel" element={<Panel />} />
      </Routes>
    </div>
  );
}

export default App;
