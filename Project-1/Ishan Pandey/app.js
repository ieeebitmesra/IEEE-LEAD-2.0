const navSlide= () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', ()=>{
        // Toogle Nav
        nav.classList.toggle('nav-active');

        //Animate links
        navLinks.forEach((link, index) => {
            // link.style.animation = ` navLinkFade 0.5s ease forwards ${index / 7 + 5}s`;
            if(link.style.animation){
                link.style.animation='';
            }else{
                link.style.animation = ` navLinkFade 0.5s ease forwards ${index / 7 + 0.6}s`;
            }
        });

        // Burger animation
        burger.classList.toggle('toggle');
    });
}
navSlide();

const coolTextContainer = document.getElementById("typing");

let i = 0;
const coolText = [
    "P",
    "Pr",
    "Pro",
    "Prog",
    "Progr",
    "Progra",
    "Program",
    "Programm",
    "Programme",
    "Programmer",
    "Programmer",
    "Programmer",
    "Programme",
    "Programm",
    "Program",
    "Progra",
    "Progr",
    "Prog",
    "Pro",
    "Pr",
    "P",
    "D",
    "De",
    "Dev",
    "Deve",
    "Devel",
    "Develo",
    "Develop",
    "Develope",
    "Developer",
    "Developer",
    "Developer",
    "Develope",
    "Develop",
    "Develo",
    "Devel",
    "Deve",
    "Dev",
    "De",
    "D",
    "L",
    "Le",
    "Lea",
    "Lear",
    "Learn",
    "Learne",
    "Learner",
    "Learner",
    "Learner",
    "Learne",
    "Learn",
    "Lear",
    "Lea",
    "Le",
    "L"
];
function coolTextHandler(){
    coolTextContainer.innerHTML = coolText[i];
    i = (i+1)%55;
}

setInterval(coolTextHandler, 250);