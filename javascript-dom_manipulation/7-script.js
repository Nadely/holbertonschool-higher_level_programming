const elemTitle = document.querySelector('#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('The request was unsuccessful.');
    }
  return response.json();
  })
  .then(data => {
    const movies = data.results;
    movies.forEach(movie => {
      const title = movie.title;
      const li = document.createElement('li');
      li.textContent = title;
      elemTitle.appendChild(li);
    });
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
