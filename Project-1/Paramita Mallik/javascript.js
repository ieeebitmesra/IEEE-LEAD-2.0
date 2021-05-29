$(document).ready(function(){
 $(window).scroll(function(){
 if(this.scroLLY >20){
    $('.navbar').addClass('sticky');
}
else{
    $('.navbar').removeClass('sticky');
}
if(this.scroll >500){
    $('.scroll-up-btn').addClass("show");
}else{
    $('.scroll-up-btn').removeClass("show");
}
 });
//slide-up Script
$('.scroll-up-btn').click(function(){
$('html').animate({scrollTop: 0});

});

//toggle menu/navbar script
$('.menu-btn').click(function(){
$('.navbar .menu').toggleClass("active");
$('.menu-btn i').toggleClass("active");
})
//typing animation script
var typed= new Typed(".typing", {
    strings: ["Developer", "Musician", "Designer"],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
});
//owl carousal script
    $('.carousel').owlCarousel({
      margin: 20,
      loop: true,
       autoplayTimeout: 2000,
       autoplayHoverPause: true,
       responsive: {
        items: 1,
        nav: false
         },
         600:{
          items: 2,
          nav: false
          },
          1000:{
           items: 3,
           nav: false
        }
    }
  
  );
}); 