import React from "react";
import { Box, Flex, Spacer, Heading, Button, Link } from "@chakra-ui/react";
import { Link as ReactRouterLink } from "react-router-dom";

const Navbar = () => {
  return (
    <Box boxShadow="md" p="4" bg="blue.500">
      <Flex alignItems="center">
        <Heading color="white">KH</Heading>
        <Spacer />
        <Box>
          <Link as={ReactRouterLink} to="/login" color="white" mx="2">
            Login
          </Link>

          {/* <Link as={ReactRouterLink} to="/register" color="white" mx="2">
            Registation
          </Link> */}

          <Link as={ReactRouterLink} to="/projects" color="white" mx="2">
            Project
          </Link>

          <Link as={ReactRouterLink} to="/attendance" color="white" mx="2">
            Attendance
          </Link>

          <Link as={ReactRouterLink} to="/permission" color="white" mx="2">
            Permission
          </Link>

          <Link as={ReactRouterLink} to="/punch" color="white" mx="2">
            Punch
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
