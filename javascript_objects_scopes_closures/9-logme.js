#!/usr/bin/node

let numArgument = 0;

exports.logMe = function (item) {
  console.log(numArgument + ': ' + item);
  numArgument++;
};
