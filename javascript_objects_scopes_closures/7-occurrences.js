#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const position in list) {
    if (list[position] === searchElement) {
      occurences++;
    }
  }
  return (occurences);
};
