#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, response, body) {
  if (!error) console.log(JSON.parse(body).title);
});
