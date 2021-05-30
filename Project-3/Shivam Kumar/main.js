const country = document.querySelector("#country");
const states = document.querySelector("#states");
const inputCountry = document.querySelector(".input--country");
const inputState = document.querySelector(".input--states");
const labelStates = document.querySelector(".label--states");
const loader = document.querySelector(".load");

let slugValue = "india";
let stateName;

function menu() {
	const menubar = document.querySelector(".menubar");
	const sideMenu = document.querySelector(".navbar__items");

	menubar.addEventListener("click", () => {
		menubar.classList.toggle("menubar--activate");
		sideMenu.classList.toggle("navbar__items--activate");
	});
}

menu();

function convertDate(date) {
	return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
}

async function dataSummary() {
	// API for fetching world data
	const response = await fetch("https://api.covid19api.com/summary");
	const values = await response.json();
	return values;
}

async function obtainSlug(country = "India") {
	const response = await dataSummary();
	countryArr = response.Countries;
	let slugIndex = countryArr.findIndex(
		(element) => element.Country.toLowerCase() === country.toLowerCase()
	);
	document.querySelector(".country-name").innerHTML =
		countryArr[slugIndex].Country;
	return countryArr[slugIndex].Slug;
}
// Search functions

async function populateCountry() {
	// Populating country names
	const data = await dataSummary();

	for (let countryVar of data.Countries) {
		const countryNode = document.createElement("OPTION");
		countryNode.setAttribute("value", countryVar.Country);
		country.appendChild(countryNode);
	}
}

function dataRepresentation(data, mod) {
	document.querySelector(
		`.total_cases${mod}`
	).innerHTML = `<span class="info__title">Confirmed</span><span class="info__data">${data.TotalConfirmed}</span><span class="new_cases info__subtitle"><i class='fa fas fa-angle-double-up'></i> ${data.NewConfirmed}</span>`;
	document.querySelector(
		`.total_recovered${mod}`
	).innerHTML = `<span class="info__title">Recovered</span><span class="info__data">${data.TotalRecovered}</span><span class="new_recovered info__subtitle"><i class='fa fas fa-angle-double-up'></i> ${data.NewRecovered}</span>`;

	let sign;
	let av = data.NewConfirmed - data.NewRecovered;
	if (av < 0) {
		sign = "down";
		av = -av;
	} else sign = "up";

	document.querySelector(
		`.total_active${mod}`
	).innerHTML = `<span class="info__title">Active</span><span class="info__data">${
		data.TotalConfirmed - data.TotalRecovered
	}</span><span class="new_active info__subtitle"><i class='fa fas fa-angle-double-${sign}'></i> ${av}</span>`;

	document.querySelector(
		`.total_deaths${mod}`
	).innerHTML = `<span class="info__title">Deaths</span><span class="info__data">${data.TotalDeaths}</span><span class="new_deaths info__subtitle"><i class='fa fas fa-angle-double-up'></i> ${data.NewDeaths}</span>`;
}

function dataRepresentationStates(data, mod) {
	document.querySelector(
		`.total_cases${mod}`
	).innerHTML = `<span class="info__title">Confirmed</span><span class="info__data">${data.Confirmed}</span>`;
	document.querySelector(
		`.total_recovered${mod}`
	).innerHTML = `<span class="info__title">Recovered</span><span class="info__data">${data.Recovered}</span>`;

	document.querySelector(
		`.total_active${mod}`
	).innerHTML = `<span class="info__title">Active</span><span class="info__data">${data.Active}</span>`;

	document.querySelector(
		`.total_deaths${mod}`
	).innerHTML = `<span class="info__title">Deaths</span><span class="info__data">${data.Deaths}</span>`;
}

function clearElement(element) {
	while (element.firstChild) {
		element.removeChild(element.firstChild);
	}
}

async function populateGlobalData() {
	// Populating global data

	const global_today_response = await dataSummary();
	const global_today = global_today_response.Global;

	dataRepresentation(global_today, "G");
	// loader.classList.remove('loading-screen')
}

async function populateCountryData(input = "India") {
	// Retirieve details of per country
	const response = await dataSummary();
	let countries = response.Countries;
	let data;

	for (let country of countries) {
		if (country.Country === input) {
			data = country;
		}
	}

	dataRepresentation(data, "C");
}

async function populateStatesData() {
	loader.classList.add("loading-screen");

	const response = await fetch("https://api.covid19api.com/live/country/india");
	const data = await response.json();
	const stateData = data.filter(
		(element) => element.Province.toLowerCase() === stateName.toLowerCase()
	);

	dataRepresentationStates(stateData[stateData.length - 1], "S");
	loader.classList.remove("loading-screen");

	let active = stateData[stateData.length - 1].Active;

	if (active > 15000) {
		document
			.querySelector(".alert-window-container")
			.classList.add("alert-window--activate");
		document.querySelector(".high").classList.add("red");
	} else if (active <= 15000 && active > 1000) {
		document
			.querySelector(".alert-window-container")
			.classList.add("alert-window--activate");
		document.querySelector(".mod").classList.add("yellow");
	} else if (active <= 1000) {
		document
			.querySelector(".alert-window-container")
			.classList.add("alert-window--activate");
		document.querySelector(".low").classList.add("green");
	}
}

// Plotting Graphs

async function plotGlobalData(dataToGraph = "TotalConfirmed") {
	loader.classList.add("loading-screen");

	let date = [];
	let ylable = [];
	let label;
	let color, bgcolor;

	const globalResponse = await fetch(`https://api.covid19api.com/world`);
	const globalData = await globalResponse.json();

	globalData.sort((a, b) => (a.TotalConfirmed > b.TotalConfirmed ? 1 : -1));

	for (let values of globalData) {
		let dateToPush = values.Date.substr(0, 10);
		date.push(dateToPush);

		if (dataToGraph === "active") {
			ylable.push(values.TotalConfirmed - values.TotalRecovered);
		} else ylable.push(values[dataToGraph]);
	}

	if (dataToGraph === "TotalConfirmed") {
		label = "Confirmed Cases";
		color = "#64b9f5";
		bgcolor = "#bce3ff";
	}

	if (dataToGraph === "TotalRecovered") {
		label = "Total Recovered";
		color = "#86f093";
		bgcolor = "#cef1d1";
	}
	if (dataToGraph === "TotalDeaths") {
		label = "Deaths";
		color = "#ff8a8a";
		bgcolor = "#f7dddd";
	}
	if (dataToGraph === "active") {
		label = "Active Cases";
		color = "#f7b879";
		bgcolor = "#f9fab7";
	}

	plot(date, ylable, label, color, bgcolor, "global-chart");

	loader.classList.remove("loading-screen");
}

async function plotCountryData(dataToGraph = "Confirmed", slug = "india") {
	loader.classList.add("loading-screen");

	let date = [];
	let ylable = [];
	let label;
	let color, bgcolor;

	const globalResponse =
		await fetch(`https://api.covid19api.com/total/country/${slug}
	`);
	const globalData = await globalResponse.json();

	globalData.sort((a, b) => (a.Confirmed > b.Confirmed ? 1 : -1));

	for (let values of globalData) {
		let dateToPush = values.Date.substr(0, 10);
		date.push(dateToPush);
		ylable.push(values[dataToGraph]);
	}

	if (dataToGraph === "Confirmed") {
		label = "Confirmed Cases";
		color = "#64b9f5";
		bgcolor = "#bce3ff";
	}

	if (dataToGraph === "Recovered") {
		label = "Total Recovered";
		color = "#86f093";
		bgcolor = "#cef1d1";
	}
	if (dataToGraph === "Deaths") {
		label = "Deaths";
		color = "#ff8a8a";
		bgcolor = "#f7dddd";
	}
	if (dataToGraph === "Active") {
		label = "Active Cases";
		color = "#f7b879";
		bgcolor = "#f9fab7";
	}

	plot(date, ylable, label, color, bgcolor, "country-chart");

	loader.classList.remove("loading-screen");
}

async function plotStatesData(dataToGraph = "Confirmed") {
	loader.classList.add("loading-screen");

	let date = [];
	let ylable = [];
	let label;
	let color, bgcolor;

	const response = await fetch("https://api.covid19api.com/live/country/india");
	const data = await response.json();
	const stateData = data.filter(
		(element) => element.Province.toLowerCase() === stateName.toLowerCase()
	);

	for (let values of stateData) {
		let dateToPush = values.Date.substr(0, 10);
		date.push(dateToPush);
		ylable.push(values[dataToGraph]);
	}

	if (dataToGraph === "Confirmed") {
		label = "Confirmed Cases";
		color = "#64b9f5";
		bgcolor = "#bce3ff";
	}

	if (dataToGraph === "Recovered") {
		label = "Total Recovered";
		color = "#86f093";
		bgcolor = "#cef1d1";
	}
	if (dataToGraph === "Deaths") {
		label = "Deaths";
		color = "#ff8a8a";
		bgcolor = "#f7dddd";
	}
	if (dataToGraph === "Active") {
		label = "Active Cases";
		color = "#f7b879";
		bgcolor = "#f9fab7";
	}

	plot(date, ylable, label, color, bgcolor, "states-chart");

	loader.classList.remove("loading-screen");
}

async function check() {
	const res = await fetch("https://api.covid19api.com/live/country/india");
	const data = await res.json();
	console.log(data);
}

function plot(xdata, ydata, label, color, bgcolor, chartContainer) {
	document.querySelector(
		`.${chartContainer}-container`
	).innerHTML = `<canvas id="${chartContainer}"></canvas>`;
	let chart = document.getElementById(chartContainer).getContext("2d");
	let chartDetails = new Chart(chart, {
		type: "line",
		data: {
			labels: xdata,
			datasets: [
				{
					label: label,
					data: ydata,
					backgroundColor: bgcolor,
					pointRadius: 0,
					borderColor: color,
					borderWidth: 2.502,
					pointHoverRadius: 6,
					fill: true,
				},
			],
		},
		options: {
			maintainAspectRatio: false,
		},
	});
}

// Graph Call functions

const graphConfirm = document.querySelectorAll(".graph-confirm");
const graphRecover = document.querySelectorAll(".graph-recover");
const graphDeaths = document.querySelectorAll(".graph-deaths");
const graphActive = document.querySelectorAll(".graph-active");

function plotGraphs(query1, query2) {
	plotGlobalData(query1);
	plotCountryData(query2, slugValue);
	plotStatesData(query2);
}

graphConfirm.forEach((e) =>
	e.addEventListener("click", () => {
		plotGraphs("TotalConfirmed", "Confirmed");
	})
);

graphRecover.forEach((e) =>
	e.addEventListener("click", () => {
		plotGraphs("TotalRecovered", "Recovered");
	})
);

graphDeaths.forEach((e) =>
	e.addEventListener("click", () => {
		plotGraphs("TotalDeaths", "Deaths");
	})
);

graphActive.forEach((e) =>
	e.addEventListener("click", () => {
		plotGraphs("active", "Active");
	})
);

// Locating user

async function reverseGeolocate(lat, long) {
	const response = await fetch(
		`https://us1.locationiq.com/v1/reverse.php?key=pk.bd651782037379ea23256b9c4260f77c&lat=${lat}&lon=${long}&format=json
		`
	);
	const data = await response.json();
	stateName = data.address.state;
	document.querySelector(".states-name").innerHTML = stateName;

	await populateStatesData(stateName);
	plotStatesData();
}

function getlocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition((position) => {
			reverseGeolocate(position.coords.latitude, position.coords.longitude);
		});
	} else {
		alert(
			"Your browser doesn't support geolocation or has been disabled by the user."
		);
	}
}

//  Execute at Startup

const execute = () => {
	populateCountry();
	populateGlobalData();
	plotGlobalData();
	populateCountryData();
	plotCountryData();
};

execute();

// Event Listeners

this.addEventListener("load", () => {
	document.querySelector(".heading").classList.add("animateOnLoad");
	document.querySelector(".form_section").classList.add("animateOnLoad");
});

this.addEventListener("load", () => {
	setTimeout(() => {
		document.querySelector(".load").classList.remove("loading-screen");
		document.querySelector(".load").classList.remove("load-start-bg");
	}, 2000);
});

document.querySelector(".search-btn").addEventListener("click", async () => {
	populateCountryData(inputCountry.value);
	slugValue = await obtainSlug(inputCountry.value);
	plotCountryData("Confirmed", slugValue);
});

document.querySelector(".track-btn").addEventListener("click", () => {
	document.querySelector(".states_section").style.display = "flex";
	getlocation();
});

document.querySelectorAll(".close-alert").forEach((element) =>
	element.addEventListener("click", () => {
		document
			.querySelector(".alert-window-container")
			.classList.remove("alert-window--activate");
		const high = document.querySelector(".high");
		const mod = document.querySelector(".mod");
		const low = document.querySelector(".low");

		if (high.classList.contains("red")) {
			high.classList.remove("red");
		}
		if (mod.classList.contains("yellow")) {
			mod.classList.remove("yellow");
		}
		if (low.classList.contains("green")) {
			low.classList.remove("green");
		}
	})
);
