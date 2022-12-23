$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, statusText, xhr) {
  data.results.forEach(function (dict) {
    $('UL#list_movies').append('<li>' + dict.title + '</li>');
  });
});