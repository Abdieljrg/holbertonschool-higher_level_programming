// select div element with id "update_header"
const updateHeaderElement = document.querySelector('#update_header');

// add click event listener to div element
updateHeaderElement.addEventListener('click', () => {
  // select <header> element
  const headerElement = document.querySelector('header');
  
  // update text content of header element
  headerElement.textContent = 'New Header!!!';
});
