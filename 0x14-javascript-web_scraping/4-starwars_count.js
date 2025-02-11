#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      return acc + (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? 1 : 0);
    }, 0);
    console.log(count);
  }
});
