import React, { useState } from 'react';
import { Box, Input, Button, Text, Spinner } from '@chakra-ui/react';
import CalendarHeatmap from 'react-calendar-heatmap';
import 'react-calendar-heatmap/dist/styles.css';
import axios from 'axios';

function GraphAttendance() {
  const [registerNo, setRegisterNo] = useState('');
  const [attendanceData, setAttendanceData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

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

  return (
    <Box p={4}>
      <Input
        placeholder="Enter Register No."
        value={registerNo}
        onChange={handleInputChange}
        mb={4}
      />
      <Button onClick={handleSubmit} colorScheme="teal" mb={4}>Submit</Button>
      
      {loading && <Spinner color="teal" />}
      {error && <Text color="red.500">{error}</Text>}
      
      {attendanceData.length > 0 && (
        <Box mt={8}>
          <CalendarHeatmap
            startDate={new Date('2024-01-01')}
            endDate={new Date('2024-12-31')}
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
          />
        </Box>
      )}
      
      {attendanceData.length === 0 && !loading && !error && (
        <Text>No attendance data available.</Text>
      )}
    </Box>
  );
}

export default GraphAttendance;