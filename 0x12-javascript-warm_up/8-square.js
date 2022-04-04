#!/usr/bin/node
const args = process.argv;
if (!args[2] || isNaN(args[2])) {
  console.log('Missing size');
} else {
  let i = 1;
  while (i <= parseInt(args[2])) {
    console.log('X'.repeat(parseInt(args[2])));
    i++;
  }
}
