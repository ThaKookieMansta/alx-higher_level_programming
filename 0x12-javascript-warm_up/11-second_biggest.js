#!/usr/bin/node
const myArgs = process.argv;
const myArray = [];
if (myArgs.length === 2 || myArgs.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < myArgs.length; i++) {
    myArray.push(Number(myArgs[i]));
  }
  const biggestIndex = myArray.indexOf(Math.max(...myArray));
  myArray.splice(biggestIndex, 1);
  console.log(Math.max(...myArray));
}
