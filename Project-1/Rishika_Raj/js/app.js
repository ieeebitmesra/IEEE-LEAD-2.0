

var menu=document.getElementById("menubar");
var hid=document.getElementById("hidden");
/*
var hid2=document.getElementById("hide2");
var hid3=document.getElementById("hide3");
var hid4=document.getElementById("hide4");
var hid5=document.getElementById("hide5");*/
//var sidenav=document.getElementById("sidenav");
$("#sidenav").css("width","0px");
//$("#sidenav").css("font-size","0px");
$("#hidden").css("display","none");

menu.onclick=function(){
	if ($("#sidenav").css("width")=="0px"){
		$("#sidenav").css("width","230px");
		//$("#sidenav").css("font-size","25px");
		$("#hidden").css("display","block");
	}
	else{
		$("#sidenav").css("width","0px");	
		$("#hidden").css("display","none");

	}
}

hid.onclick=function(){
	if ($("#sidenav").css("width")=="230px"){
		$("#sidenav").css("width","0px");
		$("#hidden").css("display","none");
	}
}
/*
hid2.onclick=function(){
	if ($("#sidenav").css("width")=="230px"){
		$("#sidenav").css("width","0px");
		$("#hidden").css("display","none");
		$("#sidenav").css("font-size","0px");
	}
}
hid3.onclick=function(){
	if ($("#sidenav").css("width")=="230px"){
		$("#sidenav").css("width","0px");
		$("#hidden").css("display","none");
		$("#sidenav").css("font-size","0px");
	}
}
hid4.onclick=function(){
	if ($("#sidenav").css("width")=="230px"){
		$("#sidenav").css("width","0px");
		$("#hidden").css("display","none");
		$("#sidenav").css("font-size","0px");
	}
}
hid5.onclick=function(){
	if ($("#sidenav").css("width")=="230px"){
		$("#sidenav").css("width","0px");
		$("#hidden").css("display","none");
		$("#sidenav").css("font-size","0px");
	}
}
*/


$(document).ready(function(){


	const url1 = 'https://codeforces.com/api/user.info?handles=_Rishika_';
	const url2 = 'https://codeforces.com/api/user.status?handle=_Rishika_&from=1&count=1000';
	async function getRating(){
		const response = await fetch(url1);
		const data = await response.json();
		if(data.status === "OK" ){
			$(".code-r").append("<b>Current rating :   </b>" + "<em>"+ data.result[0].rating +"</em>"+ "<br /><br /> <b> Rank :   </b>" + "<em>"+data.result[0].rank+"</em>");
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
			$(".code-r").append("<br/><br/><b>Number of questions solved :   </b>"+ "<em>"+c+"</em>"+"<br /><br/><b>Total number of submissions :   </b>"+ "<em>"+data.result.length+"</em>");
		}
	}
	getRating();
	getSubmission();
})
