let today = new Date();//gives current date and time


let MonthOfYear = new Array(12);
MonthOfYear[0] = "January";
MonthOfYear[1] = "February";
MonthOfYear[2] = "March";
MonthOfYear[3] = "April";
MonthOfYear[4] = "May";
MonthOfYear[5] = "June";
MonthOfYear[6] = "July";
MonthOfYear[7] = "August";
MonthOfYear[8] = "September";
MonthOfYear[9] = "October";
MonthOfYear[10] = "November";
MonthOfYear[11] = "December";

let currentHours = today.getHours();

let greeting = "";

if(currentHours >= 5 && currentHours < 12){
    greeting = "Good Morning 🌄 ,";
}

else if(currentHours >= 12 && currentHours < 17){
    greeting = "Good AfterNoon 🌞 ,";
}

else if(currentHours >= 17 && currentHours < 21){
    greeting = "Good Evening 🌝 ,";
}
else{
    greeting = "Good Night 🌙 ,";
}

let strDate = greeting + " " + today.getDate() + " / " + (MonthOfYear[today.getMonth()]) + " / " + today.getFullYear()
document.getElementById("header-date").innerHTML = strDate;



let i = 0;
let txt = 'Search for any Country'; 
let speed = 100;
function typingeffect() {
  if (i < txt.length) {
    document.getElementById("typing").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typingeffect, speed);
  }
}



// For World COVID Details

fetch("https://corona-virus-world-and-india-data.p.rapidapi.com/api", {
    "method": "GET",
    "headers": {
        "x-rapidapi-key": "7e8f102469msh9f81ccf22836c18p1b8991jsn1815ef40212f",
        "x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com"
    }
})

    .then(response => {
        // console.log(response);
        return response.json()
    }).then(data => {
        console.log(data);

        console.log(data.world_total);

        let updateTime = "Updated on " + data.statistic_taken_at;
        document.getElementById('updateTime').innerHTML = updateTime;

        let worldTotalResults = `<li class = "caseClass">Total Cases: ${data.world_total.total_cases}`;

        worldTotalResults += `<li class = "deathClass">Total Deaths: ${data.world_total.total_deaths}`;

        worldTotalResults += `<li class = "recoveredClass">Total Recovered: ${data.world_total.total_recovered}`;

        worldTotalResults += `<li class = "caseClass">Today new Cases: ${data.world_total.new_cases}`;

        worldTotalResults += `<li class = "deathClass">Today new Deaths: ${data.world_total.new_deaths}`;

        document.getElementById('world-results').innerHTML = worldTotalResults;


        document.getElementById("country-input").addEventListener("click", function () {

            let inputCountry = document.getElementById('input_country').value;

            var flag = 0;

            for (var i = 0; i < data.countries_stat.length; i++) {
                if (inputCountry.toUpperCase() === data.countries_stat[i].country_name.toUpperCase()) {

                    console.log(data.countries_stat[i].cases);
                    let searchedCountryResults = `<li class = "caseClass">Total Cases in ${inputCountry.toUpperCase()} : ${data.countries_stat[i].cases}</li>`;

                    console.log(data.countries_stat[i].deaths);
                    searchedCountryResults += `<li  class = "deathClass">Total Deaths in ${inputCountry.toUpperCase()} : ${data.countries_stat[i].deaths}</li>`;

                    console.log(data.countries_stat[i].total_recovered);
                    searchedCountryResults += `<li class = "recoveredClass">Total Recovered in ${inputCountry.toUpperCase()} : ${data.countries_stat[i].cases}</li>`;


                    document.getElementById('searched-country').innerHTML = searchedCountryResults;

                    flag = 1;

                }
            }

            if (flag === 0) {
                alert("Country name is Invalid")
            }

            // console.log(inputCountry);

        });



    })


// Location Tracker

const successCallback = (position) => {
    // console.log(position);
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;

    const urlLocation = `https://us1.locationiq.com/v1/reverse.php?key=pk.362a3b52e3bd0cfa83412d54962ae4e6&lat=${latitude}&lon=${longitude}&format=json` ;

    console.log(urlLocation);

    fetch(urlLocation).then(response => {
        return response.json()
    }).then(data => {
        console.log(data);

        document.getElementById("regionData").addEventListener("click", () => {
            locationSearch(data);
        });

        // locationSearch(data);

    })

}
const errorCallback = (error) => {
    console.log(error);
}

navigator.geolocation.getCurrentPosition(successCallback, errorCallback)



function locationSearch(data) {
    // let stringDistrict = "District: " + data.data[0].locality
    // document.getElementById('district').innerHTML = stringDistrict;

    // let stringState = "State: " + data.data[0].region
    // document.getElementById('state').innerHTML = stringState;

    // let stringCountry = "Country: " + data.data[0].country
    // document.getElementById('country').innerHTML = stringCountry;




    let currentDistrict = data.address.state_district;
    let currentState = data.address.state;
    let currentCountry = data.address.country;

    if (data.address.country.toUpperCase() === "INDIA") {
        console.log(data.address.country.toUpperCase());

        fetch("https://corona-virus-world-and-india-data.p.rapidapi.com/api_india", {
            "method": "GET",
            "headers": {
                "x-rapidapi-key": "7e8f102469msh9f81ccf22836c18p1b8991jsn1815ef40212f",
                "x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com"
            }
        })
            .then(response => {
                // console.log(response);
                return response.json()
            }).then(data => {
                console.log(data.state_wise);


                let state = data.state_wise;

                // active , deaths , recovered

                for (let i in state) {
                    // console.log(i);
                    // console.log(state[i]);

                    if (i.toUpperCase() === currentState.toUpperCase()) {
                        console.log(i);
                        console.log(state[i]);

                        let currentHeading = `<h1>Current Location Details: </h1>`
                        document.getElementById('current-heading').innerHTML = currentHeading;

                        let currentInfo = `You Current location is ${currentDistrict} , ${currentState} , ${currentCountry} .`
                        document.getElementById('current-info').innerHTML = currentInfo;

                        let currentLocationResults = `<li class = "caseClass">Total Cases : ${state[i].active}</li>`;

                        currentLocationResults += `<li class = "deathClass">Total Deaths : ${state[i].deaths}</li>`;

                        currentLocationResults += `<li class = "recoveredClass">Total Recovered : ${state[i].recovered}</li>`;

                        document.getElementById('current-results').innerHTML = currentLocationResults;

                    }

                }

                // console.log(data.state_wise.Maharashtra);


            })

    }
}
