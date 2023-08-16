-- This script lists all shows contained in the database hbtn_0d_tvshows
SELECT show.`title`, genre.`genre_id`
  FROM `tv_shows` AS show
       LEFT JOIN `tv_show_genres` AS genre
       ON show.`id` = genre.`show_id`
 ORDER BY show.`title`, genre.`genre_id`;
