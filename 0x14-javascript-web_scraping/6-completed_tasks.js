#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.reduce((acc, task) => {
      if (task.completed) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(completedTasks);
  }
});
