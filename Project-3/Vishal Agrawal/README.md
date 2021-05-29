# Covid Statistics

## Introduction

This project is a static site with the following features:-

1. Live covid statistics of the whole world
2. Covid statistics based on user location (country and state both).
3. Covid statistics of any particular Country and State.

## APIs Used
1. https://rapidapi.com/api-sports/api/covid-193
2. https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics
3. https://locationiq.com/geocoding (reverse geocoding)

## User Guide
As this is a static site (client-side), we can't provide the API key.

To use the website, you need two API keys
1. RapidAPI key
2. LocationIQ key

After getting both the keys,

cd into the JS directory, 

rename config-template.js to config.js (using the command `mv config-template.js config.js` in the JS directory), 

then enter your keys in the respective variables.

You are ready to use the site now!

## Extra Info
1. Covid-19-statistics API has a latency of 1s, so segments might take time to load
2. Covid-19-statistics API doesn't instantly update their data, so the data displayed in the second and third sections is two days older than the current date.
