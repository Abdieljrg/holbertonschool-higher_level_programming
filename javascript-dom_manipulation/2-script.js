// select div element with id "red_header"
const redHeaderElement = document.querySelector('#red_header');

// add click event listener to div element
redHeaderElement.addEventListener('click', () => {
  // select <header> element
  const headerElement = document.querySelector('header');
  
  // add class "red" to header element
  headerElement.classList.add('red');
});