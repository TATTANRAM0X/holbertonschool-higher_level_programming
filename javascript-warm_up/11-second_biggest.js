#!/usr/bin/node
const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  args.sort(comparison);
  console.log(args[args.length - 2]);
}

function comparison (a, b) {
  return a - b;
}
