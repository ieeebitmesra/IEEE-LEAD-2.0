let index = 0;
let msg = '᚛W𝖊ɭc𐍉ϻ𝖊 T𐍉 M𝕪 Ƥ𐍉rτfolΐo᚜'; 
let rate = 150;
function display() {
  if (index < msg.length) {
    document.getElementById("msgs").innerHTML += msg.charAt(index);
    index++;
    setTimeout(display, rate);
  }
}