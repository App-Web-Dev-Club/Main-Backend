import React from 'react';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
// import { jwtDecode } from 'jwt-decode';

function App() {
  const handleGoogleLogin = async (credentialResponse) => {
    try {
      // Extract the Google access token from the response
      const googleAccessToken = credentialResponse.credential.accessToken;

      // Send the Google access token to the backend
      const response = await fetch('http://your-backend-url/auth/google/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ access_token: googleAccessToken }),
      });

      if (response.ok) {
        const data = await response.json();
        // Assuming your backend returns a JWT token, you can decode and log it
        const decodedToken = jwtDecode(data.access);
        console.log('Decoded Token:', decodedToken);
      } else {
        console.error('Failed to authenticate with the backend');
      }
    } catch (error) {
      console.error('Error during Google login:', error);
    }
  };

  return (
    <GoogleOAuthProvider clientId="530274355584-5j5lu2q3e9fpns1tec41fb8i7c15pjgl.apps.googleusercontent.com">
      <GoogleLogin
        onSuccess={handleGoogleLogin}
        onError={() => {
          console.log('Login Failed');
        }}
      />
    </GoogleOAuthProvider>
  );
}

export default App;
