/*
UK --
UAE 
DRC
*/

// World data

function worlddata(){
    function getdata(){
        url = 'https://coronavirus-19-api.herokuapp.com/countries';
        fetch(url)
        .then(response => response.json())
        .then((data) => {
            // console.log(data)
            // let apidata = `<h2>World Covid Stats</h2>
            // <p>Total Cases: ${data[0].cases} | Today Cases: ${data[0].todayCases}<br>
            // Deaths: ${data[0].deaths} | Today Deaths: ${data[0].todayDeaths}<br>
            // Recovered: ${data[0].recovered}<br>
            // Active: ${data[0].active}<br>
            // Critical: ${data[0].critical}</p>
            // `
            let apidata = `
            <div class="world-data-card">
                <div class="title">
                    World COVID Stats
                </div>
                <div class="data">
                    <p>Total Cases: ${data[0].cases} | Today Cases: ${data[0].todayCases}<br></p>
                    <p class = "deaths">Total Deaths: ${data[0].deaths} | Today Deaths: ${data[0].todayDeaths}<br></p>
                    <p class = "recovered">Recovered Cases: ${data[0].recovered}<br></p>
                    <p>Active Cases: ${data[0].active}<br></p>
                    <p>Critical Cases: ${data[0].critical}</p>
                </div>
            </div>
            `
            document.querySelector('.main-content').innerHTML=apidata
            document.querySelector('.invis').classList.add('vis')
        })
    }
    getdata()
    // getUserLocation()
}

function countryWiseData(){
    let content = `
    <div class="head">
        <div class="content-title">
            Country-wise COVID Stats
        </div>
        <div class="searchbar">
            <input type="text" name="searchbox" id="searchbox" placeholder="Country name" onkeyup="searchResults()">
        </div>
    </div>
    `
    url = 'https://coronavirus-19-api.herokuapp.com/countries';
    fetch(url)
    .then(response => response.json())
    .then((data)=>{
        let apidata='<div class="country-card-container">';
        for (let i = 1; i < data.length; i++) {
            apidata+=`
                <div class="country-data-card">
                    <div class="country-name">
                        ${data[i].country}
                    </div>
                    <div class="country-data">
                        Total Cases: ${data[i].cases} | Today Cases: ${data[i].todayCases}<br>
                        <span class="deaths">Total Deaths: ${data[i].deaths} | Today Deaths: ${data[i].todayDeaths}</span><br>
                        <span class="recovered">Recovered Cases: ${data[i].recovered}</span><br>
                        Active Cases: ${data[i].active}<br>
                        Critical Cases: ${data[i].critical}
                    </div>
                </div>
            `
        }
        apidata += '</div>';
        content += apidata 
        document.querySelector('.main-content').innerHTML=content;
        document.querySelector('.invis').classList.add('vis')
        })
        // document.getElementById('searchbox').addEventListener('keyup',search_results)
}

function displaySearchResults(data){
    let apidata='<div class="country-card-container">';
        for (let i = 0; i < data.length; i++) {
            apidata+=`
                <div class="country-data-card">
                    <div class="country-name">
                        ${data[i].country}
                    </div>
                    <div class="country-data">
                        Total Cases: ${data[i].cases} | Today Cases: ${data[i].todayCases}<br>
                        <span class="deaths">Total Deaths: ${data[i].deaths} | Today Deaths: ${data[i].todayDeaths}</span><br>
                        <span class="recovered">Recovered Cases: ${data[i].recovered}</span><br>
                        Active Cases: ${data[i].active}<br>
                        Critical Cases: ${data[i].critical}
                    </div>
                </div>
            `
        }
        apidata += '</div>';
        // content += apidata 
        document.querySelector('.country-card-container').innerHTML=apidata;
        document.querySelector('.invis').classList.add('vis')
}

function searchResults(){
    let searchedItem = document.querySelector('#searchbox').value
    // console.log(searched_item)
    url = 'https://coronavirus-19-api.herokuapp.com/countries';
    fetch(url)
    .then(response => response.json())
    .then((data)=>{
        let filteredData = data.filter((Country)=> {
            return (Country.country.toLowerCase().includes(searchedItem.toLowerCase()) && Country.country != 'World')
        })
        displaySearchResults(filteredData)
    })
}

function displayResults(data){
    apidata = '<div class="state-card-container">';
    for (let i = 0; i < data.length; i++) {
        apidata+=`
            <div class="state-data-card">
                <div class="state-name">
                    ${data[i].region}
                </div>
                <div class="state-data">
                <span class= ${((data[i].newInfected)>0)? `up`:`down`}>Total Cases: ${data[i].totalInfected} | Today Cases: ${Math.abs(data[i].newInfected)}</span><br>
                    <span class="deaths">Total Deaths: ${data[i].deceased} | Today Deaths: ${data[i].newDeceased}</span><br>
                    <span class="recovered">Recovered Cases: ${data[i].recovered}</span><br>
                    Active Cases: ${data[i].activeCases}<br>
                    </div>
                    ${zoneDecider(data[i].newInfected,data[i].activeCases)}
            </div>
        `
    }
    apidata += '</div>';
    document.querySelector('.state-card-container').innerHTML=apidata;
}

function IndiaResults(){
    let searchedItem = document.querySelector('#searchbox').value
    url = 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true';
    fetch(url)
    .then(response => response.json())
    .then((data)=>{
        let filteredData = data.regionData.filter(state=> state.region.toLowerCase().includes(searchedItem.toLowerCase()))
        displayResults(filteredData)
    })
    
}

function zoneDecider(change,activeCases){
    let content=''
    if(change/activeCases<=0){
        content+=`
        <div class="zone-card green-zone-card" style="background-color: #5DD75E ;">
            <div class="zone-color">
                GREEN Zone
            </div>
            <div class="advisory">
                Follow them and protect yourself and others from infection:
                    <li>Stay inside your home and do not travel.</li>
                    <li>Wear mask, use sanitizer and practice social distancing.</li>
                    <li>Register yourself for VACCINATION.</li>
                </ul>
                <div class="links green-zone-links">
                    Informative links:<br> <a href="https://www.youtube.com/watch?v=BtN-goy9VOY">What CORONAVIRUS is?</a><br>
                    <a href="https://www.youtube.com/watch?v=zBkVCpbNnkU">How VACCINES work?</a><br>
                    <a href="https://www.google.com/intl/en_in/covid19/#safety-tips">Join the fight against COVID-19</a>
                </div>
            </div>
        </div>
        `
    }
    else if(change/activeCases>0 && change/activeCases<=0.02)
    {
        content+=`
        <div class="zone-card orange-zone-card" style="background-color: orange;">
            <div class="zone-color">
                ORANGE Zone
            </div>
            <div class="advisory">
                Follow them and protect yourself and others from infection:
                    <li>Stay inside your home and do not travel.</li>
                    <li>Wear mask, use sanitizer and practice social distancing.</li>
                    <li>Register yourself for VACCINATION.</li>
                </ul>
                <div class="links orange-zone-links">
                    Informative links:<br> <a href="https://www.youtube.com/watch?v=BtN-goy9VOY">What CORONAVIRUS is?</a><br>
                    <a href="https://www.youtube.com/watch?v=zBkVCpbNnkU">How VACCINES work?</a><br>
                    <a href="https://www.google.com/intl/en_in/covid19/#safety-tips">Join the fight against COVID-19</a>
                </div>
            </div>
        </div>
        `
    }
    else{
        content+=`
        <div class="zone-card red-zone-card" style="background-color: #b2151c;">
            <div class="zone-color">
                RED Zone
            </div>
            <div class="advisory">
                Follow them and protect yourself and others from infection:
                    <li>Stay inside your home and do not travel.</li>
                    <li>Wear mask, use sanitizer and practice social distancing.</li>
                    <li>Register yourself for VACCINATION.</li>
                </ul>
                <div class="links red-zone-links">
                    Informative links:<br> <a href="https://www.youtube.com/watch?v=BtN-goy9VOY">What CORONAVIRUS is?</a><br>
                    <a href="https://www.youtube.com/watch?v=zBkVCpbNnkU">How VACCINES work?</a><br>
                    <a href="https://www.google.com/intl/en_in/covid19/#safety-tips">Join the fight against COVID-19</a>
                </div>
            </div>
        </div>
        `
    }
    return content
}

function indiaStateData(){
    let content = `
    <div class="head">
        <div class="content-title">
            India COVID Stats
        </div>
        <div class="searchbar">
            <input type="text" name="searchbox" id="searchbox" placeholder="State name" onkeyup="IndiaResults()">
        </div>
    </div>
    `
    url = 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true';
    fetch(url)
    .then(response=> response.json())
    .then((data) => {
        let apidata='<div class="state-card-container">';
        for (let i = 0; i < data.regionData.length; i++) {
            apidata+=`
                <div class="state-data-card">
                    <div class="state-name">
                        ${data.regionData[i].region}
                    </div>
                    <div class="state-data">
                        <span class= ${((data.regionData[i].newInfected)>0)? `up`:`down`}>Total Cases: ${data.regionData[i].totalInfected} | Change in Cases: ${Math.abs(data.regionData[i].newInfected)}</span><br>
                        <span class="deaths">Total Deaths: ${data.regionData[i].deceased} | Today Deaths: ${data.regionData[i].newDeceased}</span><br>
                        <span class="recovered">Recovered Cases: ${data.regionData[i].recovered}</span><br>
                        Active Cases: ${data.regionData[i].activeCases}<br>
                    </div>
                    ${zoneDecider(data.regionData[i].newInfected,data.regionData[i].activeCases)}
                </div>
            `
        }
        apidata += '</div>';
        content += apidata 
        document.querySelector('.main-content').innerHTML=content;
        document.querySelector('.invis').classList.add('vis')
    })
}

function userLocationData(userCountry,userState){
    console.log(userCountry)
    if(userCountry === "United Kingdom"){
        userCountry ="UK"
    }
    if(userCountry === "United Arab Emirates"){
        userCountry ="UAE"
    }
    if(userCountry === "Democratic Republic of Congo"){
        userCountry ="DRC"
    }
    let content = '';
    let countryData, stateData;
    // fetching user country data
    url = 'https://coronavirus-19-api.herokuapp.com/countries';
    fetch(url)
    .then(response => response.json())
    .then((data)=>{
        countryData = data.filter(Country => Country.country.toLowerCase().includes(userCountry.toLowerCase()));
        // fetching user state data
    url = 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true';
    fetch(url)
    .then(response=> response.json())
    .then((data) => {
        stateData = data.regionData.filter(State => State.region.toLowerCase().includes(userState.toLowerCase()));
        countryData = countryData[0];
        stateData = stateData[0];
        content = `
        <div class= "location-data-card">
            <div class="location-head">
                COVID Stats at Your Location
            </div>
            <div class="country-data-card">
                <div class="country-name">
                    ${countryData.country}
                </div>
                <div class="country-data">
                    Total Cases: ${countryData.cases} | Today Cases: ${countryData.todayCases}<br>
                    <span class="deaths">Total Deaths: ${countryData.deaths} | Today Deaths: ${countryData.todayDeaths}</span><br>
                    <span class="recovered">Recovered Cases: ${countryData.recovered}</span><br>
                    Active Cases: ${countryData.active}<br>
                </div>
            </div>
            ${(userCountry === "India")?(`<div class="state-data-card">
                <div class="state-name">
                    ${stateData.region}
                </div>
                <div class="state-data">
                <span class= ${((stateData.newInfected)>0)? `up`:`down`}>Total Cases: ${stateData.totalInfected} | Today Cases: ${Math.abs(stateData.newInfected)}</span><br>
                    <span class="deaths">Total Deaths: ${stateData.deceased} | Today Deaths: ${stateData.newDeceased}</span><br>
                    <span class="recovered">Recovered Cases: ${stateData.recovered}</span><br>
                    Active Cases: ${stateData.activeCases}<br>
                </div>
                ${zoneDecider(stateData.newInfected,stateData.activeCases)}
            </div>`):(``)
        }
    </div>
    `
    document.querySelector('.main-content').innerHTML=content;
    document.querySelector('.invis').classList.add('vis')
    })
    })
    
}

function getUserLocation(){
    function getUserAdderess(latitude,longitude){
        token = 'pk.eyJ1IjoiaXNoYW5wYW5kZXkiLCJhIjoiY2twODVqNHR6MDFkdzJ3bzI2a2diMmdsMSJ9.e2bqvaC55FncJeQop2opTQ'
        url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${longitude},${latitude}.json?&access_token=${token}`
        fetch(url)
        .then(response => response.json())
        .then((data) => {
            
            let actualNum = 4;
            var i;
            for(i=0; i<data.features.length; i++){
                if (data.features[i].id.includes("country")){
                    actualNum = i
                    console.log(actualNum)
                }
            }
            const userCountry = data.features[actualNum].text;
            const userState = data.features[actualNum - 1].text;
            userLocationData(userCountry,userState)
            console.log(data)
        })
    }

    function success(position) {
        const latitude  = position.coords.latitude;
        const longitude = position.coords.longitude;
        console.log(`latitude: ${latitude}`)
        console.log(`longitude: ${longitude}`)
        
        getUserAdderess(latitude,longitude)
    }
    
    function error() {
        status.textContent = 'Unable to retrieve your location';
    }

    if(!navigator.geolocation) {
        console.log('Geolocation is not supported by your browser')
    } else {
        navigator.geolocation.getCurrentPosition(success, error);
    }

}


document.querySelector('.world-card').addEventListener('mousedown',worlddata)
document.querySelector('.country-card').addEventListener('click',countryWiseData)
document.querySelector('.India-card').addEventListener('click',indiaStateData)
document.querySelector('.user-location-card').addEventListener('click',getUserLocation)
