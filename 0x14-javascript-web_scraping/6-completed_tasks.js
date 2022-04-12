#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
let flag = 0;
let count = 1;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    const dictionary = {};
    for (const keys in obj) {
      if (obj[keys].completed === true) {
        count++;
        dictionary[obj[keys].userId] = count;
        if (obj[keys].userId !== flag) {
          count = 1;
        }
        flag = obj[keys].userId;
      }
    }
    console.log(dictionary);
  }
});
