-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, IFNULL(tv_show_genres.genre_id, 'NULL') ASC;
