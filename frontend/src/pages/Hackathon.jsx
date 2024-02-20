import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, Text, Stack, Heading, Button, CardHeader, CardBody } from '@chakra-ui/react';
import { useNavigate } from "react-router-dom";
import Navbar from '../components/Navbar';

function Hackathon() {
  const [data, setData] = useState([]);
  const [selectedHackathon, setSelectedHackathon] = useState(null);
  const navigate = useNavigate();



  useEffect(() => {
    axios.get('http://localhost:8000/kids/hackathon')
      .then((res) => {
        setData(res.data);
        console.log(res.data);
      })
      .catch((error) => {
        console.error('Error fetching hackathon data:', error);
      });
  }, []);

  const handleCardClick = (hackathon) => {
    setSelectedHackathon(hackathon);
  };

  return (
    <>
    <Navbar/>
    <Stack spacing={4} >
      {data.map((hackathon) => (
        <Card key={hackathon.id} m={10} onClick={() => handleCardClick(navigate('details',{hackathon}))}>
          <CardHeader>
            <Heading fontSize="xl">{hackathon.name}</Heading>
          </CardHeader>
          <CardBody>
            <Text fontSize="md" color="gray.500">{hackathon.shot_description}</Text>
          </CardBody>
        </Card>
      ))}
      {selectedHackathon && (
        <Card m={10}>
          <CardHeader>
            <Heading fontSize="xl">{selectedHackathon.name}</Heading>
          </CardHeader>
          <CardBody>
            <Text fontSize="md" color="gray.500">{selectedHackathon.description}</Text>
            <Text>Conducted by: {selectedHackathon.conducting_organization}</Text>
            <Text>Registration Link: <a href={selectedHackathon.registation_link} target="_blank" rel="noopener noreferrer">{selectedHackathon.registation_link}</a></Text>
            <Text>WhatsApp Link: <a href={selectedHackathon.whatsapplink} target="_blank" rel="noopener noreferrer">{selectedHackathon.whatsapplink}</a></Text>
            <Text>GCR Code: {selectedHackathon.gcr_code}</Text>
            <Text>End Date: {new Date(selectedHackathon.end_Date).toLocaleString()}</Text>
            <Button onClick={() => setSelectedHackathon(null)}>Close</Button>
          </CardBody>
        </Card>
      )}
    </Stack>
    </>
  );
}

export default Hackathon;
