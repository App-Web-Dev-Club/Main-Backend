import React, { useState } from "react";
import Navbar from "../components/Navbar";
import {
  Flex,
  FormLabel,
  Input,
  Select,
  Button,
  Alert,
  AlertIcon,
} from "@chakra-ui/react";
import axios from "axios";
import jsPDF from "jspdf";
import "jspdf-autotable";

export default function Permission() {
  const [selectedForm, setSelectedForm] = useState("");
  const [leaderNo, setLeaderNo] = useState("");
  const [leaderData, setLeaderData] = useState(null);
  const [memberNo, setMemberNo] = useState("");
  const [memberData, setMemberData] = useState(null);
  const [memberVerificationStatus, setMemberVerificationStatus] = useState(null);
  const [members, setMembers] = useState([]);
  const [alertMessage, setAlertMessage] = useState("");
  const [projectTitle, setProjectTitle] = useState("");
  const [projectDescription, setProjectDescription] = useState("");

  const handleMemberVerification = async (regno) => {
    const apiUrl = "http://127.0.0.1:8000/kids/userid";

    try {
      const response = await axios.post(apiUrl, { register_no: regno });

      if (response.status === 201) {
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
        setAlertMessage("Failed to check member data. Please try again.");
      }
    } catch (error) {
      setMemberVerificationStatus("notfound");
      setAlertMessage("Error checking member data. Please try again.");
    }

    return false;
  };

  const handleAddMember = async () => {
    const isMemberVerified = await handleMemberVerification(memberNo);
  
    if (isMemberVerified) {
      if (memberData && memberData.register_no && memberData.id) {
        setMembers([...members, { ...memberData }]);
        setMemberNo("");
        setMemberData(null); // Reset member data
        setMemberVerificationStatus(null); // Reset member verification status
      } else {
        console.error("Invalid member data after verification:", memberData);
      }
    }
  };
  

  const handleDeleteMember = (index) => {
    const updatedMembers = [...members];
    updatedMembers.splice(index, 1);
    setMembers(updatedMembers);
    setMemberVerificationStatus(null); // Reset member verification status
  };

  const handleSubmit = async () => {
    if (members.length === 0 || !selectedForm) {
      setAlertMessage("Please add at least one member and select a form type.");
      return;
    }
    console.log(members.map((member) => member.id));
    console.log(selectedForm);
    const projectsApiUrl = "http://127.0.0.1:8000/kids/permission";
    try {
      const response = await axios.post(projectsApiUrl, {
        user: members.map((member) => member.id),
        type: selectedForm,
      });

      if (response.status === 201) {
        console.log("Form updated  successfully!");

        // Generate and download the PDF
        if (selectedForm == "Late Permission") {
          // generateLatePDF(response.data);
        } else {
          // generateNightPDF(response.data);
        }

        // Reset form fields after successful submission if needed
        setProjectTitle("");
        setProjectDescription("");
        setLeaderNo("");
        setMemberNo("");
        setMembers([]);
        setLeaderData(null);
        setMemberData(null);
        setMemberVerificationStatus(null);
        setAlertMessage("");
      } else {
        console.error("Failed to submit project. Status:", response.status);
      }
    } catch (error) {
      console.error("Error submitting project:", error);
    }
  };

  const generateLatePDF = (data) => {
    const pdf = new jsPDF();

    data.forEach((item, index) => {
      if (index > 0) {
        pdf.addPage();
      }

      pdf.text(
        `Date: ${new Date(item.date_time).toLocaleDateString()}`,
        160,
        20
      );
      pdf.text("From", 10, 20);

      pdf.text(
        `   Head CTC/KIDS,
    Karunya Institute of Technology and Sciences.`,
        20,
        30
      );

      pdf.text("To", 10, 50);
      pdf.text(
        `   The Chief Warden (Boys Hostel),
    Karunya Institute of Technology and Science,
    Coimbatore-641114`,
        20,
        60
      );

      pdf.text("Subject", 10, 90);
      pdf.text(`Re: Permission for ${item.type}`, 20, 100);

      pdf.text("Respected Sir,", 20, 110);
      const textLines = [
        "The following students were working late at CTC on",
        `${new Date(item.date_time).toLocaleDateString()} Till 07:30PM. Kindly permit them to enter the hostel.`,
      ];

      textLines.forEach((line, i) => {
        pdf.text(line, 20, 120 + i * 10);
      });

      const columns = ["Sl No", "Name", "Reg No"];
    
      const rows = item.user.map((user,i) => [i + 1, user.name, user.register_no]);

      pdf.autoTable({
        startY: 160,
        head: [columns],
        body: rows,
      });

      pdf.setFontSize(12);
      pdf.setTextColor(0);
      pdf.text("Thank You.", 80, pdf.autoTable.previous.finalY + 20);
      pdf.text("(HOD CTC/KIDS)", 170, pdf.autoTable.previous.finalY + 30);
    });

    pdf.save("LateEntryPermission.pdf");
  };

  const generateNightPDF = (data) => {
    const pdf = new jsPDF();

    data.forEach((item, index) => {
      if (index > 0) {
        pdf.addPage();
      }

      pdf.text(
        `Date: ${new Date(item.date_time).toLocaleDateString()}`,
        160,
        20
      );
      pdf.text("From", 10, 20);

      pdf.text(
        `   Head CTC/KIDS,
    Karunya Institute of Technology and Sciences.`,
        20,
        30
      );

      pdf.text("To", 10, 50);
      pdf.text(
        `   The Chief Warden (Boys Hostel),
    Karunya Institute of Technology and Science,
    Coimbatore-641114`,
        20,
        60
      );

      pdf.text("Subject", 10, 90);
      pdf.text(`Re: Permission for ${item.type}`, 20, 100);

      pdf.text("Respected Sir,", 20, 110);
      const textLines = [
        "The following students were working late at CTC on",
        `${new Date(
          item.date_time
        ).toLocaleDateString()} Till 11:30PM. Kindly permit them to enter the hostel.`,
      ];

      textLines.forEach((line, i) => {
        pdf.text(line, 20, 120 + i * 10);
      });

      const columns = ["Sl No", "Name", "Reg No"];
      const rows = item.user.map((user,i) => [i + 1, user.name, user.regno]);

      pdf.autoTable({
        startY: 160,
        head: [columns],
        body: rows,
      });

      pdf.setFontSize(12);
      pdf.setTextColor(0);
      pdf.text("Thank You.", 80, pdf.autoTable.previous.finalY + 20);
      pdf.text("(HOD CTC/KIDS)", 170, pdf.autoTable.previous.finalY + 30);
    });

    pdf.save("LateEntryPermission.pdf");
  };

  const handleFormChange = (event) => {
    setSelectedForm(event.target.value);
  };

  return (
    <>
      <Navbar />

      <FormLabel>Form Type</FormLabel>
      <Select
        placeholder="Select club"
        value={selectedForm}
        onChange={handleFormChange}
      >
        <option value="Late Permission">Late Permission</option>
        <option value="Night Stay Permission">Night Stay Permission</option>
      </Select>

      <FormLabel mt={4}>Add members</FormLabel>
      {alertMessage && (
        <Alert status="error" mb={4}>
          <AlertIcon />
          {alertMessage}
        </Alert>
      )}
      <Flex direction="column">
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
                  <Button
                    onClick={() => handleDeleteMember(index)}
                    ml={2}
                    colorScheme="red"
                  >
                    Delete Member
                  </Button>
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
      </Flex>
      <Button
        style={{ marginTop: "1rem" }}
        onClick={handleSubmit}
        colorScheme="blue"
      >
        Submit form
      </Button>
    </>
  );
}
