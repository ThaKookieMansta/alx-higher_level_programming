#!/usr/bin/node
exports.esrever = function (list) {
  const myReverseList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myReverseList.push(list[i]);
  }
  return myReverseList;
};
