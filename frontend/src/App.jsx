import './App.css';
import { GoogleOAuthProvider } from '@react-oauth/google';
import { GoogleLogin } from '@react-oauth/google';
import jwt_decode from "jwt-decode";
import React from 'react';
function App() {
  return (

    
    <GoogleOAuthProvider clientId="530274355584-5j5lu2q3e9fpns1tec41fb8i7c15pjgl.apps.googleusercontent.com">
<GoogleLogin
  onSuccess={credentialResponse => {
    var decoded = jwt_decode(credentialResponse.credential);
    console.log(decoded);
  }}
  
  onError={() => {
    console.log('Login Failed');
  }}
/>;
    </GoogleOAuthProvider>


  );
}

export default App;
