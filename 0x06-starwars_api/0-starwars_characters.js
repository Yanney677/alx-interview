#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

async function starwarsCharacters(filmId) {
  try {
    const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    const response = await request(endpoint);
    const { characters } = JSON.parse(response.body);

    for (const characterUrl of characters) {
      const characterResponse = await request(characterUrl);
      const { name } = JSON.parse(characterResponse.body);
      console.log(name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

const filmId = process.argv[2];
if (!filmId || isNaN(parseInt(filmId))) {
  console.error('Please provide a valid film ID.');
} else {
  starwarsCharacters(filmId);
}
