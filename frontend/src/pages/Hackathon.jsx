import React, { useState } from 'react';
import axios from 'axios';
import {
  FormControl,
  FormLabel,
  Input,
  Button,
  InputGroup,
  InputRightElement,
  Textarea,
  Box,
  Stack,
  Checkbox,
  FormErrorMessage,
} from "@chakra-ui/react";

const Hackathon = () => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    conducting_team: '',
    registration_date: '',
    registration_link: '',
    whatsapp_link: '',
    gcr_code: '',
    end_date: '',
    banner: null,
    active: true
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleFileChange = (e) => {
    // console.log(e.target.files[0]['name']);
    setFormData({
      ...formData,
      banner: e.target.files[0]['name']
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formDataToSend = new FormData();
    Object.keys(formData).forEach((key) => {
      if (key === "banner") {
        // Check if banner exists and is not null
        if (formData[key]) {
          // Append the banner file with the directory path
          formDataToSend.append(key, `hacakthon/banner/${formData[key]}`);
        }
      } else {
        formDataToSend.append(key, formData[key]);
      }
    });
  
    try {
        console.log(formDataToSend)
      const response = await axios.post(
        "http://127.0.0.1:8000/kids/hackathon",
        formDataToSend
      );
      console.log("Upload successful:", response);
      // Handle success, maybe show a success message or redirect the user
    } catch (error) {
      console.error("Error uploading data:", error);
      // Handle error, maybe show an error message to the user
    }
  };
  

  return (
    <Box p={4}>
      <form onSubmit={handleSubmit}>
        <Stack spacing={4}>
          <FormControl id="name">
            <FormLabel>Name</FormLabel>
            <Input type="text" name="name" value={formData.name} onChange={handleChange} />
          </FormControl>

          <FormControl id="description">
            <FormLabel>Description</FormLabel>
            <Textarea name="description" value={formData.description} onChange={handleChange} />
          </FormControl>

          <FormControl id="conducting_team">
            <FormLabel>Conducting Team</FormLabel>
            <Input type="text" name="conducting_team" value={formData.conducting_team} onChange={handleChange} />
          </FormControl>

          <FormControl id="registration_date">
            <FormLabel>Registration Date and Time</FormLabel>
            <Input type="datetime-local" name="registration_date" value={formData.registration_date} onChange={handleChange} />
          </FormControl>

          <FormControl id="registration_link">
            <FormLabel>Registration Link</FormLabel>
            <Input type="url" name="registration_link" value={formData.registration_link} onChange={handleChange} />
          </FormControl>

          <FormControl id="whatsapp_link">
            <FormLabel>WhatsApp Link</FormLabel>
            <Input type="url" name="whatsapp_link" value={formData.whatsapp_link} onChange={handleChange} />
          </FormControl>

          <FormControl id="gcr_code">
            <FormLabel>GCR Code</FormLabel>
            <Input type="text" name="gcr_code" value={formData.gcr_code} onChange={handleChange} />
          </FormControl>

          <FormControl id="end_date">
            <FormLabel>End Date and Time</FormLabel>
            <Input type="datetime-local" name="end_date" value={formData.end_date} onChange={handleChange} />
          </FormControl>

          <FormControl id="banner">
            <FormLabel>Banner</FormLabel>
            <Input type="file" name="banner" onChange={handleFileChange} />
          </FormControl>

          <FormControl id="active">
            <FormLabel>Active</FormLabel>
            <Checkbox name="active" defaultChecked={formData.active} onChange={(e) => setFormData({...formData, active: e.target.checked})}>Active</Checkbox>
          </FormControl>

          <Button type="submit" colorScheme="blue">Upload</Button>
        </Stack>
      </form>
    </Box>
  );
};

export default Hackathon;
