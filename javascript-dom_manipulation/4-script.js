// select div element with id "toggle_header"
const toggleHeaderElement = document.querySelector('#toggle_header');

// add click event listener to the div element
toggleHeaderElement.addEventListener('click', () => {
  // select header element
  const headerElement = document.querySelector('header');

  // check current class and toggle it
  if (headerElement.classList.contains('red')) {
    // remove 'red' and add 'green'
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    // remove 'green' and add 'red'
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});