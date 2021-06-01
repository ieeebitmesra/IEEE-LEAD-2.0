console.log("Generator Starts");
if (config.runGenerator) {
    console.log("runGenerator is True");
    $(document).ready(function() {
        const settings = {
            "async": true,
            "crossDomain": true,
            "url": "https://covid-19-statistics.p.rapidapi.com/regions",
            "method": "GET",
            "headers": {
                "x-rapidapi-key": config.RAPIDAPI_KEY,
                "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"
            }
        };

        async function getStates(country_iso) {
            country_states = {};
            for (const country in country_iso) {
                console.log(country);
                let url = `https://covid-19-statistics.p.rapidapi.com/provinces?iso=${country_iso[country]}`;
                console.log(url);
                country_states[country] = [];
                const settings = {
                    "async": true,
                    "crossDomain": true,
                    "url": url,
                    "method": "GET",
                    "headers": {
                        "x-rapidapi-key": config.RAPIDAPI_KEY,
                        "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"
                    }
                };

                $.ajax(settings).done(function(response) {
                    console.log(response);
                    for (const state of response["data"]) {
                        country_states[country].push(state["province"]);
                    }
                });

                function sleep(ms) {
                    return new Promise(resolve => setTimeout(resolve, ms));
                }

                // preventing more than 250+ API calls at once
                await sleep(1000);
            }
            await sleep(100 * 60 * 10);
            let dataJSON = JSON.stringify(country_states);
            let json_div = $("<div></div>").text(dataJSON);
            $("body").append(json_div);
        }

        $.ajax(settings).done(function(response) {
            country_iso = {};
            // console.log(response);
            for (let country of response["data"]) {
                country_iso[`${country["name"]}`] = country["iso"];
            }
            // console.log("Retrieved ISOs");
            console.log(country_iso);
            getStates(country_iso);
        });
    });
}