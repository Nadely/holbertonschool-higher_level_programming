const elemCharacter = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('The request was unsuccessful.');
    }
  return response.json();
  })
  .then(data => {
    const nameCharacter = data.name;
    elemCharacter.textContent = nameCharacter;
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
