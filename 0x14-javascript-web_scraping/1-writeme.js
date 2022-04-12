#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
fs.writeFile(args[2], args[3], 'utf8', function (err, data) { if (err) { console.log(err); } });
