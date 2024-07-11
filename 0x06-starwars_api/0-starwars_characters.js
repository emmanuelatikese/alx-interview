#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/3/';
request.get(url, (err, body) => {
  if (err) {
    console.error(`Error: ${err}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  characters.foreach(x => {
    request.get(x, (data) => {
      const charactersName = JSON.parse(data);
      if (charactersName) {
        console.log(charactersName.name);
      }
    });
  });
});
