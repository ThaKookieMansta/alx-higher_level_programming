-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS shows
       ON shows.`show_id` = tv.`id`

       LEFT JOIN `tv_genres` AS genres
       ON genres.`id` = shows.`genre_id`
       WHERE tv.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS tv
	             INNER JOIN `tv_show_genres` AS shows
		     ON shows.`show_id` = tv.`id`

		     INNER JOIN `tv_genres` AS genres
		     ON genres.`id` = shows.`genre_id`
		     WHERE genres.`name` = "Comedy")
 ORDER BY `title`;
