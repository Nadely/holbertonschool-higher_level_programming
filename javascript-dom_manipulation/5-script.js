const elementUpdate = document.getElementById('update_header');

elementUpdate.addEventListener('click', function() {
  const updateText = document.querySelector('header');
  updateText.textContent = 'New Header!!!';
});
