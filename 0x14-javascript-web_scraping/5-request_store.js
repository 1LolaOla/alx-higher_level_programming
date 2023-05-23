#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`The response body has been stored in ${filePath}.`);
      }
    });
  }
});
