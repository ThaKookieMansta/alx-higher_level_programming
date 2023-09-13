#!/usr/bin/node
exports.converter = function (base) {
  return newNum => newNum.toString(base);
};
