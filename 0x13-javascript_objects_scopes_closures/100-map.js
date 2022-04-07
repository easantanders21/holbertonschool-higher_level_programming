#!/usr/bin/node
const baseList = require('./100-data').list;
console.log(baseList);
const newList = function maping () {
  return baseList.map((value, index) => value * index);
};
console.log(newList());
