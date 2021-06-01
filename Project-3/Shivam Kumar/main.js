const country = document.querySelector("#country");
const statesList = document.querySelector("#state");
const inputCountry = document.querySelector(".input--country");
const inputState = document.querySelector(".input--state");
const loader = document.querySelector(".load");

const num = new Intl.NumberFormat("en-US");

let slugValue = "india";
let userState,
	stateName = "Maharashtra";

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

async function populateStateList(slug = "india") {
	loader.classList.add("loading-screen");
	const stateSearch = document.querySelector(".state-search");
	clearElement(statesList);

	const response = await fetch(`https://api.covid19api.com/live/country/${slug}
	`);
	const data = await response.json();
	let states = [];
	for (let state of data) {
		if (!states.includes(state.Province)) {
			states.push(state.Province);
		}
	}
	states.sort();

	if (states.length === 1) {
		stateSearch.classList.add("no-states");
	} else if (stateSearch.classList.contains("no-states")) {
		stateSearch.classList.remove("no-states");
	}

	for (let state of states) {
		const stateNode = document.createElement("OPTION");
		stateNode.setAttribute("value", state);
		statesList.appendChild(stateNode);
	}

	loader.classList.remove("loading-screen");
}

function dataRepresentation(data, mod) {
	document.querySelector(
		`.total_cases${mod}`
	).innerHTML = `<span class="info__title">Confirmed</span><span class="info__data">${num.format(
		data.TotalConfirmed
	)}</span><span class="new_cases info__subtitle"><i class='fa fas fa-angle-double-up'></i> ${num.format(
		data.NewConfirmed
	)}</span>`;
	document.querySelector(
		`.total_recovered${mod}`
	).innerHTML = `<span class="info__title">Recovered</span><span class="info__data">${num.format(
		data.TotalRecovered
	)}</span><span class="new_recovered info__subtitle"><i class='fa fas fa-angle-double-up'></i> ${num.format(
		data.NewRecovered
	)}</span>`;

	let sign;
	let av = data.NewConfirmed - data.NewRecovered - data.NewDeaths;
	if (av < 0) {
		sign = "down";
		av = -av;
	} else sign = "up";

	document.querySelector(
		`.total_active${mod}`
	).innerHTML = `<span class="info__title">Active</span><span class="info__data">${num.format(
		data.TotalConfirmed - data.TotalRecovered - data.TotalDeaths
	)}</span><span class="new_active info__subtitle"><i class='fa fas fa-angle-double-${sign}'></i> ${num.format(
		av
	)}</span>`;

	document.querySelector(
		`.total_deaths${mod}`
	).innerHTML = `<span class="info__title">Deaths</span><span class="info__data">${num.format(
		data.TotalDeaths
	)}</span><span class="new_deaths info__subtitle"><i class='fa fas fa-angle-double-up'></i> ${num.format(
		data.NewDeaths
	)}</span>`;
}

function dataRepresentationStates(data, mod) {
	document.querySelector(
		`.total_cases${mod}`
	).innerHTML = `<span class="info__title">Confirmed</span><span class="info__data">${num.format(
		data.Confirmed
	)}</span>`;
	document.querySelector(
		`.total_recovered${mod}`
	).innerHTML = `<span class="info__title">Recovered</span><span class="info__data">${num.format(
		data.Recovered
	)}</span>`;

	document.querySelector(
		`.total_active${mod}`
	).innerHTML = `<span class="info__title">Active</span><span class="info__data">${num.format(
		data.Active
	)}</span>`;

	document.querySelector(
		`.total_deaths${mod}`
	).innerHTML = `<span class="info__title">Deaths</span><span class="info__data">${num.format(
		data.Deaths
	)}</span>`;
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

let counter = 0;

async function populateStateSearchData(slug = "india", state = "Maharashtra") {
	const response = await fetch(
		`https://api.covid19api.com/live/country/${slug}`
	);
	const data = await response.json();
	const stateData = data.filter(
		(element) => element.Province.toLowerCase() === state.toLowerCase()
	);

	dataRepresentationStates(stateData[stateData.length - 1], "SS");
	if (counter) {
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
	} else counter = 1;
}

async function populateStatesData() {
	const response = await fetch("https://api.covid19api.com/live/country/india");
	const data = await response.json();
	const stateData = data.filter(
		(element) => element.Province.toLowerCase() === userState.toLowerCase()
	);

	dataRepresentationStates(stateData[stateData.length - 1], "S");

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
}

async function plotCountryData(dataToGraph = "Confirmed", slug = "india") {
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
}

async function plotStatesData(
	dataToGraph = "Confirmed",
	slug,
	slugCountry,
	plotin
) {
	let date = [];
	let ylable = [];
	let label;
	let color, bgcolor;

	const response = await fetch(
		`https://api.covid19api.com/live/country/${slugCountry}`
	);
	const data = await response.json();
	const stateData = data.filter((element) => element.Province === slug);

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

	plot(date, ylable, label, color, bgcolor, plotin);
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

async function plotGraphs(query1, query2) {
	loader.classList.add("loading-screen");
	await plotGlobalData(query1);
	await plotCountryData(query2, slugValue);
	await plotStatesData(query2, userState, slugValue, "states-chart");
	await plotStatesData(query2, stateName, slugValue, "states-search-chart");
	loader.classList.remove("loading-screen");
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
	userState = data.address.state;
	document.querySelector(".states-name").innerHTML = userState;

	await populateStatesData(userState);
	plotStatesData("Confirmed", userState, "india", "states-chart");
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

const execute = async () => {
	populateCountry();
	populateGlobalData();
	plotGlobalData();
	populateCountryData();
	plotCountryData();
	populateStateList();
	populateStateSearchData();
	plotStatesData("Confirmed", "Maharashtra", slugValue, "states-search-chart");
};

execute();

// Event Listeners

this.addEventListener("load", () => {
	setTimeout(() => {
		document.querySelector(".load").classList.remove("loading-screen");
		document.querySelector(".load").classList.remove("load-start-bg");
	}, 2000);
});

document.querySelector(".search-btn").addEventListener("click", async () => {
	let allCountry = [];

	document.querySelectorAll("#country option").forEach((ele) => {
		allCountry.push(ele.getAttribute("value"));
	});

	if (allCountry.includes(inputCountry.value)) {
		loader.classList.add("loading-screen");

		document.querySelector(".country-name").innerHTML = inputCountry.value;
		populateCountryData(inputCountry.value);
		slugValue = await obtainSlug(inputCountry.value);
		plotCountryData("Confirmed", slugValue);

		populateStateList(slugValue);
		loader.classList.remove("loading-screen");
	} else {
		alert("Enter a valid country name or choose from the dropdown");
	}
});

document.querySelector(".track-btn").addEventListener("click", async () => {
	loader.classList.add("loading-screen");

	document.querySelector(".states_section").style.display = "flex";
	await getlocation();
	loader.classList.remove("loading-screen");
});

document
	.querySelector(".state-search-btn")
	.addEventListener("click", async () => {
		const inputStateVal = document.querySelector(".input--state");
		stateName = inputStateVal.value;

		let allStates = [];

		document.querySelectorAll("#state option").forEach((ele) => {
			allStates.push(ele.getAttribute("value"));
		});

		if (allStates.includes(stateName)) {
			loader.classList.add("loading-screen");
			document.querySelector(".states-search-name").innerHTML = stateName;

			await populateStateSearchData(slugValue, stateName);
			await plotStatesData(
				"Confirmed",
				stateName,
				slugValue,
				"states-search-chart"
			);
			loader.classList.remove("loading-screen");
		} else {
			alert("Enter a valid state name or else choose from the dropdown");
		}
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
