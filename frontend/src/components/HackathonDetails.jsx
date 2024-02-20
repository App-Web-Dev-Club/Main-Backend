import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, Text, Stack, Heading, Button, CardHeader, CardBody } from '@chakra-ui/react';
import { useNavigate } from 'react-router-dom';
import Navbar from './Navbar';
export function HackathonDetails(hackathon){
    const [selectedHackathon, setSelectedHackathon] = useState(hackathon);
    const navigate = useNavigate();
    return(<>
    <Navbar/>
         <Card m={10}>
          <CardHeader>
            <Heading fontSize="xl">{selectedHackathon.name}</Heading>
          </CardHeader>
          <CardBody>
            <Heading></Heading>
            <Text fontSize="md" color="gray.500">{selectedHackathon.description}</Text>
            <Text>Conducted by: {selectedHackathon.conducting_organization}</Text>
            <Text>Registration Link: <a href={selectedHackathon.registation_link} target="_blank" rel="noopener noreferrer">{selectedHackathon.registation_link}</a></Text>
            <Text>WhatsApp Link: <a href={selectedHackathon.whatsapplink} target="_blank" rel="noopener noreferrer">{selectedHackathon.whatsapplink}</a></Text>
            <Text>GCR Code: {selectedHackathon.gcr_code}</Text>
            <Text>End Date: {new Date(selectedHackathon.end_Date).toLocaleString()}</Text>
            <Button onClick={() => navigate('/hackathon')}>Close</Button>
          </CardBody>
        </Card>
        
    </>)
} 