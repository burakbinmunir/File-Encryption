import React from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import { options } from "./Assets/options";
import './App.css';
import './index.css';

import { useNavigate } from 'react-router-dom';

const Home = () => {

  const navigate = useNavigate();

  const particlesInit = async (main) => {
    await loadFull(main);
  };
 
  function handleEncryptClick() {
    navigate('/AES');
  }

  function handleHMACClick() {
    navigate('/HMAC');
  }

  function handleFileEncryptClick (){
    navigate('/File_Encryption')
  }

  function handleFileDecryptClick (){
    navigate('/File_Decryption')
  }

  const particlesLoaded = (container) => {};
  
  return (
    <div className="h-[200vh]">
      <div className="card h-screen flex flex-col items-start justify-end pl-20 pb-8 text-white">
        <p className="text-7xl font-medium p-0 mb-8">Welcome to Safety Hub </p>
        
      </div>
      <div>
        
      </div>
      <div className="info flex flex-col items-center justify-end text-white mt-24">
        <p className="text-3xl">Secure your data with us!</p>
        
        <button className="bg-gray-800 hover:bg-green-700 mt-10 text-2xl transform transition-all duration-300 w-50 z-10 hover:scale-90 px-8 py-2 rounded-md" 
        onClick={handleEncryptClick}
        > Text Encryption <br/>
          <p className="text-7xl"></p>
        </button>

        <button className="bg-gray-800 hover:bg-green-700 mt-10 text-2xl transform transition-all duration-300 w-50 z-10 hover:scale-90 px-8 py-2 rounded-md" 
        onClick={handleFileEncryptClick}
        > File Encryption <br/>
          <p className="text-7xl"></p>
        </button>

        <button className="bg-gray-800 hover:bg-green-700 mt-10 text-2xl transform transition-all duration-300 w-50 z-10 hover:scale-90 px-8 py-2 rounded-md" 
                onClick={handleFileDecryptClick}
                > File Decryption <br/>
            <p className="text-7xl"></p>
        </button>

        <button className="bg-gray-800 hover:bg-green-700 mt-8 text-2xl transform transition-all duration-300 w-50 z-10 hover:scale-90 px-8 py-2 rounded-md" 
        onClick={handleHMACClick}
        > Generate HMAC <br/>
          <p className="text-7xl"></p>
        </button>

        <button className="w-[50vw] h-[40vh] bg-green-1000 hover:bg-gray-700 mt-14 text-2xl transform transition-all duration-300 z-10 hover:scale-90 px-8 py-2 rounded-md">
         We use AES and HMAC algorithms to convert the plain text to an encrypted text format. The same algorithms are used to converrt the already decrypted files back to the plain text.
        </button>        
      </div>

      <Particles
        init={particlesInit}
        loaded={particlesLoaded}
        options={options}
      />
    </div>
  );
};

export default Home;