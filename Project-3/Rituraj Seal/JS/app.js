// Getting COVID-19 cases based on location search data 
var myForm3 = document.getElementById("myForm2");
    myForm3.addEventListener('submit', function (e) {
        e.preventDefault()
        var cnf,ded,rec,f1 = 0,pop1 = '',perc = '',vcc = '';
        var country = document.getElementById("country").value;
        if( f1 === 0 ){
        // Checking whether the location entered is a country
        var url2 = 'https://www.trackcorona.live/api/countries'
        fetch(url2).then(res1 => {
            return res1.json();
        }).then( dat => {
            // dat contains data of all the countries
            for( i in dat["data"] ){
                if( dat["data"][i]["location"].toLowerCase() === country.toLowerCase() ){
                    cnf = dat["data"][i]["confirmed"];
                    ded = dat["data"][i]["dead"];
                    rec = dat["data"][i]["recovered"];
                    if( vcc === 'undefined' ){
                                vcc = '';
                    }
                    document.getElementById('srch').innerHTML = ''+country+'';
                    document.getElementById('dispactivedat').innerHTML = ''+(cnf-rec-ded)+'';
                    document.getElementById('dispdeddat').innerHTML = ''+ded+'';
                    document.getElementById('dispcnfdat').innerHTML = ''+cnf+'';
                    document.getElementById('disprecdat').innerHTML = ''+rec+'';
                    document.getElementById('dispvcc').innerHTML = ''+vcc+'';
                    document.getElementById('percentage').innerHTML = ''+perc+'';
                    if( (cnf-rec-ded) >= 4000000 ){
                        window.alert('Active corona cases in '+country+' is very high. Please stay at home.');
                       document.getElementById('dispalert').innerHTML = '<fieldset id="veryhigh"><img alt ="Alert symbol" width=3% src="Photos/alert1.svg"><br>&nbsp;Active corona cases in '+country+' is very high.Please stay at home.</fieldset>';
                    }
                    else if( (cnf-rec-ded) >= 2000000 ){
                        window.alert('Active corona cases in '+country+' is high. Please take necessary precautions.');
                       document.getElementById('dispalert').innerHTML = '<fieldset id="high"><img alt="Alert symbol" width=3% src="Photos/alert1.svg"><br>&nbsp;Active corona cases in '+country+' is high. Please take necessary precautions.</fieldset>';
                    }
                    else{
                        document.getElementById('dispalert').innerHTML = '<fieldset id="low"><img alt = "Safe symbol"width=3% src="Photos/safe.svg"><br>&nbsp;Active corona cases in '+country+' is relatively low</fieldset>'
                    }
                    f1 = 1;
                    break;
                }
            }
        }).catch(err => {
            console.log(err);
        })
        f1 = 0;
    }
            if( f1 === 0 ){
                e.preventDefault();
                f1 = 0;
                // Checking whether location entered is a district in India
                var url = 'https://api.covid19india.org/v4/min/data.min.json'
                fetch(url).then( res => {
                    return res.json();
                }).then( data => {
                    var f = 0;
                    // data contains data of all thr districts in India
                    for( i in data ){
                        for( j in data[i]["districts"] ){
                        if( country.toLowerCase() === j.toLowerCase() ){
                            f = 1;
                            f1 = 1;
                            pop1 = data[i]["districts"][j]["meta"]["population"];
                            cnf = data[i]["districts"][j]["total"]["confirmed"];
                            ded = data[i]["districts"][j]["total"]["deceased"];
                            rec = data[i]["districts"][j]["total"]["recovered"];
                            vcc = data[i]["districts"][j]["total"]["vaccinated"];
                            if( vcc == 'undefined' ){
                                vcc = '';
                            }
                            document.getElementById('srch').innerHTML = ''+country+'';
                            document.getElementById('dispactivedat').innerHTML = ''+(cnf-rec-ded)+'';
                            document.getElementById('dispdeddat').innerHTML = ''+ded+'';
                            document.getElementById('dispcnfdat').innerHTML = ''+cnf+'';    
                            document.getElementById('disprecdat').innerHTML = ''+rec+'';
                            perc = vcc/pop1*100;
                            if( vcc !== 'undefined')
                            document.getElementById('dispvcc').innerHTML = 'Total vaccinated <br>&nbsp;&nbsp; '+vcc+'';
                            document.getElementById('percentage').innerHTML = 'Total population vaccinated <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '+perc.toPrecision(5)+'%';
                            if( (cnf-rec-ded)/pop1*100 >= 0.25 ){
                                window.alert('Active corona cases in '+country+' is very high. Please stay at home.');
                               document.getElementById('dispalert').innerHTML = '<fieldset id="veryhigh"><img alt ="Alert symbol" width=3% src="Photos/alert1.svg"><br>&nbsp;Active corona cases in '+country+' is very high.Please stay at home.</fieldset>';
                            }
                            else if( (cnf-rec-ded)/pop1*100 >= 0.1 ){
                                window.alert('Active corona cases in '+country+' is high. Please take necessary precautions.');
                               document.getElementById('dispalert').innerHTML = '<fieldset id="high"><img alt ="Alert symbol" width=3% src="Photos/alert1.svg"><br>&nbsp;Active corona cases in '+country+' is high. Please take necessary precautions.</fieldset>';
                            }
                            else{
                                document.getElementById('dispalert').innerHTML = '<fieldset id="low"><img alt ="Safe symbol" width=3% src="Photos/safe.svg"><br>&nbsp;Active corona cases in '+country+' is relatively low</fieldset>'
                            }                    
                        break;
                        }
                    }
                    if(f){
                        break;
                    }
                }
        })
        f1 = 0;
    }
    if( f1 === 0 ){
        var url1 = 'https://api.rootnet.in/covid19-in/stats/latest'
        // Checking whether location input is a state in India
        fetch(url1).then(res1 => {
            return res1.json();
        }).then( dat => {
            // dat contains data on all the states in India
            e.preventDefault();
            for( i in dat["data"]["regional"] ){
                if( dat["data"]["regional"][i]["loc"].toLowerCase() === country.toLowerCase() ){
                    f1 = 1;
                    cnf = dat["data"]["regional"][i]["totalConfirmed"];
                    ded = dat["data"]["regional"][i]["deaths"];
                    rec = dat["data"]["regional"][i]["discharged"];
                    if( vcc === 'undefined' ){
                        vcc = '';
                    }
                document.getElementById('srch').innerHTML = ''+country+'';
                document.getElementById('dispactivedat').innerHTML = ''+(cnf-rec-ded)+'';
                document.getElementById('dispdeddat').innerHTML = ''+ded+'';
                document.getElementById('dispcnfdat').innerHTML = ''+cnf+'';
                document.getElementById('disprecdat').innerHTML = ''+rec+'';
                document.getElementById('dispvcc').innerHTML = ''+vcc+'';
                document.getElementById('percentage').innerHTML = ''+perc+'';
                if( (cnf-rec-ded) >= 100000 ){
                    window.alert('Active corona cases in '+country+' is very high. Please stay at home.');
                   document.getElementById('dispalert').innerHTML = '<fieldset id="veryhigh"><img alt ="Alert symbol" width=3% src="Photos/alert1.svg"><br>&nbsp;Active corona cases in '+country+' is very high.Please stay at home.</fieldset>';
                }
                else if( (cnf-rec-ded) >= 50000 ){
                    window.alert('Active corona cases in '+country+' is high. Please take necessary precautions.');
                   document.getElementById('dispalert').innerHTML = '<fieldset id="high"><img alt ="Alert symbol" width=3% src="Photos/alert1.svg"><br>&nbsp;Active corona cases in '+country+' is high. Please take necessary precautions.</fieldset>';
                }
                else{
                    document.getElementById('dispalert').innerHTML = '<fieldset id="low"><img alt ="Safe symbol" width=3% src="Photos/safe.svg"><br>&nbsp;Active corona cases in '+country+' is relatively low</fieldset>'
                }
                break;
                }
            }
        f1 = 0;
    })
    }
    })
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