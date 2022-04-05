#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i = 1;
  while (i <= x) {
    theFunction();
    i++;
  }
};
