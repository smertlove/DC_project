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

let csrfToken = getCookie('X-CSRFToken');

fetch(
    '',  // ПОЛНЫЙ URL ВЬЮХИ ДЛЯ ОБРАБОТКИ ЗАПРОСА
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Requested-With' : 'XMLHttpRequest',
        'X-CSRFToken': csrfToken
      },
      body: '',  // КОНТЕНТ КОММЕНТА
    })
