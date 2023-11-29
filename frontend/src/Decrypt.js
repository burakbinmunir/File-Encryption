import React, { useState } from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import { options } from "./Assets/options";
import { useNavigate } from 'react-router-dom';

const Decrypt = () => {
  const particlesInit = async (main) => {
    await loadFull(main);
  };

  const particlesLoaded = (container) => {};

  const [selectedMethod, setSelectedMethod] = useState("Select Method");
  const [selectedKeySize, setSelectedKeySize] = useState("Select Key Size");
  const [methodDropdownOpen, setMethodDropdownOpen] = useState(false);
  const [keySizeDropdownOpen, setKeySizeDropdownOpen] = useState(false);

  const handleMethodClick = (method) => {
    setSelectedMethod(method);
    setMethodDropdownOpen(false);
  };

  const handleKeySizeClick = (keySize) => {
    setSelectedKeySize(keySize);
    setKeySizeDropdownOpen(false);
  }

  const navigate = useNavigate();

  function handleEncryptClick() {
    navigate('/');
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
              <input
                type="text"
                placeholder="Enter encrypted text"
                className="w-[32vw] h-[82vh] overflow-wrap-break-word w-110 ml-12 border border-black bg-gray-700 opacity-200 p-2 rounded-md text-black bg-white bg-opacity-70 m-5 justify-start"
              />
              <button className="bg-gray-800 hover:bg-green-700 text-white py-1 px-1 ml-16 mr-14 w-15 rounded-md">
                Decrypt Text <br />
                <p className="text-7xl"></p>
              </button>
            </div>

            <div className="w-[30vw] h-[82vh] flex flex-col p-3 rounded-md text-black bg-opacity-70 m-5 p-8 justify-center items-center">
              
              <p className="justify-center text-white font-sans text-1xl mb-20">Select your preference!</p>
              <div className="relative">
                <button
                  onClick={() => setMethodDropdownOpen(!methodDropdownOpen)}
                  className="bg-gray-700 hover:bg-green-800 text-white font-bold py-2 px-4 mb-20 rounded-md relative"
                >
                  {selectedMethod}
                  {methodDropdownOpen && (
                    <div className="origin-bottom-left absolute left-0 mt-2 w-32 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5">
                      <div
                        className="py-1"
                        role="menu"
                        aria-orientation="vertical"
                        aria-labelledby="method-options-menu"
                      >
                        <button
                          onClick={() => handleMethodClick("AES")}
                          className="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          role="menuitem"
                        >
                          AES
                        </button>
                        <button
                          onClick={() => handleMethodClick("HMAC")}
                          className="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          role="menuitem"
                        >
                          HMAC
                        </button>
                      </div>
                    </div>
                  )}
                </button>
              </div>

              <div className="relative mt-12">
                <button
                  onClick={() => setKeySizeDropdownOpen(!keySizeDropdownOpen)}
                  className="bg-gray-700 hover:bg-green-800 text-white font-bold py-2 px-4 rounded-md relative"
                >
                  {selectedKeySize}
                  {keySizeDropdownOpen && (
                    <div className="origin-bottom-left absolute left-0 mt-2 w-32 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5">
                      <div
                        className="py-1"
                        role="menu"
                        aria-orientation="vertical"
                        aria-labelledby="key-size-options-menu"
                      >
                        <button
                          onClick={() => handleKeySizeClick("128bits")}
                          className="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          role="menuitem"
                        >
                          128 bits
                        </button>
                        <button
                          onClick={() => handleKeySizeClick("192bits")}
                          className="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          role="menuitem"
                        >
                          192 bits
                        </button>
                        <button
                          onClick={() => handleKeySizeClick("256bits")}
                          className="block w-full px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
                          role="menuitem"
                        >
                          256 bits
                        </button>
                      </div>
                    </div>
                  )}
                </button>
              </div>
            </div>

            <div className="flex flex-col">
              <input
               type="text"
               placeholder="Get decrypted text"
               className="w-[32vw] h-[82vh] border border-black bg-gray-700 opacity-200 p-3 rounded-md text-black bg-white bg-opacity-70 m-5 justify-end"
              />
              <button className="bg-gray-800 hover:bg-green-700 text-white py-1 px-1 ml-16 mr-14 w-15 rounded-md"
               onClick={handleFeedback}
               > Get Text <br />
                <p className="text-7xl"></p>
              </button>
            </div>
            <button className="bg-gray-800 hover:bg-green-700 mt-0 text-1xl transform transition-all duration-300 w-30 h-10 z-10 hover:scale-90 px-8 py-2 rounded-md" 
              onClick={handleEncryptClick}
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
