$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, statusText, xhr) {
  $('DIV#hello').text(data.hello);
});