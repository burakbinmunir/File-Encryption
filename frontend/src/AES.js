import React, { useState } from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import { options } from "./Assets/options";
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Document, Page, pdfjs} from 'react-pdf';

const Encrypt = () => {
  const particlesInit = async (main) => {
    await loadFull(main);
  };

  const particlesLoaded = (container) => {};
  const navigate = useNavigate();
  const [selectedMethod, setSelectedMethod] = useState("Select Method");
  const [selectedKeySize, setSelectedKeySize] = useState("Select Key Size");
  const [methodDropdownOpen, setMethodDropdownOpen] = useState(false);
  const [keySizeDropdownOpen, setKeySizeDropdownOpen] = useState(false);
  const [plainText, setPlainText] = useState(""); // plain text
  const [encryptedText, setEncryptedText] = useState(""); // encrypted text
  const [key, setKey] = useState(""); 

  const handleMethodClick = (method) => {
    setSelectedMethod(method);
    setMethodDropdownOpen(false);
  };

  const handleKeySizeClick = (keySize) => {
    setSelectedKeySize(keySize);
    setKeySizeDropdownOpen(false);
  }

  async function perform_encryption() {
    var key_size = 0;
    
    if (selectedKeySize && plainText && key){

      if (selectedKeySize === "128bits") {
        key_size = 128;
        // if (key.length !== 16) {
        //   alert("Key size does not match!");
        //   return;
        // }

      }
      else if (selectedKeySize === "192bits") {
        key_size = 192;
        // if (key.length !== 24) {
        //   alert("Key size does not match!");
        //   return;
        // }
      }
      else if (selectedKeySize === "256bits") {
        key_size = 256;
        // if (key.length !== 32) {
        //   alert("Key size does not match!");
        //   return;
        // }
      }
      console.log(key_size, plainText, key);
      
      await axios.post('http://localhost:5000/encrypt', {
        plain_text: plainText,
        block_size:key_size,
        key: key,
      })
      .then((response) => {
        setEncryptedText(response.data.encrypted_data);
        navigator.clipboard.writeText(response.data.encrypted_data);  
      }, (error) => {
        console.log(error);
      });
    }
    else {
      alert("Please select all the fields!");
    }   
  }

  async function perform_hmac() {
    if (selectedMethod && selectedKeySize && plainText){
      await axios.post('http://localhost:5000/hmac', {
        message: plainText,
        key: key,
      })
      .then((response) => {
        setEncryptedText(response.data.hashed_mac);
      }, (error) => {
        console.log(error);
      });
    }
    else {
      alert("Please select all the fields!");
    }   
  }

  async function handleEncryptClick() {
      perform_encryption();
  }

  async function handleDecryptClick() {
    if (selectedKeySize && encryptedText && key){
      var key_size = 0;
      if (selectedKeySize === "128bits") {
        key_size = 128;
        // if (key.length !== 16) {
        //   alert("Key size does not match!");
        //   return;
        // }
      }
      else if (selectedKeySize === "192bits") {
        key_size = 192;
        // if (key.length !== 24) {
        //   alert("Key size does not match!");
        //   return;
        // }
      }
      else if (selectedKeySize === "256bits") {
        key_size = 256;
        // if (key.length !== 32) {
        //   alert("Key size does not match!");
        //   return;
        // }
      }
      await axios.post('http://localhost:5000/decrypt', {
        encrypted_data: encryptedText,
        block_size:key_size,
        key: key,
      })
      .then((response) => {
        setPlainText(response.data.decrypted_data);
        navigator.clipboard.writeText(response.data.decrypted_data);
      }, (error) => {
        console.log(error);
      });
    }
    else {
      alert("Please select all the fields!");
    }
  }


  function handleFeedback() {
    navigate('/feedback');
  }

  const [numPages, setNumPages] = useState(null);
  const [pdfText, setPdfText] = useState('');

  const readPDF = async (file) => {
    const reader = new FileReader();

    reader.onload = async () => {
      const buffer = reader.result;
      const typedArray = new Uint8Array(buffer);
      const pdfData = typedArray.buffer;

      var temp_text = ''

      // Load the PDF using react-pdf
      pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

      try {
        const pdf = await pdfjs.getDocument({ data: pdfData }).promise;
        const pages = [];

        for (let i = 1; i <= pdf.numPages; i++) {
          const page = await pdf.getPage(i);
          const textContent = await page.getTextContent();
          const pageText = textContent.items.map((item) => item.str).join(' ');
          temp_text = temp_text + pageText;
          
        }
        
        setPdfText(pages.join('\n'));
        setNumPages(pdf.numPages);
      } catch (error) {
        console.error('Error while extracting text:', error);
      }
      console.log(temp_text)
      setPlainText(temp_text);
    };

    reader.readAsArrayBuffer(file);
  };

  const onFileChange = (event) => {
    const file = event.target.files[0];
    if (file.type === 'application/pdf') {
      readPDF(file);
    }

  };
  
  pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

  return (
    <div className="relative font-mono text-white text-opacity-70 font-[700] text-opacity-90 h-screen flex items-center bg-black">
      <div className="w-[80%] h-[90%] flex flex-row z-10">
      
        <div className="bg-opacity-30 h-full w-[120%] pl-0 ">
          <div className="pl-[2%] flex flex-row justify-between">
            <div className="flex flex-col flex-wrap wrap" style={{ wordWrap: 'break-word' }}>
            <input type="file" onChange={(e)=>onFileChange(e)} />

              <textarea
                type="text"
                placeholder="Enter plain text"
                className="w-[32vw] h-[62vh] w-110 ml-12 border border-black bg-gray-700 opacity-200 p-2 rounded-md text-black bg-white bg-opacity-70 m-5 justify-start"
                onChange={(e)=>{ setPlainText(e.target.value)}}
                value={plainText}
                style={{ resize: 'none', overflowWrap: 'break-word' }}
              />
              <textarea
                type="text"
                placeholder="Enter Key"
                className="w-[32vw] h-[16vh] overflow-wrap-break-word w-110 ml-12 border border-black bg-gray-700 opacity-200 p-2 rounded-md text-black bg-white bg-opacity-70 m-5 justify-start"
                onChange={(e)=>{ setKey(e.target.value)}}
              />
              <button onClick={()=>handleEncryptClick()} className="bg-gray-800 hover:bg-green-700 text-white py-1 px-1 ml-16 mr-14 w-15 rounded-md">
                Encrypt Text <br />
                <p className="text-7xl"></p>
              </button>
            </div>

            <div className="w-[30vw] h-[82vh] flex flex-col p-3 rounded-md text-black bg-opacity-70 m-5 p-8 justify-center items-center">

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

            <div className="flex flex-col" style={{ wordWrap: 'break-word' }}>
            
            <textarea
              type="text"
              placeholder="Get encrypted text"
              className="w-[32vw] h-[82vh] border border-black bg-gray-700 opacity-200 p-3 rounded-md text-black bg-white bg-opacity-70 m-5 justify-end"
              value={encryptedText}
              style={{ wordWrap: 'break-word' }}
               />

              <button className="bg-gray-800 hover:bg-green-700 text-white py-1 px-1 ml-16 mr-14 w-15 rounded-md"
               onClick={handleDecryptClick}
               > Decrypt Text <br />
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

export default Encrypt;
