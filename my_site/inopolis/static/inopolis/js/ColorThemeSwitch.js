"use strict";

// from -- CSS class, to -- CSS class
function toggleColorTheme(from, to) {

    let elemsToChange = document.getElementsByClassName(from);

    Array.from(elemsToChange).forEach(element => {
        element.classList.remove(from);
        element.classList.add(to);
    });

    return
}



// elem1 -- DOM elem to hide, elem2 -- DOM elem to reveal
function switchVisibility (elem1, elem2) {
    elem2.classList.add("is-hidden");
    elem1.classList.remove("is-hidden");
    return
}


var colorSwitch = document.getElementById("ColorThemeSwitch");
var mainFrom = "is-dark";
var mainTo = "is-light";
var bodyFrom = "body-black";
var bodyTo = "body-white";
var footerFrom = "my_footer-black";
var footerTo = "my_footer-white";
var textFrom = "all-text-white";
var textTo = "all-text-black";

var currentSVG = document.getElementById("toggle-moon-id");
var hiddenSVG = document.getElementById("toggle-sun-id");


colorSwitch.onclick = function() {
    switchVisibility(currentSVG, hiddenSVG);
    let temp = currentSVG;
    currentSVG = hiddenSVG;
    hiddenSVG = temp;

    toggleColorTheme(mainFrom, mainTo);
    temp = mainFrom;
    mainFrom = mainTo;
    mainTo = temp;

    toggleColorTheme(bodyFrom, bodyTo)
    temp = bodyFrom;
    bodyFrom = bodyTo;
    bodyTo = temp;

    toggleColorTheme(footerFrom, footerTo)
    temp = footerFrom;
    footerFrom = footerTo;
    footerTo = temp;

    toggleColorTheme(textFrom, textTo)
    temp = textFrom;
    textFrom = textTo;
    textTo = temp;


}
