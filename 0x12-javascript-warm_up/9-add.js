#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function Add(a, b) {
  if (isNaN(a) || isNaN(b)) {
	  return (NaN);
  } else {
	  return (parseInt(a) + parseInt(b));
  }
}
  console.log(Add(a, b));
