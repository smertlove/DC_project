"use strict";

// from -- CSS class, to -- CSS class
function toggleColorTheme(from, to) {
    console.log(1);
    return
}

// elem1 -- DOM elem to hide, elem2 -- DOM elem to reveal
function switchVisibility (elem1, elem2) {
    console.log(2);
    return
}

var colorSwitch = document.getElementById("ColorThemeSwitch");
console.log(colorSwitch);
colorSwitch.onclick = function() {
    switchVisibility(1, 2);
    toggleColorTheme(1, 2);
}
