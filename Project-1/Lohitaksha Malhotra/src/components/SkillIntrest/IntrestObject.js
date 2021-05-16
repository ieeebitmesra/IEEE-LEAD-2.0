import "./Intrest.css"

function IntrestObject(props) {
	return (
		<div className="topic">
			<h1>{props.title}</h1>
			{props.children}
		</div>
	)
}
export default IntrestObject