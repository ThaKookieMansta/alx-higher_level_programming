#!/usr/bin/node
const mainDictionary = require ('./101-data');
const myDictionary = {};
for (const k in mainDictionary) {
  if (myDictionary[mainDictionary[k]] === undefined) {
    myDictionary[mainDictionary[k]] = [k];
  } else {
    myDictionary[mainDictionary[k]].push(k);
  }
}
console.log(myDictionary);
