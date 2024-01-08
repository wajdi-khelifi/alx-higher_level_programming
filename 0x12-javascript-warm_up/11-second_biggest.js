#!/usr/bin/node
const arg = process.argv.slice[2];
let secondMax = 0;

if (arg.length > 1) {
  const args = arg.map(Number);
  args.sort((a, b) => b - a);
  secendMax = args[1];
}
console.log(secondMax);
