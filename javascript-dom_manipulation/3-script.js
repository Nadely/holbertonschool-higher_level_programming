const toggleHeaderButton = document.getElementById('toggle_header');
const classHeader = document.querySelector('header');

if (classHeader) {
    if (classHeader.classList.length !== 1) {
        console.error("L'élément a plus ou moins d'une classe.");
    } else {
        toggleHeaderButton.addEventListener('click', function() {
            if (classHeader.classList.contains('red')) {
                classHeader.classList.remove('red');
                classHeader.classList.add('green');
            } else {
                classHeader.classList.remove('green');
                classHeader.classList.add('red');
            }
        });
    }
}
