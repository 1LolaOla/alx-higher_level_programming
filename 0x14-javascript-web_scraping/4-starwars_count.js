#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

const characterUrl = `${apiUrl}${characterId}`;

request(characterUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const character = JSON.parse(body);
    const moviesWithCharacter = character.films.length;
    console.log(moviesWithCharacter);
  }
});

