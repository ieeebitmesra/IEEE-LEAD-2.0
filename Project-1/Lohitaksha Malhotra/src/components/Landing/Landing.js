import React from "react"
import alertimg from "../../res/alert.png"
import headerBackground from "../../res/429540.jpg"
import { Parallax } from "react-parallax"
import Typewriter from "typewriter-effect"
import { useState } from "react"
import "./Landing.css"
function Landing(){
	const [alertRead, setAlertRead] = useState(false)
    return(
        <Parallax bgImage={headerBackground} strength={300}>
					{!alertRead && (
						<div className="idk">
							<img id="alertimg" src={alertimg} alt="!ALERT - "></img>
							This is a website built during Lead 2.0 at BIT Mesra while i am
							still learning a lot of things.
							<button
								id="x"
								onClick={() => {
									setAlertRead(true)
								}}
							>
								x
							</button>
						</div>
					)}
					<div className="App-header">
						<div className="big-text">I am Lohitaksha Malhotra.</div>
						<div className="small-text">
							I am a mechanical engineering student (1st Year) at BIT Mesra. I
							like to dabble in various parts of frontend development and like
							to learn about various technologies. I usually look into these or
							just play some games during my free time
						</div>
						<div className="notsobig-text">
						<Typewriter
							options={{
								strings: ["Programmer", "Developer", "Cool Guy" , "Learner", "Thinker"],
								autoStart: true,
								loop: true,
							}}
						/>
						</div>
						<div className="small-text" id = "yooloo">
							scroll down
						</div>
						<div className="small-text" id="arrow">
							^
						</div>
					</div>
				</Parallax>
    )
}

export default Landing