import "./App.css"
import React from "react"
import ConnectBar from "./components/ConnectBar/ConnectBar"
import About from "./components/About/About"
import loadingGif from "./res/logo.gif"
import Landing from "./components/Landing/Landing.js"
import { useEffect, useState } from "react"
import Projects from "./components/Projects/Projects"
import LoadingScreen from "react-loading-screen"
import SkillIntrest from "./components/SkillIntrest/SkillIntrest"
function App() {
	const [isLoading, setIsLoading] = useState(true)
	useEffect(() => {
		setTimeout(() => {
			setIsLoading(false)
		}, 2000)
	}, [])
	
	return (
		<LoadingScreen
			loading={isLoading}
			bgColor="#410000"
			spinnerColor="#9ee5f8"
			textColor="#FFFFFF"
			logoSrc={loadingGif}
			text="Please Scroll A Bit On Loading In"
			>
			<div className="App">
				<Landing/>
				<About />
				<SkillIntrest/>
				<Projects />
				<div>
					<hr id="Connect-Hr"></hr>
				</div>
				<ConnectBar />
			</div>
		</LoadingScreen>
	)
}

export default App
