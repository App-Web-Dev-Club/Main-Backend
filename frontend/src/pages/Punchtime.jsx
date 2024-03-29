import React, { useState } from "react";
import {
  FormControl,
  FormLabel,
  Input,
  Select,
  Button,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
} from "@chakra-ui/react";
import axios from "axios";
// import Navbar from "../components/Navbar";
import AdminNavbar from "../components/AdminNavbar";

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-GB");
}

function Punchtime() {
  const [selectedFilter, setSelectedFilter] = useState("");
  const [regNo, setRegNo] = useState("");
  const [punchData, setPunchData] = useState([]);

  const handleFilterChange = (event) => {
    setSelectedFilter(event.target.value);
  };

  const handleFilterClick = async () => {
    try {

      let payload = { type: selectedFilter };

      if (selectedFilter === "User") {
        payload.register_no = regNo;
      }

      const response = await axios.post(
        "http://localhost:8000/kids/punchtime/sort",
        payload
      );

      // Assuming the API response contains the punch data
      setPunchData(response.data);
      console.log(response.data)
    } catch (error) {
      console.error("Error fetching data:", error);

      // Handle specific error cases if needed
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.error(
          "Server responded with status code:",
          error.response.status
        );
        console.error("Response data:", error.response.data);
      } else if (error.request) {
        // The request was made but no response was received
        console.error("No response received from the server");
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error("Error setting up the request:", error.message);
      }

      // Update state or show a user-friendly error message as needed
    }
  };


  return (
    <>
      <AdminNavbar />
      <h1
        style={{
          textAlign: "center",
          fontSize: "36px",
          fontWeight: "bold",
          marginBottom: "20px",
        }}
      >
        Punch Time 
      </h1>
      
        <FormControl>
        <div className="form_">
          {/* <FormLabel fontSize={25} mx={650} mt={10}>Filter</FormLabel> */}
          <Select
            placeholder="Choose option"
            value={selectedFilter}
            // width={400}
            // mt={5}
            // mx={650}
            style={{width:"100%"}}
            onChange={handleFilterChange}
          >
            <option value="Day">Day</option>
            <option value="Week">Week</option>
            <option value="Month">Month</option>
            <option value="Year">Year</option>
            <option value="User">User</option>
          </Select>
          {selectedFilter === "User" && (
            <>
              {/* <FormLabel>Reg No</FormLabel> */}
              <div style={{paddingTop:"20px"}}>
                <Input
                
                placeholder="Reg No"
                  type="text"
                  value={regNo}
                  onChange={(e) => setRegNo(e.target.value)}
                />
              </div>
            </>
          )}
          <Button
            style={{ marginTop: "1rem" }}
            onClick={handleFilterClick}
     
          >
            Check
          </Button>

          </div>
          {/* Display table with punch data */}
          {punchData.length > 0 && (
            <Table variant="striped" colorScheme="teal" marginTop="1rem">
              <Thead>
                <Tr>
                  <Th>Srno</Th>
                  <Th>Name</Th>
                  <Th>Reg No</Th>
                  <Th>Date</Th>
                  <Th>Time</Th>
                </Tr>
              </Thead>
              <Tbody>
                {punchData.map((punch, index) => (
                  <Tr key={index}>
                    <Td>{index + 1}</Td>
                    <Td>{punch.regno.user.name}</Td>
                    <Td>{punch.regno.register_no}</Td>
                    <Td>{formatDate(punch.time)}</Td>
                    <Td>{punch.time.split("T")[1].split(".")[0]}</Td>
                  </Tr>
                ))}
              </Tbody>
            </Table>
          )}
        </FormControl>
      
    </>
  );
}

export default Punchtime;
