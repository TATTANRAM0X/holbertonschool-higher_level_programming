$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, statusText, xhr) {
  $('DIV#character').text(data.name);
});