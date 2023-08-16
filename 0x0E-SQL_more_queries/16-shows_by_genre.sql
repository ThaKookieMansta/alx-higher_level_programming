-- This script lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv.`title`, genres.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS shows
       ON tv.`id` = shows.`show_id`

       LEFT JOIN `tv_genres` AS genres
       ON shows.`genre_id` = genres.`id`
 ORDER BY tv.`title`, genres.`name`;
