-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, IFNULL(tv_genres.name, NULL) AS name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, IFNULL(tv_genres.name, NULL) ASC;
