#!/usr/bin/node
const firstArg = Number(process.argv[2]);

function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

console.log(factorial(firstArg));
