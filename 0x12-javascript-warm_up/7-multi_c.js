#!/usr/bin/node
const convertNumber = parseInt(process.argv[2]);
if (isNaN(convertNumber) === true) {
  console.log('Missing number of occurences')
} else {
	for (let index = 0; index < convertNumber; index++) {
	  console.log('C is fun');
	}
}
