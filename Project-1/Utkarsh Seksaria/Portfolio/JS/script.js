console.log('hi');
var button = document.getElementsByClassName('toggle-button');

function Togglee(){
    button[0].classList.toggle('changed');
    // menu[0].style.display.toggle('none');
    console.log('value is', button[0].classList.value)
    if(button[0].classList.value=='toggle-button changed')
    {
        menu[0].style.display = 'flex';
        // menu[0].style.transition = '1s ease-in-out';
    }
    else 
    menu[0].style.display = 'none'
}

button[0].addEventListener('click',Togglee);
var menu = document.getElementsByClassName('nav-menu');

function clickMenu(){
    menu[0].classList.toggle('change');
}
menu[0].addEventListener('click',clickMenu);
if(document.documentElement.clientWidth>=600){
    console.log('big screen');
}
window.addEventListener('resize', function(){
    console.log('screen size changed');
    if(document.documentElement.clientWidth>=600){
        console.log('big screen');
        menu[0].style.display = 'none';
        button[0].classList.value='toggle-button';
    }
    else{
        button[0].classList.value='toggle-button'
    }
})