#!/usr/bin/node
const request = require('request');
const base = 'https://swapi-api.alx-tools.com/api/films/';
request(`${base}${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }
  console.log(JSON.parse(body).title);
});
