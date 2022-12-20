#!/usr/bin/node
const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  args.sort(comparison);

  num = (args[args.length - 2]);
  console.log(num);
  console.log(args);
}

function comparison (a, b) {
  return a - b;
}
