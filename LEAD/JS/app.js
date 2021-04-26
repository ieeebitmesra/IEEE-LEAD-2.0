
/** Start of dropdown menu section for smaller screens */
var menu=document.getElementById("menubar");
var sideNav = document.getElementById("sidenav");
menu.style.height = "0%";
sideNav.style.height = "0%";
sideNav.style.fontSize = "0%";
function openNav(){
    if(menu.style.height === "0%" ){
        menu.style.height = "100%";
        sideNav.style.height = "100%";
        sideNav.style.fontSize = "large";
    }
    else{
        sideNav.style.fontSize = "0%";
        menu.style.height = "0%";
        sideNav.style.height = "0%";
    }
}
function closeNav(){
        sideNav.style.fontSize = "0%";
        menu.style.height = "0%";
        sideNav.style.height = "0%";
}
/**End of dropdown menu section for smaller screens */

/** Start of Codeforces API call for live statistics */
const url1 = 'https://codeforces.com/api/user.info?handles=Rituraj.rs';
const url2 = 'https://codeforces.com/api/user.status?handle=Rituraj.rs&from=1&count=1000'
async function getRating(){
    const response = await fetch(url1);
    const data = await response.json();
    if(data.status === "OK" ){
        document.getElementById('rating').innerHTML = "Current rating : " + data.result[0].rating;
    }
}
async function getSubmission(){
    const response = await fetch(url2);
    const data = await response.json();
    if(data.status === "OK" ){
        var c = 0;
        for( i = 0 ; i < data.result.length ; i++ ){
            if( data.result[i].verdict === "OK" )
            {
                c = c+1;
            }
        }
            document.getElementById('submissions').innerHTML =  "Number of questions solved : "+c;
    }
}
getRating();
getSubmission();
/** End of Codeforces API call for live statistics */


/** Start of animation for smoother scroll */
        let anchorSelector = 'a[href^="#"]';
      
        $(anchorSelector).on('click', function (e) {
          
            e.preventDefault();
      
            let destination = $(this.hash);
      
            let scrollPosition
                = destination.offset().top;
      
            let animationDuration = 500;

            $('html, body').animate({
                scrollTop: scrollPosition
            }, animationDuration);
        });
/** End of animation for smoother scroll */