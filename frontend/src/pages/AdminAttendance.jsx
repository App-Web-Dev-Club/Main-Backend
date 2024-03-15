import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Spinner,
  Select,
} from "@chakra-ui/react";

import AdminNavbar from "../components/AdminNavbar";

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-GB");
}

function formatTime(dateTimeString) {
    const dateTime = new Date(dateTimeString);
    return dateTime.toLocaleTimeString("en-US", { hour12: true });
  }

function AdminAttendance() {
  const [attendanceData, setAttendanceData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedClub, setSelectedClub] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/kids/routers/attendance/?search=${selectedClub}`
        );
        setAttendanceData(response.data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchData();
  }, [selectedClub]);

  const handleClubChange = (event) => {
    setSelectedClub(event.target.value);
  };

  if (loading) {
    return <Spinner size="xl" color="blue.500" />;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      <AdminNavbar />
      <h1
        style={{
          textAlign: "center",
          fontSize: "36px",
          fontWeight: "bold",
          marginBottom: "20px",
        }}
      >
        Attendance Data
      </h1>
      <div>
        <div style={{ paddingBottom: "70px" }} className="form_">
          <Select
            placeholder="Select a club"
            value={selectedClub}
            onChange={handleClubChange}
          >
            <option value="KH Core">KH Core</option>
            <option value="3D">3D</option>
            <option value="AI">AI</option>
            <option value="WEB AND APP">Web And App</option>
            <option value="IOT AND ROBOTICS">Iot And Robotics</option>
            <option value="XR">XR</option>
            <option value="CYBER SECURITY">Cyber Security</option>
            <option value="COMPETITIVE PROGRAMMING">
              Competitive Programming
            </option>
            <option value="BUILD CLUB">Build Club</option>
            <option value="GDSC">Google Developers Student Club</option>
            <option value="NSN">Nvidia Student Network</option>
            <option value="Ecell core">E-Cell Core</option>
            <option value="Accelerator club">Accelerator Club</option>
            <option value="Women Entrepreneur Club">
              Women Entrepreneurs Club
            </option>
            <option value="Resource hub">Resource Hub</option>
            <option value="Start up">Start Up Club</option>
            <option value="Kreatives core">Kreatives Core</option>
            <option value="TEDX">TED-X</option>
            <option value="Design club">Design Club</option>
            <option value="Writters club">Writers Club</option>
            <option value="KIDS">KIDS</option>
          </Select>
        </div>

        <Table variant="simple">
          <Thead>
            <Tr>
              <Th>Register No</Th>
              <Th>Name</Th>
              <Th>Project Title</Th>
              <Th>Description</Th>
              <Th>Work Done</Th>
              <Th>Date</Th>
              <Th>Time</Th>
            </Tr>
          </Thead>
          <Tbody>
            {attendanceData.map((item) => (
              <Tr key={item.id}>
                <Td>{item.user.regno.register_no}</Td>
                <Td>{item.user.regno.user.name}</Td>
                <Td>{item.project.title}</Td>
                <Td>{item.project.description}</Td>
                <Td>{item.work_done}</Td>
                <Td>{formatDate(item.date_time)}</Td>
                <Td>{formatTime(item.date_time)}</Td>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </div>
    </>
  );
}

export default AdminAttendance;
