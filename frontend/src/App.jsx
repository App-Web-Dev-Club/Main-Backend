import React from 'react';
import KH_Login from './pages/KH_Login';
import KH_Register from './pages/KH_Register';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Projects from './pages/Projects';
import ProtectedRoute from './components/ProtectedRoute';
import Attendance from './pages/Attendance';
import Permission from './pages/Permission';
import Punchtime from './pages/Punchtime';
import Hackathon from './pages/Hackathon';
// import { HackathonDetails } from './components/HackathonDetails';
// import Hackathonreg from './pages/Hackathon_add';
function App() {
  return (

    <Routes>
      <Route index element={<KH_Login />} />
      <Route path='login' element={<KH_Login />} />
      {/* <Route path='register' element={<KH_Register/>} /> */}
      <Route path='projects' element={
       
          <Projects />
      
      } />
      <Route path='attendance' element={

          <Attendance />
  
      } />
      <Route path='permission' element={<Permission />} />
      <Route path='punch' element={<Punchtime />} />
      {/* <Route path='test' element={<Hackathonreg/>} /> */}
      <Route path='hackathon' element={<Hackathon />} />
      {/* <Route path='hackathon/details' element={<HackathonDetails/>} /> */}
      {/* <Route path='details' element={<HackathonDetails/>} /> */}

    </Routes>
  );
}

export default App;
