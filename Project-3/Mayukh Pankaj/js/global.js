
      var data = new Array();
    
      var myForm=document.getElementById('myform')
      myForm.addEventListener('submit',function(e) {
        e.preventDefault()
        var country=document.getElementById('userInput').value
  
        console.log('clicked');
        
        var url="https://api.covid19api.com/total/dayone/country/"+country
        fetch(url)
        .then((res)=>res.json())
        .then((res)=> {
  
            console.log(res);
  
            var length=res.length;
            var index=length-1;
            
            console.log(length)
  
            console.log(res[index]);
  
  
            var country = document.getElementById('country');
  
            var active = document.getElementById('active');
            var confirmed = document.getElementById('confirmed');
            var recovered = document.getElementById('recovered');
            var deceased = document.getElementById('deceased');
  
          
            country.innerHTML= res[index].Country+"'s data";
  
            active.innerHTML= res[index].Active;
            confirmed.innerHTML= res[index].Confirmed;
            recovered.innerHTML= res[index].Recovered;
            deceased.innerHTML= res[index].Deaths;
  
            document.getElementById("panel").style.display = "block";
  
  
            for(var i=0;i<length;i++)
            {
  
              var date = res[i].Date;
  
              date = date.substring(0, 10);
  
              data.push({cases: res[i].Confirmed, date:d3.timeParse("%Y-%m-%d")(date)});
  
  
            }
  
           console.log(data);
  
  
                 var margin = {top: 10, right: 30, bottom: 30, left: 60},
                    width = 300 - margin.left - margin.right,
                    height = 200 - margin.top - margin.bottom;
  
                // append the svg object to the body of the page
                var svg = d3.select("#my_dataviz")
                  .append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                  .append("g")
                    .attr("transform",
                          "translate(" + margin.left + "," + margin.top + ")");
                //x axis
  
                    var x = d3.scaleTime()
                    .domain(d3.extent(data, function(d) { return d.date; }))
                    .range([ 0, width ])
  
                    var x_axis = d3.axisBottom().scale(x).ticks(3);
  
                  svg.append("g")
                    .attr("transform", "translate(0," + height + ")")
                    .call(x_axis)
                   
  
  
                // Add Y axis
                var y = d3.scaleLinear()
                  .domain([0, d3.max(data, function(d) { return d.cases; })])
                  .range([ height, 0 ]);
                svg.append("g")
                  .call(d3.axisLeft(y));
  
  
                  
  
  
                // Add the line
                svg.append("path")
                  .datum(data)
                  .attr("fill", "none")
                  .attr("stroke", "steelblue")
                  .attr("stroke-width", 1.5)
                  .attr("d", d3.line()
                    .x(function(d) { return x(d.date) })
                    .y(function(d) { return y(d.cases) })
                    )
  
  
  
  
  
  
  
  
  
        })
  
    })