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
  const [alertMessage, setAlertMessage] = useState("");





  const handleSubmit = async () => {
    if (!selectedForm) {
      setAlertMessage("Please select a form type.");
      return;
    }

    console.log(selectedForm);
    const projectsApiUrl = "http://localhost:8000/kids/permission";
    try {
      const response = await axios.post(projectsApiUrl, {
        form_type: selectedForm,
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

        setAlertMessage("");
        setSelectedForm("");
      } else {
        console.error("Failed to submit project. Status:", response.status);
      }
    } catch (error) {
      console.error("Error submitting project:", error);
    }
  };



  const handleFormChange = (event) => {
    setSelectedForm(event.target.value);
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
        Permission
      </h1>
      <div className="form_">
        <Select
          mt={10}
          placeholder="Select club"
          value={selectedForm}
          onChange={handleFormChange}
        >
          <option value="Late Permission">Late Permission</option>
          <option value="Night Stay Permission">Night Stay Permission</option>
        </Select>
        {alertMessage && (
          <Alert status="error" mb={4} width={350} mx={700} mt={5}>
            <AlertIcon />
            {alertMessage}
          </Alert>
        )}
        <div style={{ paddingRight:"20px"}}>
          <Button
            style={{ marginTop: "1rem" ,width:"100%"}}
            onClick={handleSubmit}
            colorScheme="green"
          >
            Submit form
          </Button>
        </div>
      </div>
    </>
  );
}
