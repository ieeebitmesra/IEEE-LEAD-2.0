import React, { useState } from 'react'
import './App.css';
import Data from './components/Data/Data'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, FormControl,  Nav, Form } from "react-bootstrap"
import Landing from './components/Landing/Landing';
function App() {
  const [searchValue, setSearchValue] = useState("")
  return (
    <div className="App">
      {/* Navbar */}
      <Navbar className="customNav" variant="dark" expand="lg" sticky="top">
        <Navbar.Brand href="#home">Covid Tracker</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="#worldTable" variant="dark">World Data</Nav.Link>
            <Nav.Link href="#indiaTable" variant="dark">India Data</Nav.Link>
          </Nav>
          <Form inline>
          <FormControl type="search" placeholder="Search" className="w-100" onChange={(Event) => {
            setSearchValue(Event.target.value);
          }} value={searchValue} />
          </Form>
        </Navbar.Collapse>
      </Navbar>
      {/* Home */}
      <Landing/>
      {/* Data Sheets */}
      <Data term={searchValue} />
    </div>
  );
}

export default App;
