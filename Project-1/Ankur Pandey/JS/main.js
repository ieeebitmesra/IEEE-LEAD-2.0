let index = 0;
let text = 'Hello..!!'; 
let race = 150;
function hello() {
  if (index < text.length) {
    document.getElementById("hello").innerHTML += text.charAt(index);
    index++;
    setTimeout(hello, race);
  }
}