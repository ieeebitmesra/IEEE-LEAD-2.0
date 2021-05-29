var menutoggle = 0,indian_stats_toggle = 0,indian_test_toggle = 0,indian_state_toggle = 0,toggle_about=0;
function pleaseopenmenu() {
    const navmenu = document.querySelector(".nav1");
	if (menutoggle === 0) {
		navmenu.style = "display:flex";
		menutoggle = 1;
	}
	else {
		navmenu.style = "display:none";
		menutoggle = 0;
	}
}
function openindiaoverall() {
    const section2 = document.querySelector(".sec2");
    const indiaheading = document.querySelector(".india");
	if (indian_stats_toggle === 0) {
		section2.style = "display:flex";
        indiaheading.style = "display:flex";
		indian_stats_toggle = 1;
	}
	else {
		section2.style = "display:none";
        indiaheading.style = "display:none";
		indian_stats_toggle = 0;
	}
}
function openindiatesting() {
    const section3 = document.querySelector(".sec3");
    const indiatesting = document.querySelector(".testing");
	if (indian_test_toggle === 0) {
		section3.style = "display:flex";
        indiatesting.style = "display:flex";
		indian_test_toggle = 1;
	}
	else {
		section3.style = "display:none";
        indiatesting.style = "display:none";
		indian_test_toggle = 0;
	}
}
function openstatesoverall() {
    const section4 = document.querySelector(".sec4");
    const indiastates = document.querySelector(".states");
	if (indian_state_toggle === 0) {
		section4.style = "display:flex";
        indiastates.style = "display:flex";
		indian_state_toggle = 1;
	}
	else {
		section4.style = "display:none";
        indiastates.style = "display:none";
		indian_state_toggle = 0;
	}
}
function openabout() {
    const section5 = document.querySelector(".sec5");
    const about1 = document.querySelector(".about");
	if (toggle_about === 0) {
		section5.style = "display:flex";
        about1.style = "display:flex";
		toggle_about = 1;
	}
	else {
		section5.style = "display:none";
        about1.style = "display:none";
		toggle_about = 0;
	}
}

var icon = document.querySelector(".fas");
icon.addEventListener("click", pleaseopenmenu);

var indian_covid_statistics = document.querySelector(".li11");
indian_covid_statistics.addEventListener("click", openindiaoverall);

var indian_testing_statistics = document.querySelector(".li12");
indian_testing_statistics.addEventListener("click", openindiatesting);

var indian_states_overall = document.querySelector(".li13");
indian_states_overall.addEventListener("click", openstatesoverall);

var abouty = document.querySelector(".li14");
abouty.addEventListener("click", openabout);