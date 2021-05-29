$(document).ready(function() {
    for (let country in country_drop_down) {
        if (country_drop_down[country].length == 0) {
            continue;
        }
        let country_options = $("<option></option>").attr("value", country).text(country);
        $(".country-menu").append(country_options);
    }

    $(".country-menu").change(function() {
        let choice = $(this);
        if (choice.val() === "Choose your country") {
            $(".state-menu").empty();
            let default_option = $("<option></option>").attr("value", "Choose your state").text("Choose your state");
            $(".state-menu").append(default_option);
            $(".state-menu").attr("disabled", '');
        } else {
            $(".state-menu").empty();
            let default_option = $("<option></option>").attr("value", "Choose your state").text("Choose your state");
            $(".state-menu").append(default_option);
            for (let state of country_drop_down[choice.val()]) {
                let state_options = $("<option></option>").attr("value", state).text(state);
                $(".state-menu").append(state_options);
            }
            $(".state-menu").removeAttr("disabled");
        }
    });

    function locationFound(country, state) {
        if (config.usingCovidAPIForSearchedLocation) {
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
                console.log(response);
                let country_deaths = 0;
                let country_recovered = 0;
                let country_confirmed = 0;
                let country_active = 0;
                for (state_data of response["data"]) {
                    console.log(state_data);
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

    $(".query").click(function() {
        if ($(".country-menu").val() == "Choose your country" || $(".state-menu").val() == "Choose your state") {
            $(".covid-data").addClass("hidden");
            alert("Please fill in country and state.");
        } else {
            locationFound($(".country-menu").val(), $(".state-menu").val());
        }
    });
});