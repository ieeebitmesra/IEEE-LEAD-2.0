var mybutton = document.getElementById("backToTop");
var buttonControl = document.body;

var cfHandle = document.getElementById("cf-handle");
var cfCurrentRating = document.getElementById("cf-current-rating");
var cfMaxRating = document.getElementById("cf-max-rating");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
	if (buttonControl.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		mybutton.style.display = "block";
	} else {
		mybutton.style.display = "none";
	}
}

console.log(buttonControl.scrollTop);

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
	document.body.scrollTop = 0; // For Safari
	document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


// to print codeforces stats with rank-specific colors

function getCodeforcesData() {

	function work(data) {

		var cfRankCur = data.result[0].rank;
		var cfRankMax = data.result[0].maxRank;

		cfHandle.innerHTML = "<span class=\"name-of-stat\">Handle: </span><span class=\"current-handle\"><a href=\"https://codeforces.com/profile/naman1601\" target=\"_blank\" title=\"visit my codeforces profile\">" + data.result[0].handle + "</a></span>";
		cfCurrentRating.innerHTML = "<span class=\"name-of-stat\">Current Rating: </span><span class=\"current-stats\">" + data.result[0].rating + " (" + data.result[0].rank + ")" + "</span>";
		cfMaxRating.innerHTML = "<span class=\"name-of-stat\">Max Rating: </span><span class=\"max-stats\">" + data.result[0].maxRating + " (" + data.result[0].maxRank + ")" + "</span>";

		var handleClass = document.getElementsByClassName("current-handle")[0];
		var handleLink = handleClass.getElementsByTagName("a")[0];
		var curClass = document.getElementsByClassName("current-stats");
		var maxClass = document.getElementsByClassName("max-stats");

		for(var i = 0; i < curClass.length; i++) {

			if(cfRankCur == "newbie") {

				handleLink.style.color = "grey";
				curClass[i].style.color = "grey";
			}

			if(cfRankCur == "pupil") {

				handleLink.style.color = "green";
				curClass[i].style.color = "green";
			}

			if(cfRankCur == "specialist") {

				handleLink.style.color = "darkcyan";
				curClass[i].style.color = "darkcyan";
			}

			if(cfRankCur == "expert") {

				handleLink.style.color = "#3c6ffe";
				curClass[i].style.color = "#3c6ffe";

			}

			if(cfRankCur == "candidate master") {

				handleLink.style.color = "purple";
				curClass[i].style.color = "purple";
			}

			if(cfRankCur == "master") {

				handleLink.style.color = "orange";
				curClass[i].style.color = "orange";
			}

			if(cfRankCur == "international master") {

				handleLink.style.color = "orange";
				curClass[i].style.color = "orange";
			}

			if(cfRankCur == "grandmaster") {

				handleLink.style.color = "red";
				curClass[i].style.color = "red";
			}

			if(cfRankCur == "international grandmaster") {

				handleLink.style.color = "red";
				curClass[i].style.color = "red";
			}

			if(cfRankCur == "legendary grandmaster") {

				handleLink.style.color = "rgb(150, 0, 0)";
				curClass[i].style.color = "rgb(150, 0, 0)";
			}
		}


		for(var i = 0; i < curClass.length; i++) {

			if(cfRankMax == "newbie") {

				maxClass[i].style.color = "grey";
			}

			if(cfRankMax == "pupil") {

				maxClass[i].style.color = "green";
			}

			if(cfRankCur == "specialist") {

				maxClass[i].style.color = "darkcyan";
			}

			if(cfRankMax == "expert") {

				maxClass[i].style.color = "#3c6ffe";

			}

			if(cfRankMax == "candidate master") {

				maxClass[i].style.color = "purple";
			}

			if(cfRankMax == "master") {

				maxClass[i].style.color = "orange";
			}

			if(cfRankMax == "international master") {

				maxClass[i].style.color = "orange";
			}

			if(cfRankMax == "grandmaster") {

				maxClass[i].style.color = "red";
			}

			if(cfRankMax == "international grandmaster") {

				maxClass[i].style.color = "red";
			}

			if(cfRankMax == "legendary grandmaster") {

				maxClass	[i].style.color = "rgb(150, 0, 0)";
			}
		}

		console.log(data);
	}

	$.ajax({
		url: "https://codeforces.com/api/user.info?handles=naman1601",
		method: "GET",
		success: work,
	});
};

getCodeforcesData();