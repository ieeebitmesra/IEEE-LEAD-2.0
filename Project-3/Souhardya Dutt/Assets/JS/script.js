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
		document.getElementById("world_cases").innerHTML = dataWorld.world_total.total_cases;
		document.getElementById("active_cases").innerHTML = dataWorld.world_total.active_cases;
		document.getElementById("new_cases").innerHTML = dataWorld.world_total.new_cases;
		document.getElementById("total_deaths").innerHTML = dataWorld.world_total.total_deaths;
		document.getElementById("new_deaths").innerHTML = dataWorld.world_total.new_deaths;
		document.getElementById("total_recovered").innerHTML = dataWorld.world_total.total_recovered;
		document.getElementById("india_cases").innerHTML = dataWorld.countries_stat[1].cases;
		document.getElementById("india_active_cases").innerHTML = dataWorld.countries_stat[1].active_cases;
		document.getElementById("india_new_cases").innerHTML = dataWorld.countries_stat[1].new_cases;
		document.getElementById("india_deaths").innerHTML = dataWorld.countries_stat[1].deaths;
		document.getElementById("india_new_deaths").innerHTML = dataWorld.countries_stat[1].new_deaths;
		document.getElementById("india_recovered").innerHTML = dataWorld.countries_stat[1].total_recovered;
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
   if (localStorage.getItem('theme') === 'theme-dark'){
       setTheme('theme-light');
   } else {
       setTheme('theme-dark');
   }
}
(function () {
   if (localStorage.getItem('theme') === 'theme-dark') {
       setTheme('theme-dark');
   } else {
       setTheme('theme-light');
   }
})();
toggle=document.getElementById("toggle");
toggle.onclick = toggleTheme;