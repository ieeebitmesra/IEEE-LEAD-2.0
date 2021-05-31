 init()
 function init(){
        var url= "https://api.covid19api.com/summary"
        var data= ''
        $.get(url,function(data){
            console.log(data.Global);
            data= `
            <td>${data.Global.Date}</td>
            <td>${data.Global.NewConfirmed.toLocaleString('en')}</td>
            <td>${data.Global.NewDeaths.toLocaleString('en')}</td>
            <td>${data.Global.TotalConfirmed.toLocaleString('en')}</td>
            <td>${data.Global.TotalDeaths.toLocaleString('en')}</td>
            <td>${data.Global.TotalRecovered.toLocaleString('en')}</td>
            
            `
           $("#data").html(data) 
        })
    }
    
function refresh(data){
        clearData()
        init() 
    }
    function clearData(){
       $(data).empty()
      
    }
// milestone2
window.onload=function(){
    

}






function getCovidstats(){
   
    
    fetch('https://api.covid19api.com/summary').then(function(resp){
        return resp.json()}) .then(function(data){
        
        // console.log(data.Countries[76]);
        let country=data.Countries[76].CountryCode;
        let name=data.Countries[76].Country;
        let date=data.Countries[76].Date;
        let newConfirmed =data.Countries[76].NewConfirmed;
        
        let newDeaths =data.Countries[76].NewDeaths;
        let newRecovered =data.Countries[76].NewRecovered;
        let TotalConfirmed =data.Countries[76].TotalConfirmed;
        let TotalDeaths =data.Countries[76].TotalDeaths;
        let TotalRecoverd =data.Countries[76].TotalDeaths;
        
        document.getElementById('demo').innerHTML="Country:  " + name;
        document.getElementById('code').innerHTML="Country Code:  " +country;
        document.getElementById('date').innerHTML="Date-Time:  "+date; 
        document.getElementById('cases').innerHTML=newConfirmed.toLocaleString('en');
        document.getElementById('deaths').innerHTML=newDeaths.toLocaleString('en');
        document.getElementById('recover').innerHTML=newRecovered.toLocaleString('en');
        document.getElementById('totc').innerHTML=TotalConfirmed.toLocaleString('en');
        document.getElementById('totd').innerHTML=TotalDeaths.toLocaleString('en');
        document.getElementById('totr').innerHTML=TotalRecoverd.toLocaleString('en');
        })
    
}

