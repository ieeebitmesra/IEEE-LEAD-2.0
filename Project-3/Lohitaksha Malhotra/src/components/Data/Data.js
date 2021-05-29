import React, { useEffect, useState } from 'react'
import { Table, Accordion, Card } from 'react-bootstrap';
function Data(props) {
      const [isLoaded, setIsLoaded] = useState(false);
      const [items, setItems] = useState([]);
      const [isIndiaLoaded, setIsIndiaLoaded] = useState(true);
      const [indiaItems, setIndiaItems] = useState([]);

      // get gobal data
      useEffect(() => {
            fetch("https://coronavirus-19-api.herokuapp.com/countries")
                  .then(res => res.json())
                  .then(
                        (result) => {
                              setIsLoaded(true);
                              setItems(result);
                        },
                  )
      }, [])
      
      // get India Data
      // https://api.covid19india.org/state_district_wise.json
      useEffect(() => {
            fetch("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
                  .then(res => res.json())
                  .then(
                        (result) => {
                              setIsIndiaLoaded(true);
                              setIndiaItems(result.regionData);
                        },
                  );
      }, [])
      const filteredItems = items.filter((cur) => {
            return (cur.country.toLowerCase().includes(props.term.toLowerCase()))
      })
      const filteredIndiaItems = indiaItems.filter((cur) => {
            return (cur.region.toLowerCase().includes(props.term.toLowerCase()))
      })
      return (
      <Accordion className="text-center" defaultActiveKey="0">
        <Card>
          <Accordion.Toggle as={Card.Header} eventKey="0" id="worldTable">
            World Data
    </Accordion.Toggle>
          <Accordion.Collapse eventKey="0">
            <Card.Body>
            <Table striped bordered responsive>
                  {/* Headers */}
                  <thead>
                        <tr>
                              <th>Country</th>
                              <th>Cases</th>
                              <th>Active</th>
                              <th>Deaths</th>
                              <th>New Cases</th>
                              <th>New Deaths</th>
                              <th>Recovered</th>
                              <th>Mortality Rate</th>
                        </tr>
                  </thead>
                  <tbody>
                        {(!isLoaded) && <p>Loading...</p>}
                        {(isLoaded)&&
                              filteredItems.map((cur, index) => {
                                    return (
                                          <tr className="Data-Elem" key={index}>
                                                <td className="country">{cur.country}</td>
                                                <td className="cases"> {cur.cases}</td>
                                                <td className= "active-cases">{cur.active}</td>
                                                <td className="deaths text-danger">{cur.deaths}</td>
                                                <td className="todayCases">{cur.todayCases}</td>
                                                <td className="todayDeaths text-danger" >{cur.todayDeaths}</td>
                                                <td className="recovered text-success">{cur.recovered}</td>
                                                <td>{((cur.deaths /cur.cases)>=0.02)&&(<p className="text-danger">High</p>)}
                                                {((cur.deaths /cur.cases)>=0.015 && (cur.deaths /cur.cases)<0.02)&&(<p className="text-warning">Moderate</p>)}
                                                {((cur.deaths /cur.cases)<0.015)&&(<p className="text-success">Low</p>)}
                                                </td>
                                          </tr>
                                    )
                              })
                        }
                  </tbody>
            </Table>
            </Card.Body>
          </Accordion.Collapse>
          <Accordion.Toggle as={Card.Header} eventKey="1" id="indiaTable">
            India Data
    </Accordion.Toggle>
          <Accordion.Collapse eventKey="1">
            <Card.Body>
            <Table striped bordered responsive>
                  {/* Headers */}
                  <thead>
                        <tr>
                              <th>State</th>
                              <th>Cases</th>
                              <th>Active</th>
                              <th>Deaths</th>
                              <th>Change In Cases</th>
                              <th>New Deaths</th>
                              <th>Recovered</th>
                              <th>Severity</th>
                        </tr>
                  </thead>
                  <tbody>
                        {(!isIndiaLoaded)&& <p>Loading...</p>}
                        {(isIndiaLoaded)&&
                              filteredIndiaItems.map((cur, index) => {
                                    return (
                                          <tr className="Data-Elem" key={index}>
                                                <td className="country">{cur.region}</td>
                                                <td className="cases"> {cur.totalInfected}</td>
                                                <td className="active-cases">{cur.activeCases}</td>
                                                <td className="deaths text-danger">{cur.deceased}</td>
                                                <td className="todayCases">{cur.newInfected}</td>
                                                <td className="todayDeaths text-danger" >{cur.newDeceased}</td>
                                                <td className="recovered text-success">{cur.recovered}</td>
                                                <td>
                                                {
                                                      (cur.newInfected < -0.01*cur.totalInfected) && (
                                                            <p className="text-success">Green Zone</p>)
                                                }
                                                {
                                                      ((cur.newInfected <= 0) && !(cur.newInfected < -0.01*cur.totalInfected)) && (
                                                            <p className="text-warning">Orange Zone</p>
                                                      )
                                                }
                                                {
                                                      ((cur.newInfected >= 0)) && (
                                                      <p className="text-danger">Red Zone</p>
                                                      )
                                                }

                                                </td>
                                          </tr>
                                    )
                              })
                        }
                  </tbody>
            </Table>
            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
      );
}

export default Data
