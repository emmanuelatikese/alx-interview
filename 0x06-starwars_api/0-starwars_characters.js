#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request.get(url, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const bodyJson = JSON.parse(data.body).characters;
  bodyJson.forEach(x => {
    request.get(x, (err, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const people = JSON.parse(body.body);
      console.log(people.name);
    });
  });
});
