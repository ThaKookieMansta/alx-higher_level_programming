#!/usr/bin/node
const mainDictionary = require('./101-data').dict;
const myDictionary = {};
for (const key in mainDictionary) {
  if (myDictionary[mainDictionary[key]] === undefined) {
    myDictionary[mainDictionary[key]] = [key];
  } else {
    myDictionary[mainDictionary[key]].push(key);
  }
}
console.log(myDictionary);
