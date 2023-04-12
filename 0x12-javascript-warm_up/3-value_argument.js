#!/usr/bin/node
/* eslint semi: ["error", "always"] */
/* eslint-disable camelcase */

const [, arg] = process.argv;

if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}

