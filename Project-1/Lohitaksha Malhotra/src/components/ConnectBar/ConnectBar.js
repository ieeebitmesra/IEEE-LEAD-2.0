import "./ConnectBar.css"
import linkedin from "../../res/linkedin.png"
import instagram from "../../res/instagram.png"
import github from "../../res/github.png"
import steam from "../../res/steam.png"
import background2 from "../../res/background3.jpg"
import {Parallax} from "react-parallax"
function ConnectBar() {
	return (
		<Parallax bgImage ={background2} strength = {300}>
			<div id="container-connect">
				
				<div className="ConnectBar">
					<u>Say Hello</u>
					<div className = "textalign" id = "texthello">
					Have a new project in mind? Let's collaborate and build something awesome. Let's turn that idea to an even greater product :)
					</div>
					<div className = "textalign">
					
					<div className="Connect-Item">
						<a href="https://www.instagram.com/lohitakshamalhotra/">
							<img
								className="Connect-Image"
								src={instagram}
								alt="Instagram"
							></img>
						</a>
					</div>
					<div className="Connect-Item">
						<a href="https://www.linkedin.com/in/lohitaksha-malhotra-b84392201/">
							<img
								className="Connect-Image"
								src={linkedin}
								alt="LinkedIn"
							></img>
						</a>
					</div>
					<div className="Connect-Item">
						<a href="https://github.com/Lohit244">
							<img className="Connect-Image" src={github} alt="Github"></img>
						</a>
					</div>
					<div className="Connect-Item">
						<a href="https://steamcommunity.com/profiles/76561198292046668/">
							<img className="Connect-Image" src={steam} alt="Steam"></img>
						</a>
					</div>
				</div>
				<a id = "connect-link" href = "mailto:lohit244@gmail.com" alt = "lohit244@gmail.com"><button id = "connect-button">LET'S TALK</button></a>
				
				</div>
			</div>
			
		</Parallax>
	)
}

export default ConnectBar
