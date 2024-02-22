import React, { useState, useEffect } from 'react';
import {
  Box,
  FormControl,
  FormLabel,
  Input,
  Button,
  Heading,
  Text,
} from '@chakra-ui/react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';

function KH_Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    setError('');
  }, [username, password]);

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/kids/login/', {
        email: username,
        password,
      });

      if (response.data && response.data.access) {
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
        navigate('/attendance');
      } else {
        setError('Invalid username or password');
      }
    } catch (error) {
      setError('Login failed. Please try again later.');
      console.error('Login failed:', error);
    }
  };

  return (
    <>
      <Navbar />
      <Box
        maxW="400px"
        margin="auto"
        mt="20vh"
        p="6"
        borderWidth="1px"
        borderRadius="lg"
      >
        <Heading mb="4">Login</Heading>
        <FormControl>
          <FormLabel>Username</FormLabel>
          <Input
            type="text"
            value={username}
            onChange={handleUsernameChange}
            mb="2"
          />

          <FormLabel>Password</FormLabel>
          <Input
            type="password"
            value={password}
            onChange={handlePasswordChange}
            mb="4"
          />

          {error && <Text color="red.500">{error}</Text>}

          <Button colorScheme="blue" onClick={handleLogin}>
            Login
          </Button>
        </FormControl>
      </Box>
    </>
  );
}

export default KH_Login;
