document.addEventListener('DOMContentLoaded', function() {
  const data = document.querySelector('#hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error('The request was unsuccessful.');
      }
      return response.json();
    })
    .then(dataHello => {
      const translate = dataHello.hello;
      data.textContent = translate;
    })
    .catch(error => {
      console.error('An error occurred:', error);
    });
});
