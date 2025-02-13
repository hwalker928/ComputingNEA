function setCookie(name, value) {
  document.cookie = name + "=" + value + "; path=/";
}

function getCookie(name) {
  // Append "=" to the name to search for the cookie
  var name = name + "=";

  // Get an array of cookies by splitting at the ; delimiter
  var cookies = document.cookie.split(";");

  // Loop through the array of cookies
  for (var i = 0; i < cookies.length; i++) {
    // Get the cookie at the position of the loop
    var cookie = cookies[i];

    // Remove any leading spaces
    while (cookie.charAt(0) == " ") cookie = cookie.substring(1, cookie.length);

    // If the cookie is found, return the value
    if (cookie.indexOf(name) == 0)
      return cookie.substring(name.length, cookie.length);
  }

  // If the cookie is not found, return null
  return null;
}
