#!/usr/bin/node
const x = process.argv[2];
function fact (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}
console.log(fact(parseInt(x)));
