import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Box,
  Image,
  Text,
  VStack,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalCloseButton,
  ModalBody,
  ModalFooter,
  Button,
  Flex,
} from "@chakra-ui/react";
import Navbar from '../components/Navbar';


const Hackathon = () => {
  const [hackathons, setHackathons] = useState([]);
  const [selectedHackathon, setSelectedHackathon] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    const fetchHackathons = async () => {
      try {
        const response = await axios.get('http://localhost:8000/kids/hackathon');
        setHackathons(response.data);
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching hackathons:', error);
      }
    };

    fetchHackathons();
  }, []);

  const openModal = (hackathon) => {
    setSelectedHackathon(hackathon);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setSelectedHackathon(null);
    setIsModalOpen(false);
  };

  const handleRegister = () => {
    if (selectedHackathon && selectedHackathon.registation_link) {
      window.open(selectedHackathon.registation_link, '_blank');
    } else {
      console.error('No registration link available');
    }
  };
  

  return (
    <>
      <Navbar />
      <Flex justifyContent="flex-start" p={4}>
      
      {hackathons.map((hackathon) => (
        <Box
          key={hackathon.id}
          maxW="sm"
          borderWidth="1px"
          borderRadius="lg"
          overflow="hidden"
          cursor="pointer"
          onClick={() => openModal(hackathon)}
          mx={4} // Add margin between cards
          mb={4} // Add margin below cards
        >
          <Image
            src={`http://localhost:8000/${hackathon.banner}`}
            
            alt="Hackathon Banner"
          />
          <Box p="6">
            <Text fontWeight="bold" fontSize="xl">
              {hackathon.name}
            </Text>
            <Text>{hackathon.description}</Text>
          </Box>
        </Box>
      ))}
      <Modal isOpen={isModalOpen} onClose={closeModal}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>{selectedHackathon?.name}</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Text>{selectedHackathon?.description}</Text>
            <Text>Conducting Organization: {selectedHackathon?.conducting_organization}</Text>
            <Text>Registration Date: {new Date(selectedHackathon?.registation_date).toLocaleString()}</Text>
            <Text>Website Link: <a href={selectedHackathon?.website_link} target="_blank" rel="noopener noreferrer">{selectedHackathon?.website_link}</a></Text>
            <Text>WhatsApp Link: <a href={selectedHackathon?.whatsapplink} target="_blank" rel="noopener noreferrer">{selectedHackathon?.whatsapplink}</a></Text>
            <Text>GCR Code: {selectedHackathon?.gcr_code}</Text>
            <Text>End Date: {new Date(selectedHackathon?.end_Date).toLocaleString()}</Text>
            <Text>Active: {selectedHackathon?.active ? "Yes" : "No"}</Text>
          </ModalBody>
          <ModalFooter>
            <Button colorScheme="blue" mr={3} onClick={handleRegister}>
              Register
            </Button>
            {/* <Button variant="ghost" onClick={closeModal}>Close</Button> */}
          </ModalFooter>
        </ModalContent>
      </Modal>
      </Flex>
    </>
    
  );
};

export default Hackathon;
