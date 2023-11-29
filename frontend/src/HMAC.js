import React, { useState } from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import { options } from "./Assets/options";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
const Decrypt = () => {
  const particlesInit = async (main) => {
    await loadFull(main);
  };

  const particlesLoaded = (container) => {};

  const [methodDropdownOpen, setMethodDropdownOpen] = useState(false);
  const [keySizeDropdownOpen, setKeySizeDropdownOpen] = useState(false);
  const [plainText, setPlainText] = useState(""); // plain text
  const [hmac , setHmac] = useState(""); // encrypted text
  const [key, setKey] = useState("");
  const [hmacText, setHmacText] = useState(""); // encrypted text

  const handleMethodClick = (method) => {
    setSelectedMethod(method);
    setMethodDropdownOpen(false);
  };

  const handleKeySizeClick = (keySize) => {
    setSelectedKeySize(keySize);
    setKeySizeDropdownOpen(false);
  }

  const navigate = useNavigate();

  function handleHMACClick() {
    navigate('/');
  } 

  async function perform_hmac() {
    if (plainText && key){
     

      await axios.post('http://localhost:5000/hmac', {
        message: plainText,
        key: key,
      })
      .then((response) => {
        setHmacText(response.data.hashed_mac);
        navigator.clipboard.writeText(response.data.hashed_mac);
      }, (error) => {
        console.log(error);
      });
    }
    else {
      alert("Please select all the fields!");
    }   
  }

  function handleFeedback() {
    navigate('/feedback2');
  }

  return (
    <div className="relative font-mono text-white text-opacity-70 font-[700] text-opacity-90 h-screen flex items-center bg-black">
        
      <div className="w-[80%] h-[90%] flex flex-row z-10">

        <div className="bg-opacity-30 h-full w-[120%] pl-0 ">
          <div className="pl-[2%] flex flex-row justify-between">
            <div className="flex flex-col">
              <textarea
                type="text"
                placeholder="Enter text"
                className="w-[32vw] h-[62vh] overflow-wrap-break-word flex flex-wrap w-110 ml-12 border border-black bg-gray-700 opacity-200 p-2 rounded-md text-black bg-white bg-opacity-70 m-5 justify-start"
                onChange={(e)=>{ setPlainText(e.target.value)}}
                value={plainText}
              />
              <textarea
                type="text"
                placeholder="Enter text"
                className="w-[32vw] h-[16vh] overflow-wrap-break-word w-110 ml-12 border border-black bg-gray-700 opacity-200 p-2 rounded-md text-black bg-white bg-opacity-70 m-5 justify-start"
                onChange={(e)=>{ setKey(e.target.value)}}
              />

              <button onClick={()=> perform_hmac()} className="bg-gray-800 hover:bg-green-700 text-white py-1 px-1 ml-16 mr-14 w-15 rounded-md">
                Generate Hash MAC <br />
                <p className="text-7xl"></p>
              </button>
            </div>

            <div className="w-[30vw] h-[82vh] flex flex-col p-3 rounded-md text-black bg-opacity-70 m-5 p-8 justify-center items-center">
            </div>

            <div className="flex flex-col">
              <textarea
               type="text"
               placeholder="Get Hashed Mac"
               className="w-[32vw] h-[82vh] border border-black bg-gray-700 opacity-200 p-3 rounded-md text-black bg-white bg-opacity-70 m-5 justify-end"
               value={hmacText} 
              />
              <button className="bg-gray-800 hover:bg-green-700 text-white py-1 px-1 ml-16 mr-14 w-15 rounded-md"
               onClick={handleFeedback}
               > Get Text <br />
                <p className="text-7xl"></p>
              </button>
            </div>
            <button className="bg-gray-800 hover:bg-green-700 mt-0 text-1xl transform transition-all duration-300 w-30 h-10 z-10 hover:scale-90 px-8 py-2 rounded-md" 
              onClick={()=> navigate('/')}
              > Home <br/>
            <p className="text-7xl"></p>
            </button>
          </div>
        </div>
      </div>

      <Particles
        className="z-0 absolute top-0 left-0 w-full h-full"
        init={particlesInit}
        loaded={particlesLoaded}
        options={options}
      />
    </div>
  );
};

export default Decrypt;
