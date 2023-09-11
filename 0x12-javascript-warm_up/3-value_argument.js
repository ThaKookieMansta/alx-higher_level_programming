#!/usr/bin/node
const myVal = process.argv[2];
if (myVal) {
  console.log(myVal);
} else {
  console.log('No argument');
}
