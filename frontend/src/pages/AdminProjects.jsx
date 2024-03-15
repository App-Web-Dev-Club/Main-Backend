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

function AdminProjects() {
  const [projectsData, setProjectsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedClub, setSelectedClub] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/kids/routers/projects/?search=${selectedClub}`
        );
        setProjectsData(response.data);
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
        Projects Data
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
        <Table variant="simple"> {/* Set variant to "simple" */}
          <Thead>
            <Tr>
              <Th>Title</Th>
              <Th>Description</Th>
              <Th>Status</Th>
              <Th>Project Lead</Th>
              <Th>Register Number (Project Lead)</Th>
              <Th>KH Members</Th>
            </Tr>
          </Thead>
          <Tbody>
            {projectsData.map((project) => (
              <Tr key={project.id}>
                <Td>{project.title}</Td>
                <Td>{project.description}</Td>
                <Td>{project.status}</Td>
                <Td>
                  {project.project_lead.regno.user.name}
                </Td>
                <Td>
                  {project.project_lead.regno.register_no}
                </Td>
                <Td>
                  {project.kh_members.map((member) => (
                    <div key={member.id}>
                      {member.regno.user.name} - {member.regno.register_no} ({member.club})
                    </div>
                  ))}
                </Td>
              </Tr>
            ))}
          </Tbody>
        </Table>
      </div>
    </>
  );
}

export default AdminProjects;
