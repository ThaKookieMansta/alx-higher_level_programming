#!/usr/bin/node
const firstArg = process.argv[2];
const newNum = parseInt(firstArg);
if (isNaN(newNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${newNum}`);
}
