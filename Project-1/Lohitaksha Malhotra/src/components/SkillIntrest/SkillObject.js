import "./Skill.css"

function Skill(props) {
	return (
		<div className="skill">
			<h1>{props.title}</h1>
			{props.children}
		</div>
	)
}
export default Skill
