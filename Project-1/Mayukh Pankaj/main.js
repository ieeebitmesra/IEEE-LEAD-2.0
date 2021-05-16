     
            /* navbar */

            function openNav() {
                document.getElementById("mySidenav").style.width = "250px";
              }
              
              function closeNav() {
                document.getElementById("mySidenav").style.width = "0";
              }
              
              
              
                  /* dark theme */
              
                  function darkToggle() {
                 
              
              
                 var element = document.body;
                 element.classList.toggle("dark-mode");
                 
                  
              
                      document.getElementById('dp').src = './images/anon.jfif';
              
               
                  
              
              
                   }
              
              
              
              
              
              
              
                          /*codeforces api */
                      const url1 = 'https://codeforces.com/api/user.info?handles=tourist';
                      const url2 = 'https://codeforces.com/api/user.status?handle=tourist&from=1&count=1000'
              
                      async function getRating(){
                  const response = await fetch(url1);
                  const data = await response.json();
                  if(data.status === "OK" ){
                      document.getElementById('rating').innerHTML = "current rating : " + data.result[0].rating + "<br /> current rank  : " + data.result[0].rank;
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
                          document.getElementById('submissions').innerHTML =  "Problems solved  : "+c+"<br />Total submissions : "+data.result.length;
                  }
              }
              getRating();
              getSubmission();
              /** End of Codeforces API  */
