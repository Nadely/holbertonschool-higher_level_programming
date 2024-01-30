const colorHeader = document.querySelector('#red_header');

if (colorHeader) {
  colorHeader.addEventListener('click', function() {
    colorHeader.style.color = '#FF0000'
  });
}
