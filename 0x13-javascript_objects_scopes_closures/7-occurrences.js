#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let noOfOccurences = 0;
  for (const i of list) {
    if (i === searchElement) {
      noOfOccurences++;
    }
  }
  return noOfOccurences;
};
