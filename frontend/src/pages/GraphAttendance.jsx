import React, { useState } from 'react';
import { Box, Input, Button, Text, Spinner } from '@chakra-ui/react';
// import CalendarHeatmap from 'react-calendar-heatmap';
// import 'react-calendar-heatmap/dist/styles.css';
import axios from 'axios';

import AdminNavbar from "../components/AdminNavbar";


function GraphAttendance() {
  const [registerNo, setRegisterNo] = useState('');
  const [attendanceData, setAttendanceData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const currentYear = new Date().getFullYear();

  const fetchAttendanceData = async () => {
    setLoading(true);
    setError('');

    try {
      const response = await axios.get(`http://localhost:8000/kids/routers/attendance/?filter=${registerNo}`);
      setAttendanceData(response.data);
    } catch (error) {
      setError('Error fetching attendance data. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (event) => {
    setRegisterNo(event.target.value);
  };

  const handleSubmit = () => {
    if (registerNo.trim() !== '') {
      fetchAttendanceData();
    } else {
      setError('Please enter a valid Register No.');
    }
  };

  const getTitleForValue = (value) => {
    if (!value) return null;
    console.log(value)

    const formattedDate = value.date.toLocaleDateString('en-US', {
      day: 'numeric',
      month: 'short',
    });

    // return `${formattedDate}: ${value.count} project(s)`;
    return `${formattedDate}`;

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
        Graph View of Attendance
      </h1>
    <Box p={4} >
      <div className='form_'>
        
        <Input
          placeholder="Enter Register No."
          value={registerNo}
          onChange={handleInputChange}
          mb={4}
        />
        <Button onClick={handleSubmit} colorScheme="teal" mb={4}>Submit</Button>
        
        {loading && <Spinner color="teal" />}
        {error && <Text color="red.500">{error}</Text>}
      </div>
      
      {attendanceData.length > 0 && (
        <Box mt={8}>
          <CalendarHeatmap
            startDate={new Date(`${currentYear}-01-01`)}
            endDate={new Date(`${currentYear}-12-31`)}
            values={attendanceData.map(item => ({
              date: new Date(item.date_time.substring(0, 10)),
              count: 1
            }))}
            showWeekdayLabels={true}
            horizontal={true}
            classForValue={(value) => {
              if (!value) {
                return 'color-empty';
              }
              return 'color-filled';
            }}
            titleForValue={getTitleForValue}
            
            
          />
        </Box>
      )}
      
      <div className='form_'>
        {attendanceData.length === 0 && !loading && !error && (
          <Text>No attendance data available.</Text>
        )}
      </div>
    </Box>
    </>
    
  );
}

export default GraphAttendance;
