import React from "react";
import { Box, Flex, Spacer, Heading, Button, Link } from "@chakra-ui/react";
import { Link as ReactRouterLink } from "react-router-dom";

const Navbar = () => {
  return (
    <Box boxShadow="md" p="4" bg="white" marginBottom={"20px"}>
      <Flex alignItems="center">
        <Heading color="black" >
          <Box>
            <img className="nav-bar-logo" src="../src/assets/KH_Logo.png" alt="Your Image" />
          </Box>
        </Heading>
        <Spacer />
        <Box>
          {/* <Link as={ReactRouterLink} to="/login" color="black" mx="2">
            Login
          </Link> */}

          {/* <Link as={ReactRouterLink} to="/register" color="black" mx="2">
            Registation
          </Link> */}

          <Link as={ReactRouterLink} to="/projects" color="black" mx="2">
            Project
          </Link>

          <Link as={ReactRouterLink} to="/attendance" color="black" mx="2">
            Attendance
          </Link>

          <Link as={ReactRouterLink} to="/permission" color="black" mx="2">
            Permission
          </Link>

          <Link as={ReactRouterLink} to="/punch" color="black" mx="2">
            Punch
          </Link>

          <Link as={ReactRouterLink} to="/hackathon" color="black" mx="2">
            Hackathon
          </Link>
        </Box>
        {/* <Button colorScheme="teal" ml="2">
          Login
        </Button> */}
      </Flex>
    </Box>
  );
};

export default Navbar;
