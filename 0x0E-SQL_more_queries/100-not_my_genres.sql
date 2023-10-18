-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
--    The tv_shows table contains only one record where title = Dexter (but the id can be different)
--    Each record should display: tv_genres.name
--    Results must be sorted in ascending order by the genre name
--    You can use a maximum of two SELECT statement
--    The database name will be passed as an argument of the mysql command

SELECT genres.name
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title != 'Dexter'
UNION
SELECT genres.name
FROM genres
WHERE NOT EXISTS (
    SELECT tv_show_genres.id
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter' AND tv_show_genres.genre_id = genres.id
)
ORDER BY name;