#!/usr/bin/node
exports.converter = function (base) {
  // return (base.toString(base));
  return (number) => number.toString(base);
};

/*
exports.converter = (base) => (num) => num.toString(base);

exports.converter = function (base) {
    return (num) => num.toString(base);
  };

exports.converter = function (base) {
    return function (num) {
      return num.toString(base); //interna
    };
  };
*/
