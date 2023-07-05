"use strict";


function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }

  function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }



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


var darkTheme = {
    main: "is-dark",
    body: "body-black",
    footer:"my_footer-black",
    text: "all-text-white",
    SVG: document.getElementById("toggle-moon-id")
}

var lightTheme = {
    main: "is-light",
    body: "body-white",
    footer:"my_footer-white",
    text: "all-text-black",
    SVG: document.getElementById("toggle-sun-id")
}

var themeFromCookie = getCookie("color_theme");
var currentTheme = themeFromCookie == "dark" ? darkTheme : lightTheme;
var themeForChange = themeFromCookie == "dark" ? lightTheme : darkTheme;

var colorSwitch = document.getElementById("ColorThemeSwitch");



colorSwitch.onclick = function() {

    for (var [key, value] of Object.entries(currentTheme)) {
        if (key == "SVG") {
            switchVisibility(value, themeForChange[key]);
        } else {
            toggleColorTheme(value, themeForChange[key]);
        }
      }
      let temp = currentTheme;
      currentTheme = themeForChange;
      themeForChange = temp;

      setCookie("color_theme", themeFromCookie == "dark" ? "light" : "dark", 2);
      themeFromCookie = themeFromCookie == "dark" ? "light" : "dark";

      console.log(getCookie("color_theme"));

}

document.addEventListener("DOMContentLoaded", function () {
    if (getCookie("color_theme") == "light") {
        let temp = currentTheme;
        currentTheme = themeForChange;
        themeForChange = temp;

        colorSwitch.click();
        setCookie("color_theme", "light" , 2);
        themeFromCookie = "light";
    }

});