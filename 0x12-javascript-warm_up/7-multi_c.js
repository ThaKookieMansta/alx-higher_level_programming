#!/usr/bin/node
const firstArg = process.argv[2];
const numOfTimes = Number(firstArg);
if (isNaN(numOfTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
