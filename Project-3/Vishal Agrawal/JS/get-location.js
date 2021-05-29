$(document).ready(function() {
    function getLocation() {
        if (navigator.geolocation) {
            console.log("Successfully fetch location");
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {
        let latitude = position.coords.latitude;
        let longitude = position.coords.longitude;
        getReadableLocation(latitude, longitude)
    }

    function getReadableLocation(latitude, longitude) {
        let country = "India";
        let state = "Delhi";
        if (config.usingUserLocation) {
            let endPointUrl = "https://us1.locationiq.com";
            const APIKey = config.LOCATIONQ_KEY;
            let link = `${endPointUrl}/v1/reverse.php?key=${APIKey}&lat=${latitude}&lon=${longitude}&format=json`;
            const settings = {
                "async": true,
                "crossDomain": true,
                "url": link,
                "method": "GET"
            };

            $.ajax(settings).done(function(response) {
                console.log(response);
                $(`.location-data > div > div > div > .district > .value`).text(" " + response["address"]["state_district"]);
                $(`.location-data > div > div > div > .state > .value`).text(" " + response["address"]["state"]);
                $(`.location-data > div > div > div > .country > .value`).text(" " + response["address"]["country"]);
                country = response["address"]["country"];
                state = response["address"]["state"];
                locationFound(country, state);
            });
        } else {
            locationFound(country, state);
        }

        function locationFound(country, state) {
            if (config.usingCovidAPIForUserLocation) {
                let debug = config.correctnessFactor;
                let today = new Date();
                let day = Number(String(today.getDate()).padStart(2, '0')) - debug;
                let month = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
                let year = today.getFullYear();
                let api_date = `${year}-${month}-${day}`;
                let api_url = `https://covid-19-statistics.p.rapidapi.com/reports?date=${api_date}&region_name=${country}`;
                console.log(api_url);
                const settings = {
                    "async": true,
                    "crossDomain": true,
                    "url": api_url,
                    "method": "GET",
                    "headers": {
                        "x-rapidapi-key": config.RAPIDAPI_KEY,
                        "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"
                    }
                };

                function get_comma_number(number) {
                    num_str = String(number);
                    let ans = "";
                    for (let index = 0; index < num_str.length; index++) {
                        if (index % 3 == 0 && index != 0) {
                            ans = ", " + ans;
                        }
                        ans = num_str[num_str.length - 1 - index] + ans;
                    }
                    return ans;
                }

                function displayData(deaths, recovered, confirmed, active, type) {
                    $(`.${type}-data > div > .total > .value`).text(" " + get_comma_number(confirmed));
                    $(`.${type}-data > div > .active > .value`).text(" " + get_comma_number(active));
                    $(`.${type}-data > div > .recovered > .value`).text(" " + get_comma_number(recovered));
                    $(`.${type}-data > div > .deaths > .value`).text(" " + get_comma_number(deaths));
                }

                function handleUserStateData(response) {
                    $(".state-data > div > .topic > .value").text(`${state}'s Data`);
                    displayData(response["deaths"], response["recovered"], response["confirmed"], response["active"], "state");
                }

                $.ajax(settings).done(function(response) {
                    // console.log(response);
                    let country_deaths = 0;
                    let country_recovered = 0;
                    let country_confirmed = 0;
                    let country_active = 0;
                    for (state_data of response["data"]) {
                        // console.log(state_data);
                        country_deaths += state_data["deaths"];
                        country_recovered += state_data["recovered"];
                        country_confirmed += state_data["confirmed"];
                        country_active += state_data["active"];
                        if (state_data["region"]["province"] == state) {
                            handleUserStateData(state_data);
                        }
                    }
                    $(".country-data > div > .topic > .value").text(`${country}'s Data`);
                    displayData(country_deaths, country_recovered, country_confirmed, country_active, "country");
                    $(".covid-data").removeClass("hidden");
                });
            }
        }
    }

    getLocation();
});