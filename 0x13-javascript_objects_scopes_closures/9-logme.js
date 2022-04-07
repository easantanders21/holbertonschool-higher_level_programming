#!/usr/bin/node
const NumArgs = [];
exports.logMe = function (item) {
  let count = 0;
  NumArgs.forEach(Element => {
    count++;
  });
  NumArgs.push(item);
  console.log(count + ': ' + item);
};
