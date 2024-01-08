#!/usr/bin/node
if (!process.argv[2]) {
	console.log('No argument');
} else {
	console.log(typeof process.argv[2]);
}
