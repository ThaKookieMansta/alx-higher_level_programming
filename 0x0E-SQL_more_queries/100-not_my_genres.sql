-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT `name`
  FROM `tv_genres` AS genres
       INNER JOIN `tv_show_genres` AS shows
       ON genres.`id` = shows.`genre_id`

       INNER JOIN `tv_shows` AS tv
       ON shows.`show_id` = tv.`id`
       WHERE genres.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS genres
	             INNER JOIN `tv_show_genres` AS shows
		     ON genres.`id` = shows.`genre_id`

		     INNER JOIN `tv_shows` AS tv
		     ON shows.`show_id` = tv.`id`
		     WHERE tv.`title` = "Dexter")
 ORDER BY genres.`name`;
