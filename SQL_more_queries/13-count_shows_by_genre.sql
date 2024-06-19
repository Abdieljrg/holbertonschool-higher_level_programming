-- Genres with show counts (single SELECT)

SELECT tv_genres.name AS genre, count(tv_genres.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;