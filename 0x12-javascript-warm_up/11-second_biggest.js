#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let i = 2;
  let sec = 0;
  let first = 0;
  while (i <= args.length) {
    if (args[i] > first) {
      sec = first;
      first = args[2];
    }
    i++;
  }
  console.log(sec);
}
