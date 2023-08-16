--  this script lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv.`title`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_genres` AS shows
       ON tv.`id` = shows.`show_id`

       INNER JOIN `tv_genres` AS genres
       ON genres.`id` = shows.`genre_id`
       WHERE genres.`name` = "Comedy"
 ORDER BY tv.`title`;
