//This function will get the covid data of user entered country
const getEnteredCountryData = async () => {

    const response = await fetch(`https://api.covid19api.com/live/country/${enteredCountry}`);

    if (response.status !== 200) {
        //Error Handling in case of Invalid country entered by user
        document.querySelector("#myHeading").innerText = "Invalid Country";
        throw new Error('cannot fetch data');

    }

    const data = await response.json();

    return data;


};


//Globally declared for
//accessibility over whole code
let state;
let enteredCountry;

//we target submit button
let submitButton = document.querySelector(".sumbiter");

//this event listener will get the user entered values 
//and get the data of entered data and then  we will put
//the data on website
submitButton.addEventListener("click", () => {
    state = document.querySelector(".userState").value;
    enteredCountry = document.querySelector(".userCountry").value;


    getEnteredCountryData()
        .then((data) => {
            //Error Handling in case of Invalid country entered by user
            if (data.length == 0) {
                document.querySelector("#myHeading").innerText = "Invalid Country";
                return;
            }


            //Search province from country data            
            let i;
            let arr = [];
            let j = 0;
            for (i = data.length - 1; j !== 2 && i >= 0; i--) {

                if (data[i].Province === state) {
                    arr[j] = data[i];
                    j += 1;
                }

            }



            final = arr[0];
            init = arr[1];

            //Error handling in case of invalid state entered by user                
            if (final === undefined) {
                document.querySelector("#myHeading").innerText = "Invalid State";
            }

            else {
                document.querySelector("#myHeading").innerText = "Covid data of the above State";
            }

            //We enter the data we got ; into our website
            let x = final.Deaths;
            let y = document.querySelector(".totDeathNum");
            y.innerText = `${x}`;

            x = final.Confirmed;
            y = document.querySelector(".totConfNum");
            y.innerText = `${x}`;

            x = final.Recovered;
            y = document.querySelector(".totRecNum");
            y.innerText = `${x}`;

            x = final.Deaths - init.Deaths;
            y = document.querySelector(".newDeathNum");
            y.innerText = `${x}`;

            x = final.Recovered - init.Recovered;
            y = document.querySelector(".newRecNum");
            y.innerText = `${x}`;

            x = final.Confirmed - init.Confirmed;
            y = document.querySelector(".newConfNum");
            y.innerText = `${x}`;


        })
        .catch(err => console.log('rejected :', err.message));
});



