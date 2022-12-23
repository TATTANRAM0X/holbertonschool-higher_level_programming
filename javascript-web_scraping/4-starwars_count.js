#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;
let count = 0;

request.get(url, function (error, response, body) {
  if (!error) {
    const json = JSON.parse(body).results;
    for (const movie of json) {
      for (const WedgeAntilles of movie.characters) {
        if (WedgeAntilles.includes(id)) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
