#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const position of list) {
    if (position === searchElement) {
      occurences++;
    }
  }
  return occurences;
};
