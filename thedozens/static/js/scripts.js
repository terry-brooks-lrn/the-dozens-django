// Inital Joke On Load
$.getJSON("https://the-dozens.onrender.com/insult", response => {
  $("#joke").text(
    Object.values(response)[0]
  );
});
// On-Demand Joke Load
const place_joke = () => {
  $.getJSON("https://the-dozens.onrender.com/insult", response => {
  $("#joke").text(
    Object.values(response)[0]
  );
});
};
flexFontJoke = function () {
    var divs = document.getElementsById("joke");
    for(var i = 0; i < divs.length; i++) {
        var relFontsize = divs[i].offsetWidth*0.05;
        divs[i].style.fontSize = relFontsize+'px';
    }
};
window.onload = function(event) {
    flexFontJoke();
};
window.onresize = function(event) {
    flexFontJoke();
};
