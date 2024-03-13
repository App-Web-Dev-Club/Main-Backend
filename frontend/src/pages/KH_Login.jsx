import React, { useState, useEffect } from "react";
import {
  Box,
  FormControl,
  FormLabel,
  Input,
  Button,
  Heading,
  Text,
} from "@chakra-ui/react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import "./pages.css";

function KH_Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [showUsernameEmoji, setShowUsernameEmoji] = useState(true); // State to control username emoji visibility
  const [showPasswordEmoji, setShowPasswordEmoji] = useState(true); // State to control password emoji visibility
  const navigate = useNavigate();

  useEffect(() => {
    setError("");
  }, [username, password]);

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleUsernameFocus = () => {
    setShowUsernameEmoji(false); // Hide username emoji when username input is focused
  };

  const handleUsernameBlur = () => {
    if (!username) {
      setShowUsernameEmoji(true); // Show username emoji if username input is blurred and username is empty
    }
  };

  const handlePasswordFocus = () => {
    setShowPasswordEmoji(false); // Hide password emoji when password input is focused
  };

  const handlePasswordBlur = () => {
    if (!password) {
      setShowPasswordEmoji(true); // Show password emoji if password input is blurred and password is empty
    }
  };

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://localhost:8000/kids/login/", {
        email: username,
        password,
      });

      if (response.data && response.data.access) {
        axios.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${response.data.access}`;
        navigate("/attendance");
      } else {
        setError("Invalid username or password");
      }
    } catch (error) {
      setError("Login failed. Please try again later.");
      console.error("Login failed:", error);
    }
  };

  return (
    <>
      
      <div className="LoginCard">
        <Box maxW="400px" margin="auto"  p="6">
          <Heading style={{ textAlign: "center", marginBottom: "20px" }}>
          <img
                className="logo"
                src="../src/assets/KH_Logo.png"
                alt="Logo"

              />
          </Heading>
          <FormControl>
            <FormLabel>Username</FormLabel>
            <Input id="Usename"
              color={"black"}
              type="text"
              placeholder={showUsernameEmoji ? "👤" : ""}
              onFocus={handleUsernameFocus}
              onBlur={handleUsernameBlur}
              value={username}
              onChange={handleUsernameChange}
              mb="2"
            />
            <FormLabel>Password</FormLabel>
            <Input id="Pass"
              type="password"
              value={password}
              placeholder={showPasswordEmoji ? "🔑" : ""}
              onFocus={handlePasswordFocus}
              onBlur={handlePasswordBlur}
              onChange={handlePasswordChange}
              mb="4"
            />
            {error && <Text color="red.500">{error}</Text>}
            <div style={{alignItems:"center", paddingLeft:"80px"}}>
              <Button
              className="loginB"
                bg="rgba(0,0,0,0.1)"
                color="black"
                border="1px solid black"
                _hover={{ bg: "rgba(0,0,0,0.2)" }}
                onClick={handleLogin}
                style={{width:"60%"}}
              >
                Login
              </Button>
            </div>
          </FormControl>
        </Box>
      </div>
    </>
  );
}

export default KH_Login;
