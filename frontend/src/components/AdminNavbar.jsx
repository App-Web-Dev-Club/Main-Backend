import React, { useState } from "react";
import { Box, Flex, Spacer, Heading, Link } from "@chakra-ui/react";
import { Link as ReactRouterLink, useLocation } from "react-router-dom";
import "./Nav.css";

const AdminNavbar = () => {
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
              to="/admin/punch"
              className={activeLink === "/admin/punch" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/admin/punch")}
            >
              Punch data
            </Link>
            <Link
              as={ReactRouterLink}
              to="/admin/clubs"
              className={activeLink === "/admin/clubs" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/admin/clubs")}
            >
              Club data
            </Link>

            <Link
              as={ReactRouterLink}
              to="/admin/attendance"
              className={activeLink === "/admin/attendance" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/admin/attendance")}
            >
              Attendance data
            </Link>

            <Link
              as={ReactRouterLink}
              to="/admin/attendance/graph"
              className={activeLink === "/admin/attendance/graph" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/admin/attendance/graph")}
            >
              Attendance Graph
            </Link>

            <Link
              as={ReactRouterLink}
              to="/admin/projects"
              className={activeLink === "/admin/projects" ? "link active" : "link"}
              mx="2"
              onClick={() => setActiveLink("/admin/projects")}
            >
              Projects data
            </Link>
          </Box>
        </Flex>
      </Box>
    </div>
  );
};

export default AdminNavbar;
