-- This script displays the average temp in Farenheit by city
-- ordered by temp
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
