import React from "react";
import "./App.css";
import Login from "./pages/Login";
import Panel from "./pages/Panel";
import { Route, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route exact path="/" element={<Login />} />
        <Route exact path="/panel" element={<Panel />} />
      </Routes>
    </div>
  );
}

export default App;
