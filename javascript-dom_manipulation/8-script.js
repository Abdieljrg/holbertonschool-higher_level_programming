// function to fetch and update hello text
function fetchAndUpdateHello() {
    // url to fetch hello translation
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    // fetch data from the url
    fetch(url)
      .then(response => {
        // check if response is ok (status in range 200-299)
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // parse the json from response
        return response.json();
      })
      .then(data => {
        // get the hello translation from json data
        const helloText = data.hello;
        
        // select the <div> element with id "hello"
        const helloElement = document.querySelector('#hello');
        
        // update text content of <div> with hello translation
        helloElement.textContent = helloText;
      })
      .catch(error => {
        // handle any errors that occurred during fetch operation
        console.error('There has been a problem with your fetch operation:', error);
      });
  }
  
  // wait until DOM is fully loaded
  document.addEventListener('DOMContentLoaded', fetchAndUpdateHello);