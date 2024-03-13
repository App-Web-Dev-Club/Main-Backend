import React, { useState } from "react";
import { Box, Flex, Spacer, Heading, Link } from "@chakra-ui/react";
import { Link as ReactRouterLink, useLocation } from "react-router-dom";
import "./Nav.css";

const Navbar = () => {
  const location = useLocation();
  const [activeLink, setActiveLink] = useState(location.pathname);

  return (
    <div>
      <Box boxShadow="md" p="4" bg="white" marginBottom={"20px"}>
        <Flex alignItems="center">
          <Heading color="black">
            <Box>
              <img
                className="nav-bar-logo"
                src="../src/assets/KH_Logo.png"
                alt="Logo"
              />
            </Box>
          </Heading>
          <Spacer />
          <Box>
            <Link
              as={ReactRouterLink}
              to="/projects"
              className={activeLink === "/projects" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/projects")}
            >
              Project
            </Link>

            <Link
              as={ReactRouterLink}
              to="/attendance"
              className={activeLink === "/attendance" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/attendance")}
            >
              Attendance
            </Link>

            <Link
              as={ReactRouterLink}
              to="/permission"
              className={activeLink === "/permission" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/permission")}
            >
              Permission
            </Link>

            <Link
              as={ReactRouterLink}
              to="/hackathon"
              className={activeLink === "/hackathon" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/hackathon")}
            >
              Hackathon
            </Link>
          </Box>
        </Flex>
      </Box>
    </div>
  );
};

export default Navbar;
