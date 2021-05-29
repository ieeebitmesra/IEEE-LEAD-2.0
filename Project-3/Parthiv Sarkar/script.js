var entry = document.getElementById("entry");
console.log(entry);
    entry.addEventListener('submit', function (e) 
    
    {
        e.preventDefault();
        var confirmed,dead,recovered,active,flag = 0;
        var inp = document.getElementById("inp").value;
        console.log(inp);
        if( flag === 0 ){
            var url1 = 'https://api.rootnet.in/covid19-in/stats/latest'
            fetch(url1).then(res1 => {
                return res1.json();
            }).then( dat => {
                e.preventDefault();
                for( i in dat["data"]["regional"] ){
                    if( dat["data"]["regional"][i]["loc"].toLowerCase() === inp.toLowerCase() ){
                        flag = 1;
                        confirmed = dat["data"]["regional"][i]["totalConfirmed"];
                        dead = dat["data"]["regional"][i]["deaths"];
                        recovered = dat["data"]["regional"][i]["discharged"];
                        active = confirmed-recovered-dead;
                        document.getElementById('cur').innerHTML = inp;
                        document.getElementById('ac').innerHTML = active;
                        document.getElementById('dead').innerHTML = dead;
                        document.getElementById('tot').innerHTML = confirmed;
                        document.getElementById('rec').innerHTML = recovered;
                       
                        document.getElementById('zon').innerHTML = "Look for the districts.";
            
                        break;
                    }
                }
            if( flag === 1 ){
            
            }
            flag = 0;
        })
        }
        if( flag === 0 ){
        var url2 = 'https://www.trackcorona.live/api/countries'
        fetch(url2).then(res1 => {
            return res1.json();
        }).then( dat => {
            for( i in dat["data"] ){
                if( dat["data"][i]["location"].toLowerCase() === inp.toLowerCase() ){
                    confirmed = dat["data"][i]["confirmed"];
                    dead = dat["data"][i]["dead"];
                    recovered = dat["data"][i]["recovered"];
                    active = confirmed-recovered-dead;
                    document.getElementById('cur').innerHTML = inp;
            document.getElementById('ac').innerHTML = active;
            document.getElementById('dead').innerHTML = dead;
            document.getElementById('tot').innerHTML = confirmed;
            document.getElementById('rec').innerHTML = recovered;
            document.getElementById('zon').innerHTML = "Look for the districts.";
            
                    flag = 1;
                    break;
                }
            }
            if(flag === 1){
            
            }
        })
        flag = 0;
    }
            if( flag === 0 ){
                e.preventDefault();
                flag = 0;
                var url = 'https://api.covid19india.org/v4/min/data.min.json'
                fetch(url).then( res => {
                    return res.json();
                }).then( data => {
                    var f = 0;
                    for( i in data ){
                        for( j in data[i]["districts"] ){
                        if( inp.toLowerCase() === j.toLowerCase() ){
                            f = 1;
                            flag = 1;
                           
                            confirmed = data[i]["districts"][j]["total"]["confirmed"];
                            dead = data[i]["districts"][j]["total"]["deceased"];
                            recovered = data[i]["districts"][j]["total"]["recovered"];
                            vaccine = data[i]["districts"][j]["total"]["vaccinated"];
                            active = confirmed-recovered-dead;
                            document.getElementById('cur').innerHTML = inp;
                            document.getElementById('ac').innerHTML = active;
                            document.getElementById('dead').innerHTML = dead;
                            document.getElementById('tot').innerHTML = confirmed;
                            document.getElementById('rec').innerHTML = recovered;

                            if(active>15000){
                            document.getElementById('zon').innerHTML = "RED ZONE.(HIGH ALERT)";
                                }
                           else if(active>=10000){
                            document.getElementById('zon').innerHTML = "ORANGE ZONE.(RISK)";}
                            else{
                            document.getElementById('zon').innerHTML = "GREEN ZONE.(SAFE)";}

                            break;
                        }
                    }
                if( flag === 1 ){
                
                }
            }
                flag = 0;
            
            })
        }
    })