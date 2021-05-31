fetch("https://corona-virus-world-and-india-data.p.rapidapi.com/api", {
	"method": "GET",
	"headers": {
		"x-rapidapi-key": "073d5d427bmsh66171dee6e5e823p106db8jsna035b2a3cec4",
		"x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com"
	}
})
.then(
	function(response_world){
		if (response_world.status !== 200) {
        console.log('Looks like there was a problem. Status Code: ' +
          response_world.status);
        return;
	}
	response_world.json().then(function(dataWorld) {
        // console.log(dataWorld);
        document.getElementById("country").innerHTML = dataWorld.countries_stat[0].country_name;
        document.getElementById("confirmed").innerHTML = dataWorld.countries_stat[0].cases;
        document.getElementById("active").innerHTML = dataWorld.countries_stat[0].active_cases;
        document.getElementById("recovered").innerHTML = dataWorld.countries_stat[0].total_recovered;
        document.getElementById("deaths").innerHTML = dataWorld.countries_stat[0].deaths;
        document.getElementById("alert").innerHTML = "High Risk";
        document.getElementById("alert").style.color = "red";
		const btn = document.getElementById("searchBtn");
        for(let i=0; i<dataWorld.countries_stat.length; i++) {
            let table = document.getElementById("stateTable");
		    let row = table.insertRow(-1);
		    let state = row.insertCell(0);
		    let confirmed = row.insertCell(1);
		    let active = row.insertCell(2);
		    let deaths = row.insertCell(3);
            let recovered = row.insertCell(4);

            state.innerHTML = dataWorld.countries_stat[i].country_name;
            confirmed.innerHTML = dataWorld.countries_stat[i].cases;
            active.innerHTML = dataWorld.countries_stat[i].active_cases;
            deaths.innerHTML = dataWorld.countries_stat[i].deaths;
            recovered.innerHTML = dataWorld.countries_stat[i].total_recovered;
            // console.log(dataWorld.countries_stat[i].recovered);
        }

        btn.onclick = function() {
            let search = document.getElementById("searchBox").value;
            // console.log(search);
            for(let i=0; i<dataWorld.countries_stat.length; i++){
                // console.log(dataWorld.countries_stat[i].country_name);
                if(dataWorld.countries_stat[i].country_name.toUpperCase() === search.toUpperCase()){
                    document.getElementById("country").innerHTML = dataWorld.countries_stat[i].country_name;
                    document.getElementById("confirmed").innerHTML = dataWorld.countries_stat[i].cases;
                    document.getElementById("active").innerHTML = dataWorld.countries_stat[i].active_cases;
                    document.getElementById("recovered").innerHTML = dataWorld.countries_stat[i].total_recovered;
                    document.getElementById("deaths").innerHTML = dataWorld.countries_stat[i].deaths;
                    console.log(i);
                    if(i<=20){
                        document.getElementById("alert").innerHTML = "High Risk";
                        document.getElementById("alert").style.color = "red";
                    } else if(i<=100){
                        document.getElementById("alert").innerHTML = "Moderate Risk";
                        document.getElementById("alert").style.color = "orange";
                    } else {
                        document.getElementById("alert").innerHTML = "Low Risk";
                        document.getElementById("alert").style.color = "Green";
                    }
                }
            }
        }
      });
    }
)
.catch(err => {
	console.error(err);
});
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

function toggleTheme() {
    tableTheme = document.getElementById("stateTable");
   if (localStorage.getItem('theme') === 'theme-dark'){
       setTheme('theme-light');
       tableTheme.classList="table table-striped table-hover";
       document.getElementById("searchBox").classList="form-control";
   } else {
       setTheme('theme-dark');
       tableTheme.classList="table table-dark table-striped table-hover";
       document.getElementById("searchBox").classList="form-control bg-dark";
   }
   tableTheme = document.getElementById("stateTable");
}
function checkTheme() {
  tableTheme = document.getElementById("stateTable");
  if (localStorage.getItem("theme") === "theme-light") {
    setTheme("theme-light");
    tableTheme.classList = "table table-striped table-hover";
    document.getElementById("searchBox").classList = "form-control";
  } else {
    setTheme("theme-dark");
    tableTheme.classList = "table table-dark table-striped table-hover";
    document.getElementById("searchBox").classList = "form-control bg-dark";
  }
  tableTheme = document.getElementById("stateTable");
}
window.onload = checkTheme;
(function () {
   if (localStorage.getItem('theme') === 'theme-dark') {
       setTheme('theme-dark');
   } else {
       setTheme('theme-light');
   }
})();
toggle=document.getElementById("toggle");
toggle.onclick = toggleTheme;