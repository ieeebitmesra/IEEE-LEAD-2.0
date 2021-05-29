function ini() {
   let x = "india";
   Clean(x);
   fetch('https://api.covid19api.com/live/country/India').then((response) => {
      return response.json();

   }).then((data) => {
      console.log(data);
      india(data);

   })

}





function getdta() {


   fetch('https://ix.cnn.io/data/novel-coronavirus-2019-ncov/world/full.min.json?q=1622050032').then((response) => {
      return response.json();

   }).then((data) => {
      console.log(data);
      show(data);




   }).catch((error) => {
      console.log(error);

   })
}







function get() {
   let x = 'class1';
   Clean(x);

   fetch('https://ix.cnn.io/data/novel-coronavirus-2019-ncov/world/full.min.json?q=1622050032').then((response) => {
      return response.json();

   }).then((data) => {
      console.log(data);

      computation(data);



   }).catch((error) => {
      console.log(error);

   })
}



function show(data) {



   const total = data.history.totals;
   const place = data.history.places;
   const wdiv = document.getElementById('class');

   let z = 0;
   let x = 0;
   let l = 0;
   let m = 0;
   const deaths = document.createElement('h3');
   for (var s = 0; s < total.deaths.length; s++) {

      x += total.deaths[s];
   }
   const cases = document.createElement('h3');
   for (var a = 0; a < total.cases.length; a++) {
      z += total.cases[a];

   }
   const newcases = document.createElement('h3');
   for (var r = 0; r < place.length; r++) {


      for (var a = 0; a < place[r].new_cases.length; a++) {
         l += place[r].new_cases[a];
      }
   }
      const newdeaths = document.createElement('h3');
      for (var r = 0; r < place.length; r++) {


         for (var a = 0; a < place[r].new_deaths.length; a++) {
            m += place[r].new_deaths[a];
         }
      }


      cases.innerHTML = " Total cases= " + z;
      deaths.innerHTML = " Total deaths= " + x;
      newcases.innerHTML = "New cases =" + l;
      newdeaths.innerHTML = "New deaths =" + m;
     
      wdiv.appendChild(cases);
      wdiv.appendChild(deaths);
      wdiv.appendChild(newcases);
      wdiv.appendChild(newdeaths);
   }

   const button = document.getElementById('bu');
   const para = document.getElementById('covid');

   button.addEventListener('click', update);

   function update() {
      // para.textContent='Here it is';
      button.value = 'clicked';
      getdta();

      doSomething();
   }


   function doSomething() {
      // Disable the button
      document.getElementById("bu").disabled = true;

      // Do your processing here
      alert("You clicked button!");

  
   }

   const myButton = document.getElementById('bug');
   myButton.addEventListener('click', get);



   function computation(data) {

      const ndiv = document.getElementById('class1');
      var ncases = document.createElement('h3');
      var ndeaths = document.createElement('h3');
      var cont = document.createElement('h3');
      var countryname = document.createElement('h3');

      var y = 0;
      var x = 0;

      const plac = data.history.places;
      let country = document.getElementById('search').value;
      for (var r = 0; r < plac.length; r++) {

         if (plac[r].name == country) {
            for (var a = 0; a < plac[r].new_cases.length; a++) {
               y += plac[r].new_cases[a];
               x += plac[r].new_deaths[a];
               cont.innerHTML = 'Continent = ' + plac[r].continent;
               countryname.innerHTML = 'Country = ' + plac[r].name;
            }
         }

         ncases.innerHTML = 'New cases =' + y;
         ndeaths.innerHTML = 'New deaths = ' + x;


      }


      ndiv.appendChild(ncases);
      ndiv.appendChild(ndeaths);
      ndiv.appendChild(cont);
      ndiv.appendChild(countryname);

   }



   const newbutton = document.getElementById('ins');
   newbutton.addEventListener('click', ini);







   function india(data) {
      let pro = document.getElementById('in').value;
      const ins = document.getElementById("india");
      var active = document.createElement('h3');
      var confirm = document.createElement("h3");
      var deaths = document.createElement('h3');
      var province = document.createElement('h3');
      var recover = document.createElement('h3');
      for (var a = 0; a < data.length; a++) {
         if (data[a].Province == pro) {
            active.innerHTML = "Active Cases =  " + data[a].Active;
            confirm.innerHTML = "Confirmed Cases = " + data[a].Confirmed;
            deaths.innerHTML = " Deaths =  " + data[a].Deaths;
            province.innerHTML = " Province: " + data[a].Province;
            recover.innerHTML = " Recoverd = " + data[a].Recovered;
         }
      }
      ins.appendChild(active);
      ins.appendChild(confirm);
      ins.appendChild(deaths);
      ins.appendChild(province);
      ins.appendChild(recover);


   }


   function Clean(x) {
      document.getElementById(x).innerHTML = '';
   }







// FOR ACCESSING CURRENT LOCATION



   // var options = {
   //    enableHighAccuracy: true,
   //    timeout: 5000,
   //    maximumAge: 0
   //  };
    
   //  function success(pos) {
   //    var crd = pos.coords;

   //   function cal(data)
   //   {
      
      
   //    let la= document.getElementById("inside");
   //    var active = document.createElement('h3');
   //    var confirms = document.createElement("h3");
   //    var deaths = document.createElement('h3');
   //    var province = document.createElement('h3');
   //    var recover = document.createElement('h3');
   //    for (var a = 0; a < data.length; a++) {
   //       if (data[a].Latitude ==crd.latitude) {
   //          if(data[a].Longitude == crd.longitude){
   //          active.innerHTML = "Active Cases =  " + data[a].Active;
   //          confirms.innerHTML = "Confirmed Cases = " + data[a].Confirmed;
   //          deaths.innerHTML = " Deaths =  " + data[a].Deaths;
   //          province.innerHTML = " Province: " + data[a].Province;
   //          recover.innerHTML = " Recoverd = " + data[a].Recovered;
   //          }
   //       }
   //    }
   //   }
    
   //    // console.log('Your current position is:');
   //    // console.log(`Latitude : ${crd.latitude}`);
   //    // console.log(`Longitude: ${crd.longitude}`);
   //    // console.log(`More or less ${crd.accuracy} meters.`);
   //    la.appendChild(active);
   //    la.appendChild(confirms);
   //    la.appendChild(deaths);
   //    la.appendChild(province);
   //    la.appendChild(recover);
   //  }
    
   //  function error(err) {
   //    console.warn(`ERROR(${err.code}): ${err.message}`);
   //  }
    
   //  navigator.geolocation.getCurrentPosition(success, error, options);



   //  function inside()
   //  {
   //    fetch('https://api.covid19api.com/live/country/India').then((response) => {
   //       return response.json();
   
   //    }).then((data) => {
   //       console.log(data);
   //       cal(data);

        
   
   //    })
   //  }