// import React from "react";
import { Box, Flex, Spacer, Heading, Link } from "@chakra-ui/react";
import { Link as ReactRouterLink } from "react-router-dom";
import "./Nav.css"
const Navbar = () => {
  return (
    <div>
    <Box boxShadow="md" p="4" bg="black" marginBottom={"20px"}>
      <Flex alignItems="center">
        <Heading color="black" >
          <Box>
            <img className="nav-bar-logo" src="../src/assets/KH_Logo.png" alt="Your Image" />
          </Box>
        </Heading>
        <Spacer />
        <Box >
          {/* <Link as={ReactRouterLink} to="/login" color="black" mx="2">
            Login
          </Link> */}

          {/* <Link as={ReactRouterLink} to="/register" color="black" mx="2">
            Registation
          </Link> */}

          <Link className="link" as={ReactRouterLink} to="/projects" color="white" mx="2">
            Project
          </Link>

          <Link className="link" as={ReactRouterLink} to="/attendance" color="white" mx="2">
            Attendance
          </Link>

          <Link  className="link" as={ReactRouterLink} to="/permission" color="white" mx="2">
            Permission
          </Link>

          {/* <Link className="link" as={ReactRouterLink} to="/admin/punch" color="white" mx="2">
            Punch
          </Link> */}

          <Link className="link" as={ReactRouterLink} to="/hackathon" color="white " mx="2">
            Hackathon
          </Link>
        </Box>
        {/* <Button colorScheme="teal" ml="2">
          Login
        </Button> */}
      </Flex>
    </Box>
    </div>
  );
};

export default Navbar;
