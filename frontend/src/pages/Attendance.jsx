import React, { useState, useEffect, useCallback } from "react";
import {
  FormControl,
  FormLabel,
  Input,
  Button,
  Select,
  Box,
} from "@chakra-ui/react";

import Navbar from "../components/Navbar";
import axios from "axios";

const Attendance = () => {
  const [registerNo, setRegisterNo] = useState("");
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState("");
  const [workDone, setWorkDone] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleVerify = useCallback(async () => {
    setIsLoading(true);
    const apiUrl = "http://127.0.0.1:8000/kids/userid/projects";

    try {
      const response = await axios.post(apiUrl, { register_no: registerNo });

      if (response.status === 200) {
        const data = response.data;
        setProjects(data.member.concat(data.lead));
      } else {
        console.error("Failed to fetch projects. Status:", response.status);
      }
    } catch (error) {
      console.error("Error fetching projects:", error);
    } finally {
      setIsLoading(false);
    }
  }, [registerNo]);

  const handleSubmitAttendance = async () => {
    const attendanceApiUrl = 'http://127.0.0.1:8000/kids/attendance';
  
    try {
      console.log({
        register_no: registerNo,
        project: selectedProject,
        work_done: workDone,
      })
      const response = await axios.post(attendanceApiUrl, {
        register_no: registerNo,
        project: selectedProject,
        work_done: workDone,
      });
  
      if (response.status === 200) {
        console.log('Attendance submitted successfully!');
        // Optionally, you can reset the form or perform other actions upon successful submission
      } else {
        console.error('Failed to submit attendance. Status:', response.status);
      }
    } catch (error) {
      console.error('Error submitting attendance:', error);
    }
  };

  useEffect(() => {
    handleVerify();
  }, [handleVerify]); // Run the verification on component mount and when registerNo changes

  return (
    <>
      <Navbar />
      <FormControl>
        <FormLabel>Register No</FormLabel>
        <Input
          type="text"
          value={registerNo}
          onChange={(e) => setRegisterNo(e.target.value)}
        />
        <Button
          colorScheme="green"
          style={{ marginTop: "1rem" }}
          onClick={handleVerify}
          isLoading={isLoading}
        >
          Verify
        </Button>

        {/* Display projects once verified */}
        {projects.length > 0 && (
          <>
            <FormLabel mt={4}>Select Project</FormLabel>
            <Select
              placeholder="Select project"
              onChange={(e) => setSelectedProject(e.target.value)}
            >
              {projects.map((project) => (
                <option key={project.id} value={project.id}>
                  {project.title}
                  {project.lead &&
                    project.lead.length > 0 &&
                    project.lead[0].id === parseInt(registerNo) && (
                      <Box
                        as="span"
                        ml={2}
                        color="white"
                        bg="blue"
                        px={2}
                        py={1}
                        borderRadius="md"
                      >
                        Lead
                      </Box>
                    )}
                </option>
              ))}
            </Select>

            <FormLabel mt={4}>Work Done</FormLabel>
            <Input
              type="text"
              value={workDone}
              onChange={(e) => setWorkDone(e.target.value)}
            />

            <Button
              mt={4}
              colorScheme="blue"
              onClick={handleSubmitAttendance}
              isLoading={isLoading} // Disable the button while submitting
            >
              Submit Attendance
            </Button>
          </>
        )}
      </FormControl>
    </>
  );
};

export default Attendance;
