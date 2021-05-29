document.getElementById('submit').addEventListener('click', countryData);
document.getElementById('submit2').addEventListener('click', stateData);

worldData();
getLocation();

function worldData() {

    const URL1 = "https://api.covid19api.com/summary";
    const col1 = document.getElementById("col-1");
    const col2 = document.getElementById("col-2");
    const col3 = document.getElementById("col-3");
    const col4 = document.getElementById("col-4");
    col1.innerHTML = "<p>Loading...</p>";
    col2.innerHTML = "<p>Loading...</p>";
    col3.innerHTML = "<p>Loading...</p>";
    col4.innerHTML = "<p>Loading...</p>";
    fetch(URL1)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let out1 = `<h2>Cases Worldwide</h2>
            <p><img src="images/globe.jpg" alt="globe" height="100px"></p>`;
            let out2 = `<h3>Total Confirmed</h3>
            <p>${data.Global.TotalConfirmed}</p>
            <h3>New Confirmed</h3>
            <p>${data.Global.NewConfirmed}</p>`
            let out3 = `<h3>Total Recovered</h3>
            <p>${data.Global.TotalRecovered}</p>
            <h3>New Confirmed</h3>
            <p>${data.Global.NewRecovered}</p>`
            let out4 = `<h3>Total Deceased</h3>
            <p>${data.Global.TotalDeaths}</p>
            <h3>New Deceased</h3>
            <p>${data.Global.NewDeaths}</p>`
            col1.innerHTML = out1;
            col2.innerHTML = out2;
            col3.innerHTML = out3;
            col4.innerHTML = out4;
        })
}


//------------------------------------------------------------------------------------------------------------------------------


function countryData(e) {
    e.preventDefault();
    let ctry = document.getElementById('country').value.toUpperCase();

    const URL2 = "https://api.covid19api.com/summary";
    const col1 = document.getElementById("col-1");
    const col2 = document.getElementById("col-2");
    const col3 = document.getElementById("col-3");
    const col4 = document.getElementById("col-4");
    col1.innerHTML = "<p>Loading...</p>";
    col2.innerHTML = "<p>Loading...</p>";
    col3.innerHTML = "<p>Loading...</p>";
    col4.innerHTML = "<p>Loading...</p>";
    fetch(URL2)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let out1 = ``;
            let out2 = ``;
            let out3 = ``;
            let out4 = ``;
            data.Countries.forEach(res => {
                if (`${res.Country}`.toUpperCase() == ctry) {

                    out1 = `<h2>${res.Country}</h2>`;
                    out2 = `<h3>Total Confirmed</h3>
                    <p>${res.TotalConfirmed}</p>
                    <h3>New Confirmed</h3>
                    <p>${res.NewConfirmed}</p>`
                    out3 = `<h3>Total Recovered</h3>
                    <p>${res.TotalRecovered}</p>
                    <h3>New Confirmed</h3>
                    <p>${res.NewConfirmed}</p>`
                    out4 = `<h3>Total Deceased</h3>
                    <p>${res.TotalDeaths}</p>
                    <h3>New Deceased</h3>
                    <p>${res.NewDeaths}</p>`
                }
            })
            if (out1 == ``) {
                alert("Enter valid country name");
            }
            else
                col1.innerHTML = out1;
            col2.innerHTML = out2;
            col3.innerHTML = out3;
            col4.innerHTML = out4;
        })
}


//-------------------------------------------------------------------------------------------------------------------------------------------

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
            let sta_c = `${add.results[0].components.state}`.toUpperCase();
            let dist = `${add.results[0].components.state_district}`.toUpperCase();
            console.log(ctry, state, dist);
            //ctry="JAPAN";
            if (ctry != "INDIA")
                displayLocOt(ctry);
            else
                displayLocIN("INIDA", "BIHAR", "NALANDA");
        }
        )
}


//----------------------------------------------------------------------------------------------------------------

function displayLocOt(c) {
    //console.log(c);
    const URL2 = "https://api.covid19api.com/summary";

    const col11 = document.getElementById("stt");
    const col12 = document.getElementById("col-12");
    const col13 = document.getElementById("col-13");
    const col14 = document.getElementById("col-14");
    const col15 = document.getElementById("col-15");
    col12.innerHTML = "<p>Loading...</p>";
    col13.innerHTML = "<p>Loading...</p>";
    col14.innerHTML = "<p>Loading...</p>";
    col15.innerHTML = "<p>Loading...</p>";
    fetch(URL2)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            let out = "(Based on your current location)";
            let out1 = ``;
            let out2 = ``;
            let out3 = ``;
            let out4 = ``;
            data.Countries.forEach(res => {
                if (`${res.Country}`.toUpperCase() == c) {

                    out1 = `<h2>${res.Country}</h2>`;
                    out2 = `<h3>Total Confirmed</h3>
                    <p>${res.TotalConfirmed}</p>
                    <h3>New Confirmed</h3>
                    <p>${res.NewConfirmed}</p>`;
                    out3 = `<h3>Total Recovered</h3>
                    <p>${res.TotalRecovered}</p>
                    <h3>New Confirmed</h3>
                    <p>${res.NewConfirmed}</p>`;
                    out4 = `<h3>Total Deceased</h3>
                    <p>${res.TotalDeaths}</p>
                    <h3>New Deceased</h3>
                    <p>${res.NewDeaths}</p>`;
                }
            })
            col11.innerHTML = out;
            col12.innerHTML = out1;
            col13.innerHTML = out2;
            col14.innerHTML = out3;
            col15.innerHTML = out4;

        })
}
//--------------------------------------------------------------------------------------------------------------------------------------------------
function capitalize(inp) {
    var words = inp.split(' ');
    var cap = [];
    words.forEach(ele => {
        cap.push(ele[0].toUpperCase() + ele.slice(1, ele.length));
    });
    return cap.join(' ');

}


//---------------------------------------------------------------------------------------------------------------------------------------

function displayLocIN(c, s, d) {
    let sn = capitalize(s.toLowerCase());
    let dn = capitalize(d.toLowerCase());
    console.log(sn, dn);
    const col11 = document.getElementById("stt");
    const col12 = document.getElementById("col-12");
    const col13 = document.getElementById("col-13");
    const col14 = document.getElementById("col-14");
    const col15 = document.getElementById("col-15");
    col12.innerHTML = "<p>Loading...</p>";
    col13.innerHTML = "<p>Loading...</p>";
    col14.innerHTML = "<p>Loading...</p>";
    col15.innerHTML = "<p>Loading...</p>";


    const URLI = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise";
    fetch(URLI)
        .then((response) => {
            return response.json();
        })
        //.then(console.log)
        .then((dat) => {
            let out = ``;
            let out1 = ``;
            let out2 = ``;
            let out3 = ``;
            let out4 = ``;
            dat.data.statewise.forEach(res => {
                if (`${res.state}`.toUpperCase() == s) {
                    out = `<h3>State - ${res.state}</h3>
                    <p>(Based on your current location)</p>`;
                    out1 = `<h3>Active Cases</h3>
                    <p>${res.active}</p>`;
                    out2 = `<h3>Total Confirmed</h3>
                    <p>${res.confirmed}</p>`;
                    out3 = `<h3>Total Recoverd</h3>
                    <p>${res.recovered}</p>`;
                    out4 = `<h3>Total Deceased</h3>
                    <p>${res.deaths}</p>`;
                }
            }
            )
            if (out2 == ``)
                out2 = `<p>Result not Found</p>`
            else {
                col11.innerHTML = out;
                col12.innerHTML = out1;
                col13.innerHTML = out2;
                col14.innerHTML = out3;
                col15.innerHTML = out4;
            }
        })
    const col21 = document.getElementById("dis");
    const col22 = document.getElementById("col-22");
    const col23 = document.getElementById("col-23");
    const col24 = document.getElementById("col-24");
    const col25 = document.getElementById("col-25");
    col22.innerHTML = "<p>Loading...</p>";
    col23.innerHTML = "<p>Loading...</p>";
    col24.innerHTML = "<p>Loading...</p>";
    col25.innerHTML = "<p>Loading...</p>";
    const URLD = "https://api.covid19india.org/state_district_wise.json";
    fetch(URLD)
        .then((resp) => {
            return resp.json()
        })
        //.then(console.log)
        .then((data) => {
            let v= `data.${sn}.districtData.${dn}.confirmed`;
           // let $sn= gfuigfu; 
            console.log(v);
            let out = `<h3>District - ${dn}</h3>
            <p>(Based on your current location)</p>`;
            let out1 = `<h3>Active Cases</h3>
            <p>${data[sn]['districtData'][dn]['active']}</p>`;
            out2 = `<h3>Total Confirmed</h3>
            <p>${data[sn]['districtData'][dn]['confirmed']}</p>`;
            out3 = `<h3>Total Recoverd</h3>
            <p>${data[sn]['districtData'][dn]['recovered']}</p>`;
            out4 = `<h3>Total Deceased</h3>
            <p>${data[sn]['districtData'][dn]['deceased']}</p>`;


        

    if (out2 == ``)
        out2 = `<p>Result not Found</p>`
    else {
        col21.innerHTML = out;
        col22.innerHTML = out1;
        col23.innerHTML = out2;
        col24.innerHTML = out3;
        col25.innerHTML = out4;
    }      }  )
}


//------------------------------------------------------------------------------------------------------

function stateData(e) {
    e.preventDefault();
    let state = document.getElementById('state').value.toUpperCase();

    const col11 = document.getElementById("stt");
    const col12 = document.getElementById("col-12");
    const col13 = document.getElementById("col-13");
    const col14 = document.getElementById("col-14");
    const col15 = document.getElementById("col-15");
    col12.innerHTML = "<p>Loading...</p>";
    col13.innerHTML = "<p>Loading...</p>";
    col14.innerHTML = "<p>Loading...</p>";
    col15.innerHTML = "<p>Loading...</p>";


    const URLI = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise";
    fetch(URLI)
        .then((response) => {
            return response.json();
        })
        //.then(console.log)
        .then((dat) => {
            let out = ``;
            let out1 = ``;
            let out2 = ``;
            let out3 = ``;
            let out4 = ``;
            dat.data.statewise.forEach(res => {
                if (`${res.state}`.toUpperCase() == state) {
                    out = `<h3>State - ${res.state}</h3>`;
                    out1 = `<h3>Active Cases</h3>
                    <p>${res.active}</p>`;
                    out2 = `<h3>Total Confirmed</h3>
                    <p>${res.confirmed}</p>`;
                    out3 = `<h3>Total Recoverd</h3>
                    <p>${res.recovered}</p>`;
                    out4 = `<h3>Total Deceased</h3>
                    <p>${res.deaths}</p>`;
                }
            }
            )
            if (out2 == ``) {
                alert("Enter a valid state or district.")
                out = `<p>Result not Found</p>`;
                col11.innerHTML = out;
            }
            else {
                col11.innerHTML = out;
                col12.innerHTML = out1;
                col13.innerHTML = out2;
                col14.innerHTML = out3;
                col15.innerHTML = out4;
            }
        })

        document.getElementById("col-21").style.display="none";
        document.getElementById("row-4").style.display="none";
       /* const col21 = document.getElementById("dis");
    const col22 = document.getElementById("col-22");
    const col23 = document.getElementById("col-23");
    const col24 = document.getElementById("col-24");
    const col25 = document.getElementById("col-25");
    col22.innerHTML = "<p>Loading...</p>";
    col23.innerHTML = "<p>Loading...</p>";
    col24.innerHTML = "<p>Loading...</p>";
    col25.innerHTML = "<p>Loading...</p>";
    const URLD = "https://api.covid19india.org/state_district_wise.json";
    fetch(URLD)
        .then((resp) => {
            return resp.json()
        })
        //.then(console.log)
        .then((data) => {
            let out = `<h3>District - ${dn}</h3>`;
            let out1 = `<h3>Active Cases</h3>
            <p>${data.sn.districtData.dn.active}</p>`;
            out2 = `<h3>Total Confirmed</h3>
            <p>${data.sn.districtData.dn.confirmed}</p>`;
            out3 = `<h3>Total Recoverd</h3>
            <p>${data.sn.districtData.dn.recovered}</p>`;
            out4 = `<h3>Total Deceased</h3>
            <p>${data.sn.districtData.dn.deceased}</p>`;


        

    if (out2 == ``)
        out2 = `<p>Result not Found</p>`
    else {
        col21.innerHTML = out;
        col22.innerHTML = out1;
        col23.innerHTML = out2;
        col24.innerHTML = out3;
        col25.innerHTML = out4;
    }      }  )*/
}