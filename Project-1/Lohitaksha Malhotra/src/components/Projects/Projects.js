import "./Projects.css"
import { Parallax } from "react-parallax"
import projectsBackground from "../../res/48078.jpg"
function Projects(){
    return(
        <div className = "projects-root">
        <div className = "projects-header">
            <h1>My Projects</h1>
        </div>
        <Parallax bgImage = {projectsBackground} strength = {300}>
        <div className = "projects-container">
            <p className = "small-text">*These are just random placeholder images and text instead of project links because i don't have any projects, you get the idea</p>
            <div className = "gallery">
                <div className = "gallery-item" id = "img1"><a href = "https://github.com/Lohit244/4/tree/master">Portfolio</a></div>
                <div className = "gallery-item" id = "img2">Image2</div>
                <div className = "gallery-item" id = "img3">Image3</div>
                <div className = "gallery-item" id = "img4">Image4</div>
            </div>
            <div className = "gallery">
                <div className = "gallery-item" id = "img5">Image5</div>
                <div className = "gallery-item" id = "img6">Image6</div>
                <div className = "gallery-item" id = "img7">Image7</div>
                <div className = "gallery-item" id = "img8">Image8</div>
            </div>
        </div>
        </Parallax>
        </div>
    )
}

export default Projects;