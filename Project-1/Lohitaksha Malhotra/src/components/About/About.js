import React from "react"
import "./About.css"
import myphoto from "../../res/about.png"
import { Parallax } from "react-parallax"
import boom from "../../res/boom.png"
function About() {
	const boomPhoto = precentage => (
		<div 
		  style={{
			position: 'absolute',
			width: '100px',
			height: '100px',
			borderRadius: '50%',
			backgroundImage: `url(${boom})`,
			backgroundRepeat: 'no-repeat',
			backgroundSize:`cover`,
			left: '50%',
			top: '50%',
			transform: `translate(-50%, -50%) scale(${precentage * 7})`,
		  }}
		>
		</div>
	  )
	return (
		<div className="about-container">
			<div className="about">
				<Parallax 
				renderLayer={boomPhoto}>
			<div className = "photo-block">
					<img id="my-img" src={myphoto} alt="something went wrong"></img>
					<div className = "photo-text">Lohitaksha Malhotra</div>
					<hr id="hr2"></hr>
				</div>
		</Parallax>
				
				<div className = "small-text">
					<h1 className = "big-text">My Education</h1>
					10<sup>th</sup>- CBSE Board
					<br />
					12<sup>th</sup> - PCM - CBSE Board - 87.2%
					<br />
					Mechanical Engineering - BIT Mesra (Currently Persuing)
				</div>
			</div>
			
		</div>
	)
}

export default About
