#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log(1);
} else {
  const fac = factorial(parseInt(args[2]));
  console.log(fac);
}

function factorial (n) {
  if (n === 1) { return 1; } else { return (n * factorial(n - 1)); }
}
