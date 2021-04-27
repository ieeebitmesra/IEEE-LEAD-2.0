import React from "react"
import footer from "../../res/footer.jpg"
import { Parallax } from "react-parallax"
import Skill from "./SkillObject"
import "./SkillIntrest.css"
import IntrestObject from "./IntrestObject"
function SkillIntrest() {
	return (
		<Parallax bgImage={footer} strength={500}>
			<div className="intrests">
				<div className="about-header">
					<h1 id="skillHeading">My Skills</h1>I am very new so i dont have many
					but i'll keep improving
				</div>
				<div className="skills-container">
					<Skill title="Python">
						I now basic python and am working my way to learning data science
						methods.
					</Skill>
					<Skill title="ReactJS">
						This entire project is built on react.. but ofcourse i am still
						figuring my way with react too and am still but a newbie.
					</Skill>
					<Skill title="HTML and CSS">
						By no means exceptional at these and especially CSS, but i can deal
						with these languages to an extent.
					</Skill>
					<Skill title="Photoshop">
						I have been using photoshop for quite some time and can do a good
						bit with it
					</Skill>
				</div>
			</div>
			<div className="intrests">
				<div className="about-header">
					<h1 id="intrestHeading">My Intrests</h1>
					in case you wanna know more about me
				</div>
				<div className="intrests-container">
					<IntrestObject title="Programming">
						I am still learning but ofcourse I do like programming.
					</IntrestObject>
					<IntrestObject title="Anime & Manga">Yes, i am a weeb.</IntrestObject>
					<IntrestObject title="Gaming">
						I dont have a good gaming grade laptop but i do still play games
						like Valorant and CS:GO.
					</IntrestObject>
				</div>
			</div>
		</Parallax>
	)
}

export default SkillIntrest
