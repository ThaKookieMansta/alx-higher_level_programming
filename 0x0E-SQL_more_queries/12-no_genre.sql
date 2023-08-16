-- This script lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT show.`title`, genre.`genre_id`
  FROM `tv_shows` AS show
       LEFT JOIN `tv_show_genres` AS genre
       ON show.`id` = genre.`show_id`
       WHERE genre.`genre_id` IS NULL
 ORDER BY show.`title`, genre.`genre_id`;
