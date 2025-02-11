#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, response) => console.log(`code: ${response && response.statusCode}`));
