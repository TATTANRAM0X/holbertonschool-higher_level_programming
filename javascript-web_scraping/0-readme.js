#!/usr/bin/node
const file = require('fs');

file.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});
