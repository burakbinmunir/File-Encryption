import React from 'react';
import './App.css';
import './index.css';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

import Home from './Home';
import Encrypt from './AES';
import Decrypt from './HMAC';
import Feedback from './Feedback';
import Feedback2 from './Feedback2';
import File_Encrypt from './File_Encryption'
import File_Decrypt from './File_Decryption'

const App = () => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />}/>
        
        <Route path="/AES" element={<Encrypt />}/>

        <Route path="/HMAC" element={<Decrypt />}/>
 
        <Route path="/feedback" element={<Feedback />}/>

        <Route path='/File_Encryption' element={<File_Encrypt />}/>
        
        <Route path='/File_Decryption' element={<File_Decrypt />}/>

        <Route path="/feedback2" element={<Feedback2 />}/>
      </Routes>
    </Router>
  );
};

export default App;