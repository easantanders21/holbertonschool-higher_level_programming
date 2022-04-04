#!/usr/bin/node
const args = process.argv;
let i = 2;
const array = [];
if (args.length <= 3) {
  console.log(0);
} else {
  while (args[i]) {
    array.push(parseInt(args[i]));
    i++;
  }
  array.sort(compareNumbers);
  console.log(array[array.length - 2]);
}

function compareNumbers (a, b) {
  return a - b;
}
