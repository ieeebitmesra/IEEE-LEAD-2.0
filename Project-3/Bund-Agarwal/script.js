//FUNCTION TO DECLARE GLOBAL LEVEL INFO
const card1=document.querySelector("#card-1");
const card2=document.querySelector("#card-2");
const card3=document.querySelector("#card-3");
function global() {
    fetch('https://coronavirus-19-api.herokuapp.com/all ').then((response)=>{
        return response.json();
    }).then((data)=>{const cases=data.cases;
        const deaths=data.deaths;
        const recovered=data.recovered;
        globalDetail(cases,recovered,deaths);
     }).catch();}
 //FUNCTION TO MODIFY GLOBAL INFO    
function globalDetail(cases,recovered,deaths){const c=document.createElement("h2");
let count=167070000;
setInterval(()=>{
  if(count<cases)
  count++;
c.textContent=count;
c.style.color='white';
},0.2);
card1.appendChild(c);
const r=document.createElement("h2");
let count2=148011000;
setInterval(()=>{
  if(count2<recovered)
  count2++;
r.textContent=count2;
r.style.color='green'
},0.2);
card2.appendChild(r);
const d=document.createElement("h2");
let count3=3469000;
setInterval(()=>{
  if(count3<deaths)
  count3++;
d.textContent=count3;
d.style.color='red';
},0.2);
card3.appendChild(d);

}
global();
//STATE INFO
var div=document.getElementById("state");

function stateInfo() {


      fetch('https://api.rootnet.in/covid19-in/stats/daily').then((response)=>{
        return response.json();}).then((data)=>{
     var last=Object.keys(data.data).pop();
     var lastValue=data.data[last];
     for(var key in data.data[last].regional)
     {
   const day=lastValue.regional[key].loc;
   const confirmed=lastValue.regional[key].confirmedCasesIndian;
   const deaths=lastValue.regional[key].deaths;
   const discharged=lastValue.regional[key].discharged;
   show(day,confirmed,deaths,discharged);
     }
  

    }).catch();}
// STATE DETAIL DISPLAY
function show(day,confirmed,deaths,discharged)
{
var pre=document.createElement("pre");
pre.textContent=`${day} 
CONFIRMED-CASES:${confirmed}
DEATHS:${deaths}
DISCHARGED:${discharged}`;
const hr=document.createElement("hr");
div.appendChild(pre);
div.appendChild(hr);
}stateInfo();
//FUNCTION FOR LAST UPDATE
function update() {


  fetch('https://api.rootnet.in/covid19-in/stats/daily').then((response)=>{
    return response.json();}).then((data)=>{
 var last=Object.keys(data.data).pop();
 var lastValue=data.data[last];
 var last_update=data.lastRefreshed;
 showDetail(last_update.substring(0,10));
}).catch();}
/*FOR DISPLAY OF LAST UPDATE*/
function showDetail(day)
{ var aside=document.getElementById("last-update");
var h2=document.createElement("h4");
h2.textContent=day;
aside.appendChild(h2);

}update();