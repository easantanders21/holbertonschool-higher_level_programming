#!/usr/bin/node
const args = process.argv;
const array_sort = [];
if (args.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  while (args[i]) {
    array_sort.push(parseInt(args[i]));
    i++;
  }
  array_sort.sort(compareNumbers);
  console.log(array_sort[array_sort.length - 2]);
}

function compareNumbers (a, b) {
  return a - b;
}
