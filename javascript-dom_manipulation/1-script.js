// select div element with id "red_header"
const redHeaderElement = document.querySelector('#red_header');

// add click event listener to div element
redHeaderElement.addEventListener('click', () => {
  // select header element
  const headerElement = document.querySelector('header');
  
  // change the text color to red
  headerElement.style.color = '#FF0000';
});
