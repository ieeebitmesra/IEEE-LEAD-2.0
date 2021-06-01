$(document).ready(function () {
    let debug = config.correctnessFactor;
    if (config.usingWorldStatsAPI) {
        console.log("Retrieving World Data");
        // getting current date for api call
        let today = new Date();
        today.setDate(today.getDate() - debug);
        let day = String(Number(String(today.getDate()))).padStart(2, '0');
        let month = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        let year = today.getFullYear();
        let api_date = `${year}-${month}-${day}`;
        // console.log(api_date);
        const api_key = config.RAPIDAPI_KEY;
        let link = "https://covid-193.p.rapidapi.com/history?country=all&day=" + api_date;
        console.log(`Retrieving info for date: ${api_date}`);

        const settings = {
            "async": true,
            "crossDomain": true,
            "url": link,
            "method": "GET",
            "headers": {
                "x-rapidapi-key": api_key,
                "x-rapidapi-host": "covid-193.p.rapidapi.com"
            }
        };

        $.ajax(settings).done(function (response) {
            console.log("API Response Received");
            console.log(response.response);
            let data_outer_array = response.response;

            let cases_data = data_outer_array[0]["cases"];
            let deaths_data = data_outer_array[0]["deaths"];

            // Overall Data
            let total_cases = Number(cases_data["total"]);
            let total_deaths = Number(deaths_data["total"]);
            let total_recovered = Number(cases_data["recovered"]);
            let total_active_cases = Number(cases_data["active"]);

            let len1 = data_outer_array[0]["deaths"]["new"].length;
            let len2 = data_outer_array[0]["cases"]["new"].length;
            let deaths_today = Number(data_outer_array[0]["deaths"]["new"].substring(1, len1));
            let cases_today = Number(data_outer_array[0]["cases"]["new"].substring(1, len2));
            // console.log(deaths_today);
            // console.log(cases_today);

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

            $(`.world-data > div > .total > .value`).text(" " + get_comma_number(total_cases));
            $(`.world-data > div > .active > .value`).text(" " + get_comma_number(total_active_cases));
            $(`.world-data > div > .recovered > .value`).text(" " + get_comma_number(total_recovered));
            $(`.world-data > div > .deaths > .value`).text(" " + get_comma_number(total_deaths));
            $(`.world-data > div > .new-cases > .value`).text(" " + get_comma_number(cases_today));
            $(`.world-data > div > .new-deaths > .value`).text(" " + get_comma_number(deaths_today));
        });
    }
});