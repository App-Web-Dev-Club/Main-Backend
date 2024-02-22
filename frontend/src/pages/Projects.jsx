import React, { useState, useEffect } from "react";
import {
  FormControl,
  FormLabel,
  Input,
  Button,
  Text,
  Flex,
  IconButton,
  Alert,
  AlertIcon,
} from "@chakra-ui/react";
import { CloseIcon } from "@chakra-ui/icons";
import Navbar from "../components/Navbar";
import axios from "axios";

function Projects() {
  const [leaderNo, setLeaderNo] = useState("");
  const [leaderData, setLeaderData] = useState(null);
  const [leaderVerificationStatus, setLeaderVerificationStatus] = useState(null);

  const [memberNo, setMemberNo] = useState("");
  const [memberData, setMemberData] = useState(null);
  const [memberVerificationStatus, setMemberVerificationStatus] = useState(null);

  const [members, setMembers] = useState([]);
  const [alertMessage, setAlertMessage] = useState("");

  const [projectTitle, setProjectTitle] = useState("");
  const [projectDescription, setProjectDescription] = useState("");

  useEffect(() => {
    if (memberData && memberData.register_no && memberVerificationStatus === "verified") {
      setMembers([...members, { ...memberData }]);
      setMemberNo(""); // Clear memberNo after successfully adding a member
    }
  }, [memberData, memberVerificationStatus]);

  const handleLeaderVerification = async () => {
    const apiUrl = "http://127.0.0.1:8000/kids/userid";

    try {
      const response = await axios.post(apiUrl, { register_no: leaderNo });
      
      if (response.status === 201 || response.status === 200) {
        const data = response.data;
        if (data && data.register_no) {
          setLeaderData(data);
          setLeaderVerificationStatus("verified");
        } else {
          setLeaderVerificationStatus("notfound");
        }
      } else {
        setLeaderVerificationStatus("notfound");
        console.error("Failed to send leader data. Status:", response.status);
      }
    } catch (error) {
      setLeaderVerificationStatus("notfound");
      console.error("Error sending leader data:", error);
    }
  };

  const handleMemberVerification = async (register_no) => {
    const apiUrl = "http://127.0.0.1:8000/kids/userid";
    
    try {
      const response = await axios.post(apiUrl, { register_no: register_no });
      
      if (response.status === 201 || response.status === 200) {
        const data = response.data;
        if (data && data.register_no) {
          setMemberData(data);
          setMemberVerificationStatus("verified");
          setAlertMessage("");
          return true;
        } else {
          setMemberVerificationStatus("notfound");
          setAlertMessage("Member not registered.");
        }
      } else {
        setMemberVerificationStatus("notfound");
        setAlertMessage("Member not found.");
      }
    } catch (error) {
      setMemberVerificationStatus("notfound");
      setAlertMessage("Error checking member data. Please try again.");
    }

    return false;
  };

  const handleAddMember = async () => {
    if (leaderVerificationStatus !== "verified") {
      setAlertMessage("Please verify the leader first.");
      return;
    }
  
    await handleLeaderVerification();
  
    if (leaderVerificationStatus === "verified") {
      const isMemberVerified = await handleMemberVerification(memberNo);
      
      if (!isMemberVerified) {
        console.error("Member verification failed.");
      }
    }
  };

  const handleDeleteMember = (index) => {
    const updatedMembers = [...members];
    updatedMembers.splice(index, 1);
    setMembers(updatedMembers);
  };

  const handleSubmit = async () => {
    if (leaderVerificationStatus !== "verified" || members.length === 0) {
      setAlertMessage("Please verify the leader and add at least one member.");
      return;
    }

    const projectsApiUrl = "http://127.0.0.1:8000/kids/projects";
    console.log(members.map((member) => member.id))
    try {
      const response = await axios.post(projectsApiUrl, {
        title: projectTitle,
        description: projectDescription,
        project_lead: leaderData.id,
        kh_members: members.map((member) => member.id),
        status: "hold",
      });

      if (response.status === 201) {
        console.log("Project submitted successfully!");
      } else {
        console.error("Failed to submit project. Status:", response.status);
      }
    } catch (error) {
      console.error("Error submitting project:", error);
    }
  };

  return (
    <>
      <Navbar />
      <FormControl>
        <FormLabel>Title</FormLabel>
        <Input
          type="text"
          value={projectTitle}
          onChange={(e) => setProjectTitle(e.target.value)}
        />

        <FormLabel>Description</FormLabel>
        <Input
          type="text"
          value={projectDescription}
          onChange={(e) => setProjectDescription(e.target.value)}
        />

        <FormLabel>Team Leader No.</FormLabel>
        <Input
          type="text"
          value={leaderNo}
          onChange={(e) => {
            setLeaderNo(e.target.value);
            setLeaderVerificationStatus(null);
          }}
        />

        <Button
          style={{ marginTop: "1rem" }}
          onClick={handleLeaderVerification}
          colorScheme="green"
        >
          Verify Leader
        </Button>

        {leaderVerificationStatus === "verified" && leaderData && (
          <Text color="green" mt={2}>
            &#10004; Leader Verified: {leaderData.register_no}
          </Text>
        )}

        {leaderVerificationStatus === "notfound" && (
          <Text color="red" mt={2}>
            &#10008; Leader not found or invalid
          </Text>
        )}

        <FormLabel mt={4}>Add members</FormLabel>
        {alertMessage && (
          <Alert status="error" mb={4}>
            <AlertIcon />
            {alertMessage}
          </Alert>
        )}
        <Flex direction="column">
          {leaderVerificationStatus === "verified" && (
            <>
              {members.map((member, index) => (
                <Flex key={index} align="center" mt={2}>
                  {member && member.register_no ? (
                    <>
                      <Input
                        type="text"
                        value={member.register_no}
                        isReadOnly
                        placeholder="Member name"
                      />
                      <IconButton
                        icon={<CloseIcon />}
                        aria-label="Delete member"
                        onClick={() => handleDeleteMember(index)}
                        ml={2}
                        colorScheme="red"
                      />
                    </>
                  ) : null}
                </Flex>
              ))}
              <Flex align="center" mt={2}>
                <Input
                  type="text"
                  value={memberNo}
                  onChange={(e) => setMemberNo(e.target.value)}
                  placeholder="Member No."
                />
                <Button
                  style={{ marginLeft: "1rem" }}
                  colorScheme="green"
                  onClick={handleAddMember}
                >
                  Add Member
                </Button>
              </Flex>
            </>
          )}
        </Flex>
        <Button
          style={{ marginTop: "1rem" }}
          onClick={handleSubmit}
          colorScheme="blue"
        >
          Submit Project
        </Button>
      </FormControl>
    </>
  );
}

export default Projects;
