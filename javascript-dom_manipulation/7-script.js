// URL to fetch movie data
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// fetch data from URL
fetch(url)
  .then(response => {
    // check if response is ok (status in range 200-299)
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // parse JSON from response
    return response.json();
  })
  .then(data => {
    // get list of films from JSON data
    const films = data.results;
    
    // select "ul" element with id "list_movies"
    const listMoviesElement = document.querySelector('#list_movies');
    
    // iterate over films and create "li" element for each title
    films.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(error => {
    // handle errors that occurred in fetch operation
    console.error('There has been a problem with your fetch operation:', error);
  });
