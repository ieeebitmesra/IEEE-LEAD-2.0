document.getElementById("menu_button").onclick = function() {myFunction()};

function myFunction() {
  document.getElementById("menu_dropdown").classList.toggle("show");
}

function scroll(){
    var x=document.body.scrollTop;
    if(x>1000 || document.documentElement.scrollTop > 1000){
        var y=document.getElementsByClassName("class01");
        for(var i=0;i<y.length;i++){
            y[i].classList.add("animation01");
        }
    }

}
window.onscroll = function () {
    scroll();
};