import React, { useEffect , useState } from 'react'
import { Container, Row, Col, Jumbotron, Button} from 'react-bootstrap'
function Landing() {
    const [location, setLocation] = useState("Enable Location")
    const [data, setData] = useState([])
    const [worldData, setWorldData]= useState([])

    // Get Location Data
    useEffect(()=>{
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                // Get the coordinates of the current position.
                var lat = position.coords.latitude;
                var lng = position.coords.longitude;
                // console.log("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ lng + "," + lat + ".json?&access_token=pk.eyJ1IjoibG9oaXQyNDQiLCJhIjoiY2twNWZoZ3MzMHU4YjJ4cjJkcWhvZWZvNiJ9.qrQoAp1hwFBvf98GYdvh1Q")
                fetch("https://api.mapbox.com/geocoding/v5/mapbox.places/"+ lng + "," + lat + ".json?&access_token=pk.eyJ1IjoibG9oaXQyNDQiLCJhIjoiY2twNWZoZ3MzMHU4YjJ4cjJkcWhvZWZvNiJ9.qrQoAp1hwFBvf98GYdvh1Q")
                .then(res => res.json())
                .then(
                                (result) => {
                                    var countryIndex = 0;
                                    for(var i = 0;i<result.features.length;i++){
                                        if(result.features[i].id.includes("country")){
                                            countryIndex = i;
                                        }
                                    }
                                    var TempName = result.features[countryIndex].place_name
                                    if (TempName==="United Kingdom"){
                                        TempName = "UK";
                                    }
                                    if (TempName==="United Arab Emirates"){
                                        TempName = "UAE";
                                    }
                                    if (TempName==="Democratic Republic of Congo"){
                                        TempName = "DRC";
                                    }
                                    setLocation(TempName);
                                },
                    )
                fetch("https://coronavirus-19-api.herokuapp.com/countries/" + location)
                .then(res=> res.json())
                .then(
                    (result)=>{
                        setData(result)
                    }
                )
            });
            
        }
        else {
            console.log("No Location")
        }
    
    },[location])

    // Get World Data
    useEffect(()=>{
        fetch("https://coronavirus-19-api.herokuapp.com/all")
        .then(res =>res.json())
        .then(
            (result)=>{
                setWorldData(result)
            }
        )
    },[])
    return (
        <Jumbotron id="home" className="d-flex flex-column align-items-center">
        <Container className="text-center" >
            <Row>
                <Col md={6}>
                    <h1> {location}</h1>
                    <h6>Total : {data.cases}</h6>
                    <h6> Active: {data.active}</h6>
                    <h6> New Cases: {data.todayCases}</h6>
                    <h6> Deaths: {data.deaths}</h6>
                    <h6> Critical: {data.critical}</h6>
                    <h6> Recovered : {data.recovered}</h6>
                    </Col>
                <Col md={6}>
                    <h1>Global</h1>
                    <h6>Cases : {worldData.cases}</h6>
                    <h6> Deaths: {worldData.deaths}</h6>
                    <h6> Recovered: {worldData.recovered}</h6>
                </Col>
            </Row>
        </Container>
        <Button className="LearnButton" variant="outline-primary" size="lg" onClick={()=>{
            window.open("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public")
        }}>Learn more</Button>
        </Jumbotron>
    )
}
export default Landing