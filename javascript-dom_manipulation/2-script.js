const classRed = document.querySelector('#red_header');

if (classRed) {
  classRed.addEventListener('click', function() {
    classRed.classList.add('red')
  });
}
