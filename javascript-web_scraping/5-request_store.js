#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (error, body) {
  if (!error) {
    fs.writeFile(file, body.body, 'utf-8', function (fail) {
      if (fail) {
        console.log(fail);
      }
    });
  }
});
