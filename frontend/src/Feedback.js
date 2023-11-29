import React from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import { options } from "./Assets/options";
import "./App.css";
import { useNavigate } from 'react-router-dom';

const Feedback = () => {

const navigate = useNavigate();

  const particlesInit = async (main) => {
    await loadFull(main);
  };

  function handleGoBackClick() {
    navigate('/');
  }

  const particlesLoaded = (container) => {};

  return (
    <div className="h-[200vh]">
      <div className="card h-screen flex flex-col items-center justify-center text-white font-sans">
       <p className="text-5xl mb-8">Congratulations! Your data is encrypted successfully</p>
       <div className="w-[31vw] bg-black/50 rounded p-8 text-justify-centre text-lg">
            We priorities the data confidentiality of our clients.
       </div>
      </div>

      <div className="info flex flex-col items-center justify-end text-white mt-24">
        
        <button className="bg-gray-800 hover:bg-green-700 mt-8 text-2xl transform transition-all duration-300 w-50 z-10 hover:scale-90 px-8 py-2 rounded-md" 
         onClick={handleGoBackClick}
        > Back to Home <br />
          <p className="text-7xl"></p>
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

export default Feedback;