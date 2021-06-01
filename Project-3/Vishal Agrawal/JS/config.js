const config = {
    // API KEYS
    LOCATIONQ_KEY: "pk.9587e5a9c076086b5d92503bf93bb61d",
    RAPIDAPI_KEY: "8aeeb6037dmshd23a7de6e8336d9p14b8b9jsna4b9590b12c0",

    // Correctness Factor
    // The number of day before the current day for which data is needed
    // It is used for removing and testing anybugs in API
    // Recommened value >= 1 because of the Second covid API
    // First API used for world stats is live (no correctness Factor needed).
    correctnessFactor: 2,

    // Development Variables do not alter if you only want to test the site
    usingWorldStatsAPI: 1,
    usingUserLocation: 1,
    usingCovidAPIForUserLocation: 1,
    usingCovidAPIForSearchedLocation: 1,

    // Generator Variable, most probably you don't need to change it
    // It will launch 250 API calls with the help of which I made the
    // dropdown for search location section
    // all the data which will be generated is already stored in data.json 
    runGenerator: 0,
}