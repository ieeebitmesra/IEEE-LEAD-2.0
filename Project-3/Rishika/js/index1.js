document.getElementById('world').addEventListener('click', worldData);
document.getElementById('submit').addEventListener('click', countryData);

getLocation();

function worldData() {

    const URL1 = "https://api.covid19api.com/summary";
    const main = document.getElementById("main");
    main.innerHTML = "<p>Loading...</p>";
    fetch(URL1)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let output =
                `<h2>World Data</h2>
    <ul list-style="none" font-size=25px>
    <li><strong>Total Confirmed : </strong> ${data.Global.TotalConfirmed}</li>
    <li><strong>Total Deaths : </strong> ${data.Global.TotalDeaths}</li>
    <li><strong>Total Recovered : </strong> ${data.Global.TotalRecovered}</li>
    <li><strong>New Confirmed : </strong> ${data.Global.NewConfirmed}</li>
    <li><strong>New Deaths : </strong> ${data.Global.NewDeaths}</li>
    <li><strong>New Recovered : </strong> ${data.Global.NewRecovered}</li>
  </ul>`;
            main.innerHTML = output;
        })
}

function countryData(e) {
    e.preventDefault();
    let ctry = document.getElementById('country').value.toUpperCase();
    //let state = document.getElementById('state').value.toUpperCase();

    const URL2 = "https://api.covid19api.com/summary";
    const main2 = document.getElementById("main-2");
    main2.innerHTML = "<p>Loading...</p>";
    fetch(URL2)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let output = ``;
            data.Countries.forEach(res => {
                if (`${res.Country}`.toUpperCase() == ctry) {
                    output +=
                        `<h3>${res.Country}</h3>
    <ul style="list-style-type:none;" font-size=25px>
    <li><strong>Total Confirmed : </strong> ${res.TotalConfirmed}</li>
    <li><strong>Total Deaths : </strong> ${res.TotalDeaths}</li>
    <li><strong>Total Recovered : </strong> ${res.TotalRecovered}</li>
    <li><strong>New Confirmed : </strong> ${res.NewConfirmed}</li>
    <li><strong>New Deaths : </strong> ${res.NewDeaths}</li>
    <li><strong>New Recovered : </strong> ${res.NewRecovered}</li>
     </ul>`;
                }
            })
            if(output==``){
            alert("Enter valid country name");
            output="Try Again.......";
            }
    main2.innerHTML = output;
        })
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position);
    } else {
        alert("Geolocation is not supported by the browser.");
    }
}

function position(position) {
    lat = position.coords.latitude;
    long = position.coords.longitude;
    console.log(lat, long);
    url = `https://api.opencagedata.com/geocode/v1/json?q=${lat}+${long}&key=afeb4a8547444ca8b0f2c76090a1d29c`;
    fetch(url)
        .then(response => response.json())
        //.then(console.log)
        .then(add => {
            let ctry = `${add.results[0].components.country}`.toUpperCase();
            let state = `${add.results[0].components.state}`.toUpperCase();
            let dist = `${add.results[0].components.state_district}`.toUpperCase();
            console.log(ctry, state,dist);
            if (ctry != "INDIA")
                displayLocOt(ctry);
            else
                displayLocIN(ctry, state, dist);
        }
        )
}

function displayLocOt(c) {
    //console.log(c);
    const loc = document.getElementById("loc");
    loc.innerHTML = "<p>Loading...</p>";
    const URLO = "https://api.covid19api.com/summary";

    fetch(URLO)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let output = ``;
            data.Countries.forEach(res => {
                if (`${res.Country}`.toUpperCase() == c) {
                    output +=
                        `<h3>${res.Country}</h3>
    <p><b>(Based on Your current Location)</b></p>
    <ul style="list-style-type:none;" font-size=25px>
    <li><strong>Total Confirmed : </strong> ${res.TotalConfirmed}</li>
    <li><strong>Total Deaths : </strong> ${res.TotalDeaths}</li>
    <li><strong>Total Recovered : </strong> ${res.TotalRecovered}</li>
    <li><strong>New Confirmed : </strong> ${res.NewConfirmed}</li>
    <li><strong>New Deaths : </strong> ${res.NewDeaths}</li>
    <li><strong>New Recovered : </strong> ${res.NewRecovered}</li>
     </ul>`;
                }
            })
            if (output == ``)
                output = `<p>Result not Found</p>`
            loc.innerHTML = output;
        })
}

//---------------------------------------------------------------------------------------------------------------------------------------

function displayLocIN(c, s,d ) {
    console.log(c,s);
    const loc = document.getElementById("loc");
    const loc2 = document.getElementById("loc2");
 
    loc.innerHTML = "<p>Loading...</p>";
    const URLO = "https://api.covid19api.com/summary";

    fetch(URLO)
        .then((resp) => {
            return resp.json();
        })
        .then((data) => {
            let output = ``;
            data.Countries.forEach(res => {
                if (`${res.Country}`.toUpperCase() == c) {
                    output +=
                        `<h3>${res.Country}</h3>
    <p><b>(Based on Your current Location)</b></p>
    <ul style="list-style-type:none;" font-size=25px>
    <li><strong>Total Confirmed : </strong> ${res.TotalConfirmed}</li>
    <li><strong>Total Deaths : </strong> ${res.TotalDeaths}</li>
    <li><strong>Total Recovered : </strong> ${res.TotalRecovered}</li>
    <li><strong>New Confirmed : </strong> ${res.NewConfirmed}</li>
    <li><strong>New Deaths : </strong> ${res.NewDeaths}</li>
    <li><strong>New Recovered : </strong> ${res.NewRecovered}</li>
     </ul>`;
                }
            })
    loc.innerHTML=output;
})
const URLI = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise";
    fetch(URLI)
        .then((response) => {
            return response.json();
        })
        //.then(console.log)
        .then((dat) => {
            let output2 = ``;
            dat.data.statewise.forEach(res => {
                        if (`${res.state}`.toUpperCase() == s)
                            output2 +=
                                `<h3>${res.state}</h3>
     <p><b>(Based on Your current Location)</b></p>
    <ul style="list-style-type:none;" font-size=25px>    
    <li><strong>Total Confirmed : </strong> ${res.confirmed}</li>
    <li><strong>Total Recovered : </strong> ${res.recovered}</li>
    <li><strong>Total Deaths : </strong> ${res.deaths}</li>
    <li><strong>Active Cases : </strong> ${res.active}</li>
     </ul>`;
                    }
            )
            if (output2 == ``)
            output2 = `<p>Result not Found</p>`
        loc2.innerHTML=output2;
})
}
