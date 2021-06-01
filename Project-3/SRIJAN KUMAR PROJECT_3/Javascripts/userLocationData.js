function getLocation() {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {

            //Firstly we fetch the latitude and longitude
            //with the help of getCurrentPosition() function   

            latitude0 = position.coords.latitude;
            longitude0 = position.coords.longitude;

            //This function converts the user coordinates 
            //into human readable address using the Opencage API  
            const getAddress = async () => {

                const response = await fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude0}+${longitude0}&key=1f8aaebee43341eaa98a2011cfae34bc`);

                if (response.status !== 200) {
                    throw new Error('cannot fetch data');
                }

                const data = await response.json();


                return data;


            };


            getAddress()
                .then((data) => {
                    //The human readable address is then used to get
                    //the covid data using the covid19api

                    myCountry = data.results[0].components.country;
                    myState = data.results[0].components.state;


                    //The myAddress box in the webPage
                    //is updated with the address we got

                    let x0 = document.querySelector(".myAddress");
                    x0.innerText =
                        `

Latitude  : ${latitude0}

Longitude : ${longitude0}

District  : ${data.results[0].components.state_district}

State     : ${data.results[0].components.state}

Country   : ${data.results[0].components.country}

`

                    //This function returns the covid data 
                    //of country of User( Actually it returns Promise :) )
                    const getCovidData = async () => {

                        let url = `https://api.covid19api.com/live/country/${myCountry}`;
                        const response = await fetch(url);


                        if (response.status !== 200) {
                            throw new Error('cannot fetch data');
                        }

                        const data = await response.json();


                        return data;


                    };

                    getCovidData()
                        .then((data) => {
                            console.log(data);

                            //The covid data we got is of country,
                            //now we will search the user's State/Province in
                            //this huge data of country                         

                            let i;
                            let arr = [];
                            let j = 0;
                            for (i = data.length - 1; j !== 2; i--) {

                                if (data[i].Province === myState) {
                                    arr[j] = data[i];
                                    j += 1;
                                }

                            }

                            console.log(arr[0]);
                            console.log(arr[1]);

                            final = arr[0];
                            init = arr[1];
                            //The final array is the Province Covid Data of
                            //last updated day and the init array is the
                            //Province Covid Data of second last updated day.
                            //So difference of final and init data will give us
                            //the data of newest day.

                            //The useful data is then
                            //fed in our wesite by targeting
                            //respective divs
                            let x = final.Deaths;
                            let y = document.querySelector(".totDeathNum");
                            y.innerText = `${x}`;

                            x = final.Confirmed;
                            y = document.querySelector(".totConfNum");
                            y.innerText = `${x}`;

                            x = final.Recovered;
                            y = document.querySelector(".totRecNum");
                            y.innerText = `${x}`;

                            x = final.Deaths - init.Deaths;
                            y = document.querySelector(".newDeathNum");
                            y.innerText = `${x}`;

                            x = final.Recovered - init.Recovered;
                            y = document.querySelector(".newRecNum");
                            y.innerText = `${x}`;

                            x = final.Confirmed - init.Confirmed;
                            y = document.querySelector(".newConfNum");
                            y.innerText = `${x}`;

                        })
                        .catch(err => console.log('rejected :', err.message));
                })
                .catch(err => console.log('rejected :', err.message));

        });


    }

}


//This function checks if user allows
//us the access to its location and then
//print the result accordingly on our webpage. 
navigator.geolocation.watchPosition(function (position) {

    document.querySelector("#myh3").innerText = "Covid Data of the above State";

},
    function (error) {

        if (error.code == error.PERMISSION_DENIED) {

            document.querySelector("#myh3").innerText = "User Denied Geolocation";

        }
    });

//We declare the variables globally
//for their accessibility over the
//whole code.

let latitude0;
let longitude0;
let myCountry;
let myState;

// getLocation() function called
getLocation();

