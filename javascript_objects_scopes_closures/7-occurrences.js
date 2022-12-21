#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
let occurences = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
        occurences++;
    }
  }
  return (occurences);
};