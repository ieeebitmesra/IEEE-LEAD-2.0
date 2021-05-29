/* -----------------------------------------Smooth Scroll effect------------------------------------------------ */
import jump from "./jump.module.js";
document.querySelectorAll(".top-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        jump("#navbar", {
            duration: 1000,
            offset: 1,
        });
    });
});
document.querySelector("#home-btn").addEventListener("click", () => {
    jump(".container-home", {
        duration: 1000,
        offset: 1,
    });
});
document.querySelector("#personalize-btn").addEventListener("click", () => {
    jump(".container-personalize", {
        duration: 1000,
        offset: 1,
    });
});
document.querySelector("#about-btn").addEventListener("click", () => {
    jump(".container-AboutMe", {
        duration: 1000,
        offset: 1,
    });
});
document.querySelector("#technologies-btn").addEventListener("click", () => {
    jump(".container-technologies", {
        duration: 1000,
        offset: 1,
    });
});
document.querySelector("#projects-btn").addEventListener("click", () => {
    jump(".container-projects", {
        duration: 1000,
        offset: 1,
    });
});
document.querySelector("#cf-btn").addEventListener("click", () => {
    jump(".container-cp", {
        duration: 1000,
        offset: 1,
    });
});
/* ------------------------------------------------CP - Section ------------------------------------------------- */

let rankMap = new Map([
    ["newbie", "grey"],
    ["pupil", "green"],
    ["specialist", "darkcyan"],
    ["expert", "blue"],
    ["candidate master", "purple"],
    ["master", "orange"],
    ["international master", "orange"],
    ["grandmaster", "red"],
    ["international grandmaster", "red"],
    ["legendary grandmaster", "rgb(150,0,0)"],
]);

var rating = document.getElementById("rating");
var maxRating = document.getElementById("max-rating");
var rank = document.getElementById("rank");
var maxRank = document.getElementById("max-rank");
var profileLink = document.getElementById("profile-link");
var curClass = document.getElementsByClassName("cf-stats-cur");
var maxClass = document.getElementsByClassName("cf-stats-max");
var cpInputField = document.getElementById("cp-input-field");
var cpButton = document.getElementById("cp-btn");

function updateCPSection(handle_name) {
    function work(data) {
        console.log(data.result.length);
        if (data.result[0].rank == undefined) {
            var cfRankCur = data.result[0].rank;
            var cfRankMax = data.result[0].maxRank;
            var cfRatingCur = data.result[0].rating;
            var cfRatingMax = data.result[0].maxRating;
            var profileName = data.result[0].handle;

            rating.innerText = "Current Rating : Unrated";
            maxRating.innerText = "Max Rating : Unrated";
            rank.innerText = "Current Rank : - ";
            maxRank.innerText = "Max Rank : - ";
            profileLink.innerText = profileName;
            profileLink.href = "https://codeforces.com/profile/" + profileName;
            profileLink.style.backgroundColor = "black";

            for (var i = 0; i < curClass.length; i++) {
                curClass[i].style.color = "black";
            }

            for (var i = 0; i < maxClass.length; i++) {
                maxClass[i].style.color = "black";
            }
        } else {
            var cfRankCur = data.result[0].rank;
            var cfRankMax = data.result[0].maxRank;
            var cfRatingCur = data.result[0].rating;
            var cfRatingMax = data.result[0].maxRating;
            var profileName = data.result[0].handle;

            rating.innerText = "Current Rating : " + cfRatingCur;
            maxRating.innerText = "Max Rating : " + cfRatingMax;
            rank.innerText = "Current Rank : " + cfRankCur;
            maxRank.innerText = "Max Rank : " + cfRankMax;
            profileLink.innerText = profileName;
            profileLink.href = "https://codeforces.com/profile/" + profileName;
            profileLink.style.backgroundColor = rankMap.get(cfRankCur);

            for (var i = 0; i < curClass.length; i++) {
                curClass[i].style.color = rankMap.get(cfRankCur);
            }

            for (var i = 0; i < maxClass.length; i++) {
                maxClass[i].style.color = rankMap.get(cfRankMax);
            }
        }

        // console.log(data);
    }

    $.ajax({
        url: "https://codeforces.com/api/user.info?handles=" + handle_name,
        method: "GET",
        success: work,
        error:() => {
            alert("User Not Found!");
        }
    });
}

cpInputField.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        updateCPSection(cpInputField.value);
    }
});

cpButton.addEventListener("click", () => {
    updateCPSection(cpInputField.value);
});

updateCPSection("sarvjot");

/* ------------------------------------------------Image-Popup------------------------------------------------- */
$(".certificate-btn").magnificPopup({
    type: "iframe",
    gallery: {
        enabled: true,
    },
});
$(".project-img").magnificPopup({
    type: "image",
    gallery: {
        enabled: true,
    },
});

// media query event handler
if (matchMedia) {
    const mq = window.matchMedia("(max-width:700px)");
    mq.addListener(WidthChange);
    WidthChange(mq);
}

// media query change
function WidthChange(mq) {
    if (mq.matches) {
        // window width is less than 500px
        $(".certificate-btn").magnificPopup({
            type: "image",
            gallery: {
                enabled: true,
            },
        });
    } else {
        // window width is more than 500px
        $(".certificate-btn").magnificPopup({
            type: "iframe",
            gallery: {
                enabled: true,
            },
        });
    }
}
/* --------------------------------------Javascript theme Switcher ----------------------------------------------*/

var body = document.querySelector("body");

// Applying the cached theme on reload

let color = localStorage.getItem("color");
let font = localStorage.getItem("font");

if (color) {
    body.classList = [color];
}
if (font) {
    body.id = font;
}
updateStyle();

// Color Switcher
document.querySelector("#card-1").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.classList.contains("aqua") === false) {
        body.classList = ["aqua"];
        localStorage.setItem("color", "aqua");
        updateStyle();
    }
});
document.querySelector("#card-2").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.classList.contains("furious") === false) {
        body.classList = ["furious"];
        localStorage.setItem("color", "furious");
        updateStyle();
    }
});
document.querySelector("#card-3").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.classList.contains("peaceful") === false) {
        body.classList = ["peaceful"];
        localStorage.setItem("color", "peaceful");
        updateStyle();
    }
});
document.querySelector("#card-4").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.classList.contains("lovely") === false) {
        body.classList = ["lovely"];
        localStorage.setItem("color", "lovely");
        updateStyle();
    }
});
// Font-Style Switcher
document.querySelector("#handwriting-card-1").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.id !== "sketchy") {
        body.id = "sketchy";
        localStorage.setItem("font", "sketchy");
        updateStyle();
    }
});
document.querySelector("#handwriting-card-2").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.id !== "classic") {
        body.id = "classic";
        localStorage.setItem("font", "classic");
        updateStyle();
    }
});
document.querySelector("#handwriting-card-3").addEventListener("click", () => {
    var body = document.querySelector("body");
    if (body.id !== "trendy") {
        body.id = "trendy";
        localStorage.setItem("font", "trendy");
        updateStyle();
    }
});
/*------------------------------------------- Current Style Dashboard -------------------------------------------*/
function updateStyle() {
    document.querySelector(
        "#current-style"
    ).textContent = `${body.classList[0]} - ${body.id}`;
}
