function getLocation(){
    let lat,lon;
    navigator.geolocation.getCurrentPosition(pos => {
    lat = pos.coords.latitude;
    lon = pos.coords.longitude;
    const key1 = '8e8ac6460bmsh1fe2851c85425d7p12c847jsn4cfda51e485f';
    const key = "AIzaSyB7jTTqZVkmHBNRW5nMPGxK4Fyt8JFRvKk";
    let url3 = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+lat+','+lon+'&key='+key;
    fetch(url3).then( response => {
        return response.json();
    }).then( data =>{
        var url = 'https://api.covid19india.org/v4/min/data.min.json'
        fetch(url).then( res => {
            return res.json();
        }).then( disdata => {
        var f = 0,f1 = 0,cnf,rec,ded,vcc,country,pop,cact,cded,crec;
        for( k = 0; k < data.results.length ; k++ ){   
            console.log(data.results[k]);
            for( district  = 0; district < data.results[k].address_components.length ; district++ ){
                console.log(district);
                for( i in disdata ){
                    for( j in disdata[i]["districts"] ){
                        if( data.results[k].address_components[district].long_name.toLowerCase() === j.toLowerCase() ){
                        f = 1;
                        f1 = 1;
                        country = data.results[k].address_components[district].long_name;
                        pop = disdata[i]["districts"][j]["meta"]["population"];
                        cnf = disdata[i]["districts"][j]["total"]["confirmed"];
                        ded = disdata[i]["districts"][j]["total"]["deceased"];
                        rec = disdata[i]["districts"][j]["total"]["recovered"];
                        vcc = disdata[i]["districts"][j]["total"]["vaccinated"];
                        break;
                        }
                    }
                    if(f){
                        break;
                    }
                }
                if(f1){
                    break;
                }
            }
            if(f1){
                break;
            }
        }
        if( f1 === 1 ){        
            document.getElementById('srch').innerHTML = ''+country+'';
            document.getElementById('dispactivedat').innerHTML = ''+(cnf-rec-ded)+'';
            document.getElementById('dispdeddat').innerHTML = ''+ded+'';
            document.getElementById('dispcnfdat').innerHTML = ''+cnf+'';
            document.getElementById('disprecdat').innerHTML = ''+rec+'';
            document.getElementById('dispvcc').innerHTML = 'Total vaccinated <br>&nbsp;&nbsp; '+vcc+'';
            document.getElementById('dispprec').innerHTML = ''+pop+'';
        }
    })
})
})
}