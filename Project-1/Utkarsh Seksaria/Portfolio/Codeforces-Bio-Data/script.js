var title = $(".font2");
console.log(title);
var handle = 'utkarsh05';
function display() {
    console.log('functin called');
     handle = document.getElementById("input").value;
    if(handle=='undefined' || handle=='null' || handle == '') handle = 'utkarsh05';
    console.log(handle);
    for (var i = 0; i < title.length; i++) {
        title[i].innerText = "Calculating.....";
    }
    function work(data) {
        console.log("data is ", data.result[0]);
        var first = data.result[0].firstName;
        first += " ";
        if (data.result[0].lastName != null) first += data.result[0].lastName;
        title[0].innerText = handle;
        console.log("first", first);
        console.log(first.length);
        title[1].innerText = first;
        if (title[1].innerText == "undefined")
            title[1].innerText = "No name found on codeforces";
        var rating = data.result[0].rating;
        title[2].innerText = rating;
        var titlee = data.result[0].rank;
        function jsUcfirst(titlee) {
            return titlee.charAt(0).toUpperCase() + titlee.slice(1);
        }
        title[3].innerText = jsUcfirst(titlee);
        var maxrating = data.result[0].maxRating;
        title[4].innerText = maxrating;
    }
    $.ajax({
        url: "https://codeforces.com/api/user.info?handles=" + handle,
        method: "GET",
        success: work,
    });

    function contests(data) {
        var numcontest = data.result.length;
        title[5].innerText = numcontest;
        var maxrank = 1000000000;
        var bestchange = -100000;
        var neww = true;
        for (var j = 0; j < data.result.length; j++) {
            var tem = data.result[j].rank;
            if (tem < maxrank) maxrank = tem;
            var newrating = data.result[j].newRating;
            var oldrating = data.result[j].oldRating;
            var change = newrating - oldrating;
            if (j == 0 && change > 1100) neww = false;
            if (neww == true) {
                if (j == 0) change -= 500;
                else if (j == 1) change -= 350;
                else if (j == 2) change -= 250;
                else if (j == 3) change -= 150;
                else if (j == 4) change -= 100;
                else if (j == 5) change -= 50;
            }
            if (change < 1000) if (change > bestchange) bestchange = change;
        }
        title[6].innerText = maxrank;
        title[7].innerText = bestchange;
    }

    $.ajax({
        url: "https://codeforces.com/api/user.rating?handle=" + handle,
        method: "GET",
        success: contests,
    });

    function problems(data) {
        var ans = 0;
        var acnt = 0,
            bcnt = 0,
            ccnt = 0,
            dcnt = 0,
            ecnt = 0,
            fcnt = 0,
            gcnt = 0,
            hcnt = 0,
            icnt = 0,
            jcnt = 0,
            tcnt = 0;
        var prob = new Set([]);
        var index = new Set([]);
        title[9].innerText = data.result.length;
        for (var i = 0; i < data.result.length; i++) {
            index.add(data.result[i].problem.index);
            var name = data.result[i].problem.name;
            if (prob.has(name) == false) {
                if (data.result[i].verdict == "OK") {
                    tcnt++;
                }
                prob.add(name);
            }
        }
        title[8].innerText = tcnt;
    }
    $.ajax({
        url:
            "https://codeforces.com/api/user.status?handle=" +
            handle +
            "&from=1&count=100000",
        method: "GET",
        success: problems,
    });
}
var tem= 'utkarsh05';
display();
var button = document.getElementById("button");
// console.log('handle is',handle);
button.addEventListener("click", display);
