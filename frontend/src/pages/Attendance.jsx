import React, { useState, useEffect, useCallback } from "react";
import {
  FormControl,
  FormLabel,
  Input,
  Button,
  Select,
  Box,
  Flex
} from "@chakra-ui/react";
import "./pages.css"
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
    const apiUrl = "http://localhost:8000/kids/memberid/projects";

    try {
      const response = await axios.post(apiUrl, { register_no: registerNo });

      if (response.status === 201) {
        const data = response.data;
        console.log(data)
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

  useEffect(() => {
    // Clear other fields when registerNo changes
    setSelectedProject("");
    setWorkDone("");
    setProjects([]);
  }, [registerNo]);

  const handleSubmitAttendance = async () => {
    const attendanceApiUrl = 'http://localhost:8000/kids/attendance';
  
    try {
      const response = await axios.post(attendanceApiUrl, {
        register_no: registerNo,
        project: selectedProject,
        work_done: workDone,
      });
  
      if (response.status === 201) {
        console.log('Attendance submitted successfully!');
        // Reset form fields after successful submission
        setRegisterNo("");
        setSelectedProject("");
        setWorkDone("");
      } else {
        console.error('Failed to submit attendance. Status:', response.status);
      }
    } catch (error) {
      console.error('Error submitting attendance:', error);
      if (error.response && error.response.status === 401) {
        // If 401 error occurs, display an alert message
        window.alert('Please login to submit attendance.');
      }
    }
  };
  

  return (
    <>
      <Navbar />
      <h1
        style={{
          textAlign: "center",
          fontSize: "36px",
          fontWeight: "bold",
          marginBottom: "20px",
        }}
      >
        Attendance 
      </h1>
      <div className="form_">
        <FormControl>
          {/* <FormLabel marginLeft={700} marginTop={10}>Register No</FormLabel> */}
         
            <Flex alignItems="center">
              <Input
                type="text"
                placeholder="Register No"
                value={registerNo}
              
                onChange={(e) => setRegisterNo(e.target.value)}
                style={{ marginRight: "1rem" }}
              />
              <div style={{ paddingBottom: "20px" }}>
                <Button
                  colorScheme="green"
                  style={{paddingTop:"4px"}}
                  onClick={handleVerify}
                  isLoading={isLoading}
                >
                  Verify
                </Button>
              </div>
            </Flex>
          
          {/* Display projects once verified */}
          {projects.length > 0 && (
            <>
              {/* <FormLabel mt={4}>Select Project</FormLabel> */}
              <Select
                placeholder="Select project"
                value={selectedProject}
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
              {/* <FormLabel mt={4}>Work Done</FormLabel> */}
              <div style={{paddingTop:"20px"}}>
                <Input
                  placeholder="Work Done"
                
                  type="text"
                  value={workDone}
                  onChange={(e) => setWorkDone(e.target.value)}
                />
              </div>
              <div style={{paddingRight:"20px"}}>
                <Button
                style={{width:"100%"}}
                  mt={4}
                  colorScheme="blue"
                  onClick={handleSubmitAttendance}
                  isLoading={isLoading} // Disable the button while submitting
                >
                  Submit Attendance
                </Button>
              </div>
            </>
          )}
        </FormControl>
      </div>
    </>
  );
};

export default Attendance;
