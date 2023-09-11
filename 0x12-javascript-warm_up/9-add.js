#!/usr/bin/node
const firstNum = Number(process.argv[2]);
const secNum = Number(process.argv[3]);

function add (a, b) {
  const result = a + b;
  return result;
}

console.log(add(firstNum, secNum));
