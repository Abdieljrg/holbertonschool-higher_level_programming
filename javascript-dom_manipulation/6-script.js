// URL fetch character data
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Fetch data from URL
fetch(url)
  .then(response => {
    // Check if response is ok (status in range 200-299)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse JSON from the response
    return response.json();
  })
  .then(data => {
    // Get the character name from the JSON data
    const characterName = data.name;
    
    // Select the <div> element with id "character"
    const characterElement = document.querySelector('#character');
    
    // Update the text content of the <div> with the character name
    characterElement.textContent = characterName;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch operation
    console.error('There has been a problem with your fetch operation:', error);
  });
