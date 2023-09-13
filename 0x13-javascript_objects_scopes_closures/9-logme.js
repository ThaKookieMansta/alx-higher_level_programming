#!/usr/bin/node
let argNum = 0;
exports.logMe = function (item) {
  console.log(`${argNum++}: ${item}`);
};
