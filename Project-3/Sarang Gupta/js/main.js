// function to fetch world data
function getData() {

    fetch("https://covid-19-tracking.p.rapidapi.com/v1", {
        "method": "GET",
        "headers": {
            "x-rapidapi-key": "30783a336emsh8f107ac4963783dp12931fjsn8dbc83f14b62",
            "x-rapidapi-host": "covid-19-tracking.p.rapidapi.com"
        }
    })
        .then((response) => {
            return response.json();
        }).then((data) => {
            displayData(data);
            countryData(data);

        })
}
//function to display world data
function displayData(data) {
    let activeCase = document.getElementById('activecase')
    let newcase = document.getElementById('newcase')
    let newdeath = document.getElementById('newdeath')
    let totalcase = document.getElementById('totalcase')
    let totaldeath = document.getElementById('totaldeath')
    let totalrecovered = document.getElementById('totalrecovered')
    activeCase.innerHTML = data[0]['Active Cases_text']
    newcase.innerHTML = data[0]['New Cases_text']
    newdeath.innerHTML = data[0]['New Deaths_text']
    totalcase.innerHTML = data[0]['Total Cases_text']
    totaldeath.innerHTML = data[0]['Total Deaths_text']
    totalrecovered.innerHTML = data[0]['Total Recovered_text']
}
getData();
var fetchedData;
var indiaData;
// function to display default country data i.e USA before the user searches for any other country
function countryData(data) {
    fetchedData = data;
    let cont = document.getElementById('countryname')
    let activeCase = document.getElementById('countryactive')
    let newcase = document.getElementById('countrynewc')
    let newdeath = document.getElementById('countrynewd')
    let totalcase = document.getElementById('countrytotalc')
    let totaldeath = document.getElementById('countrytotald')
    let totalrecovered = document.getElementById('countrytotalr')
    let alertcard = document.getElementById('cardalert')
    let alerttext = document.getElementById('alerttext')
    cont.innerHTML = 'USA'
    totalcase.innerHTML = "Total Cases: " + data[1]['Total Cases_text']
    activeCase.innerHTML = "Active Cases: " + data[1]['Active Cases_text']
    totalrecovered.innerHTML = "Total Recovered: " + data[1]['Total Recovered_text']
    totaldeath.innerHTML = "Total Deaths: " + data[1]['Total Deaths_text']
    if (data[1]['New Cases_text'] == "") {
        data[1]['New Cases_text'] = 'NA';
    }
    if (data[1]['New Deaths_text'] == "") {
        data[1]['New Deaths_text'] = 'NA'
    }
    newcase.innerHTML = "New Cases: " + data[1]['New Cases_text']
    newdeath.innerHTML = "New Deaths: " + data[1]['New Deaths_text']
    alertcard.style.backgroundColor = 'red';
    alerttext.innerHTML = 'USA is in HIGH risk zone as it is among top 10 worst COVID-19 affected countries so,please STAY HOME STAY SAFE';


}
//funtion to display country-wise data according to the search of the user
function displayCountryData() {
    let str = document.getElementById('countrytext').value
    let final = str.toUpperCase();
    fetchedData.forEach(function (element) {
        if (element['Country_text'].toUpperCase() == final) {
            console.log(element['Country_text'].toUpperCase())
            let alertIndex = fetchedData.indexOf(element)
            let alertcard = document.getElementById('cardalert')
            let alerttext = document.getElementById('alerttext')
            let cont = document.getElementById('countryname')
            let activeCase = document.getElementById('countryactive')
            let newcase = document.getElementById('countrynewc')
            let newdeath = document.getElementById('countrynewd')
            let totalcase = document.getElementById('countrytotalc')
            let totaldeath = document.getElementById('countrytotald')
            let totalrecovered = document.getElementById('countrytotalr')
            
            cont.innerHTML = element['Country_text']
            totalcase.innerHTML = "Total Cases: " + element['Total Cases_text']
            activeCase.innerHTML = "Active Cases: " + element['Active Cases_text']
            totalrecovered.innerHTML = "Total Recovered: " + element['Total Recovered_text']
            totaldeath.innerHTML = "Total Deaths: " + element['Total Deaths_text']
            if (element['New Cases_text'] == "") {
                element['New Cases_text'] = 'NA';
            }
            if (element['New Deaths_text'] == "") {
                element['New Deaths_text'] = 'NA'
            }
            newcase.innerHTML = "New Cases: " + element['New Cases_text']
            newdeath.innerHTML = "New Deaths: " + element['New Deaths_text']
            if (alertIndex <= 11) {
                alertcard.style.backgroundColor = 'red';
                alerttext.innerHTML = element['Country_text'].toUpperCase() + ' is in HIGH risk zone, as it is among top 10 worst COVID-19 affected countries so,please STAY HOME STAY SAFE';

            }
            else if (alertIndex <= 50) {
                alertcard.style.backgroundColor = 'orange'
                alerttext.innerHTML = element['Country_text'].toUpperCase() + ' is in MODERATE risk zone, as it is among top 50 worst COVID-19 affected countries so,please STAY HOME STAY SAFE';
            }
            else {
                alertcard.style.backgroundColor = 'green'
                alerttext.innerHTML = element['Country_text'].toUpperCase() + ' is in LOW risk zone,as it is not among top 50 worst COVID-19 affected countries so,please STAY HOME STAY SAFE';
            }
            
        }
       
    })
    
   
}
//event lister for clicking on search button to get data of the country entered by the user
let dispContData = document.getElementById('get')
dispContData.addEventListener('click', () => {
    displayCountryData();
})
//function to get Indian covid stats and printing it in a tabular format
function getIndiaData() {
    fetch("https://corona-virus-world-and-india-data.p.rapidapi.com/api_india", {
        "method": "GET",
        "headers": {
            "x-rapidapi-key": "30783a336emsh8f107ac4963783dp12931fjsn8dbc83f14b62",
            "x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com"
        }
    }).then(response => {
        return response.json();
    }).then((data) => {
        let arr = data['state_wise']
        indiaData = arr;
        let table = document.getElementById('indiantotaldata')
        let rowtotal = table.insertRow(-1)
        let total = rowtotal.insertCell(0)
        let activetotal = rowtotal.insertCell(1)
        let confirmedtotal = rowtotal.insertCell(2)
        let Deathstotal = rowtotal.insertCell(3)
        let nctotal = rowtotal.insertCell(4)
        let ndtotal = rowtotal.insertCell(5)
        let nrtotal = rowtotal.insertCell(6)
        let Recoveredtotal = rowtotal.insertCell(7)
        total.innerHTML = 'Total'
        activetotal.innerHTML = data['total_values'].active
        confirmedtotal.innerHTML = data['total_values'].confirmed
        Deathstotal.innerHTML = data['total_values'].deaths
        nctotal.innerHTML = data['total_values'].deltaconfirmed
        ndtotal.innerHTML = data['total_values'].deltadeaths
        nrtotal.innerHTML = data['total_values'].deltarecovered
        Recoveredtotal.innerHTML = data['total_values'].recovered


        for (let i in arr) {
            let table = document.getElementById('indiandata');
            let row = table.insertRow(-1);
            let state = row.insertCell(0)
            let active = row.insertCell(1)
            let confirmed = row.insertCell(2)
            let Deaths = row.insertCell(3)
            let nc = row.insertCell(4)
            let nd = row.insertCell(5)
            let nr = row.insertCell(6)
            let Recovered = row.insertCell(7)
            if (arr[i].state != 'State Unassigned') {
                state.innerHTML = arr[i].state
                active.innerHTML = arr[i].active
                confirmed.innerHTML = arr[i].confirmed
                Deaths.innerHTML = arr[i].deaths
                nc.innerHTML = arr[i].deltaconfirmed
                nd.innerHTML = arr[i].deltadeaths
                nr.innerHTML = arr[i].deltarecovered
                Recovered.innerHTML = arr[i].recovered
            }
        }
    })
}
getIndiaData();
//Getting the values of latitude and longitude of our current location
const successCallback = (position) => {
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;
    reverseGeocoding(latitude, longitude)//calling reverseGeoding function
}
const errorCallback = (error) => {
    alert(error);
}
navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
//this function takes latitude and longitude as parameter and requests the api to get our current location 
function reverseGeocoding(latitude, longitude) {
    fetch(`https://us1.locationiq.com/v1/reverse.php?key=pk.0ff7930fdd8dc25309db2103845557f9&lat=${latitude}&lon=${longitude}&format=json`)
        .then(res => res.json())
        .then(response => {
            let locah1 = document.getElementById('locationh1')
            let locacont = document.getElementById('locationcont')
            let lostate = document.getElementById('locationstate')
            let locadist = document.getElementById('locationdist')
            let locationbg = document.getElementById('yourlocation')
            let districtalert = document.getElementById('districtalert')
            locah1.innerHTML = 'Your Current Location is: '
            locacont.innerHTML = 'Country: ' + response.address.country
            lostate.innerHTML = 'State: ' + response.address.state
            locadist.innerHTML = 'District: ' + response.address.state_district
            locationbg.style.opacity = 1;
            locah1.style.opacity = 1;
            locacont.style.opacity = 1;
            lostate.style.opacity = 1;
            locadist.style.opacity = 1;
            let locabox = document.getElementById('locationcoviddata')
            let locadata1 = document.getElementById('locationcoviddata1')
            let locadata2 = document.getElementById('locationcoviddata2')
            let locadata3 = document.getElementById('locationcoviddata3')
            let locadata4 = document.getElementById('locationcoviddata4')
            let locadata5 = document.getElementById('locationcoviddata5')
            let locadata6 = document.getElementById('locationcoviddata6')
            let locadata7 = document.getElementById('locationcoviddata7')
            let locadata8 = document.getElementById('locationcoviddata8')
            locabox.style.opacity = 1;
            locadata1.innerHTML = response.address.state_district
            locadata2.innerHTML = "Active Cases: " + indiaData[response.address.state].district[response.address.state_district].active
            locadata3.innerHTML = "Total Confirmed: " + indiaData[response.address.state].district[response.address.state_district].confirmed
            locadata4.innerHTML = "Total Deaths: " + indiaData[response.address.state].district[response.address.state_district].deceased
            locadata5.innerHTML = "Total Recovered: " + indiaData[response.address.state].district[response.address.state_district].recovered
            locadata6.innerHTML = "New Confirmed: " + indiaData[response.address.state].district[response.address.state_district].delta.confirmed
            locadata7.innerHTML = "New Deaths: " + indiaData[response.address.state].district[response.address.state_district].delta.deceased
            locadata8.innerHTML = "New Recovered: " + indiaData[response.address.state].district[response.address.state_district].delta.recovered
            if (indiaData[response.address.state].district[response.address.state_district].active > 1000) {
                districtalert.innerHTML = 'You are in HIGH Risk zone';
                districtalert.style.backgroundColor = 'red';
            }
            else if (indiaData[response.address.state].district[response.address.state_district].active > 500) {
                districtalert.innerHTML = 'You are in MODERATE Risk zone';
                districtalert.style.backgroundColor = 'orange';
            }
            else {
                districtalert.innerHTML = 'You are in LOW Risk zone';
                districtalert.style.backgroundColor = 'green';
            }
        })
}




