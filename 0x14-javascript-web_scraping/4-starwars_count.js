#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response, body) => {
  console.log(
    error ||
    JSON.parse(body).results.filter((movie) =>
      movie.characters
        .includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length
  );
});
