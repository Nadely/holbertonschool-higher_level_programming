const element = document.querySelector('#add_item');

element.addEventListener('click', function() {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  const list = document.querySelector('.my_list');
  list.appendChild(newItem);
});
