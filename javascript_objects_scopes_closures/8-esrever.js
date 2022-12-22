#!/usr/bin/node

exports.esrever = function (list) {
  let last = list.length - 1;
  const array = [];

  for (let first = 0; first < list.length; first++) {
    array[first] = list[last];
    last--;
  }
  return array;
};
