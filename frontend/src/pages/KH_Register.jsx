import React, { useState } from 'react';
import {
  FormControl,
  FormLabel,
  Input,
  Select,
  Button
} from '@chakra-ui/react';
import axios from 'axios';
import Navbar from '../components/Navbar';



function KH_Register() {
  const [registerNo, setRegisterNo] = useState('');
  const [kmail, setKmail] = useState('');
  const [contactNumber, setContactNumber] = useState('');
  const [joinedDate, setJoinedDate] = useState('');
  const [hostel, setHostel] = useState('');
  const [selectedRole, setSelectedRole] = useState('MEMBER');
  const [selectedClub, setSelectedClub] = useState('');
  const [password, setPassword] = useState('');
  const [name,SetName] = useState('')

  const handleRegisterNoChange = (event) => {
    setRegisterNo(event.target.value.toUpperCase());
  };

  const handleName = (event) => {
    SetName(event.target.value);
  };

  const handleKmailChange = (event) => {
    setKmail(event.target.value);
  };

  const handleContactNumberChange = (event) => {
    setContactNumber(event.target.value);
  };

  const handleJoinedDateChange = (event) => {
    setJoinedDate(event.target.value);
  };

  const handleHostelChange = (event) => {
    setHostel(event.target.value);
  };

  const handleRoleChange = (event) => {
    setSelectedRole(event.target.value);
  };

  const handleClubChange = (event) => {
    setSelectedClub(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleFormSubmit = async () => {
    const formData = {
      name:name,
      regno: registerNo,
      kmail,
      contact_number: contactNumber,
      joined_date: joinedDate,
      hostel,
      permission: selectedRole,
      club: selectedClub,
      password
    };
    console.log(formData)
    
    try {
      const response = await axios.post('http://localhost:8000/kids/register', formData);

      if (response.status === 201) {
        console.log('Form data successfully submitted!');
        // You can add further logic here based on the response from the server
      } else {
        console.error('Failed to submit form data.');
      }
    } catch (error) {
      console.error('Error occurred while submitting form data:', error);
    }
  };

  return (
    <>
    <Navbar />
      <FormControl>

      <FormLabel>Name</FormLabel>
        <Input type="text" value={name} onChange={handleName} />

        <FormLabel>Register No</FormLabel>
        <Input type="text" value={registerNo} onChange={handleRegisterNoChange} />

        <FormLabel>Kmail</FormLabel>
        <Input type="email" value={kmail} onChange={handleKmailChange} />

        <FormLabel>Contact Number</FormLabel>
        <Input type="integer" value={contactNumber} onChange={handleContactNumberChange} />

        <FormLabel>Joined Date</FormLabel>
        <Input type="date" value={joinedDate} onChange={handleJoinedDateChange} />

        <FormLabel>Hostel</FormLabel>
        <Input type="text" value={hostel} onChange={handleHostelChange} />

        <FormLabel>Select Role</FormLabel>
        <Select placeholder="Select Role" value={selectedRole} onChange={handleRoleChange}>
          <option value="MEMBER">MEMBER</option>
        </Select>

        <FormLabel>Select club</FormLabel>
        <Select placeholder="Select club" value={selectedClub} onChange={handleClubChange}>
          <option value="3D">3D</option>
          <option value="WEB_AND_APP">WEB_AND_APP</option>
          <option value="IOT_AND_ROBOTICS">IOT_AND_ROBOTICS</option>
          <option value="XOR">XOR</option>
          <option value="CYBERSECURITY">CYBERSECURITY</option>
          <option value="COMPETITIVE_PROGRAMMING">COMPETITIVE_PROGRAMMING</option>
        </Select>

        <FormLabel>Password</FormLabel>
        <Input type="password" value={password} onChange={handlePasswordChange} />
      </FormControl>

      <Button onClick={handleFormSubmit}>Save</Button>
    </>
  );
}

export default KH_Register;
