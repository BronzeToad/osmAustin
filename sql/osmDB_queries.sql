------------------------------------------------------------------------------
-- WGU - Udacity: Data Wrangling
-- OpenStreetMap - ATX
-- osmDB other queries
------------------------------------------------------------------------------

-- number of unique contributors
SELECT COUNT(DISTINCT uid) AS contributors
FROM  (
          SELECT uid FROM nodes
        UNION ALL
          SELECT uid FROM ways
      );


-- top 3 contributors
SELECT  uid,
        user,
        COUNT(*) AS contributions
FROM  (
          SELECT uid, user FROM nodes
        UNION ALL
          SELECT uid, user FROM ways
      )
GROUP BY uid, user
ORDER BY contributions DESC
LIMIT 3;


-- top 10 contributors
SELECT  uid,
        user,
        COUNT(*) AS contributions
FROM  (
          SELECT uid, user FROM nodes
        UNION ALL
          SELECT uid, user FROM ways
      )
GROUP BY uid, user
ORDER BY contributions DESC
LIMIT 10;


-- contributions per year
SELECT  year,
        COUNT(*) AS contributions
FROM  (
          SELECT SUBSTR(timestamp, 1, 4) AS year FROM nodes
        UNION ALL
          SELECT SUBSTR(timestamp, 1, 4) AS year FROM ways
      )
GROUP BY year
ORDER BY year;


-- years with the most contributions
SELECT  year,
        COUNT(*) AS contributions
FROM  (
          SELECT SUBSTR(timestamp, 1, 4) AS year FROM nodes
        UNION ALL
          SELECT SUBSTR(timestamp, 1, 4) AS year FROM ways
      )
GROUP BY year
ORDER BY contributions DESC
LIMIT 3;


-- contribution frequency by month
SELECT  CASE
          WHEN mon = '01' THEN 'January'
          WHEN mon = '02' THEN 'February'
          WHEN mon = '03' THEN 'March'
          WHEN mon = '04' THEN 'April'
          WHEN mon = '05' THEN 'May'
          WHEN mon = '06' THEN 'June'
          WHEN mon = '07' THEN 'July'
          WHEN mon = '08' THEN 'August'
          WHEN mon = '09' THEN 'September'
          WHEN mon = '10' THEN 'October'
          WHEN mon = '11' THEN 'November'
          WHEN mon = '12' THEN 'December'
        END AS month,
        COUNT(*) AS contributions
FROM  (
          SELECT SUBSTR(timestamp, 6, 2) AS mon FROM nodes
        UNION ALL
          SELECT SUBSTR(timestamp, 6, 2) AS mon FROM ways
      )
GROUP BY month
ORDER BY mon;


-- months with the most contributions
SELECT  CASE
          WHEN mon = '01' THEN 'January'
          WHEN mon = '02' THEN 'February'
          WHEN mon = '03' THEN 'March'
          WHEN mon = '04' THEN 'April'
          WHEN mon = '05' THEN 'May'
          WHEN mon = '06' THEN 'June'
          WHEN mon = '07' THEN 'July'
          WHEN mon = '08' THEN 'August'
          WHEN mon = '09' THEN 'September'
          WHEN mon = '10' THEN 'October'
          WHEN mon = '11' THEN 'November'
          WHEN mon = '12' THEN 'December'
        END AS month,
        COUNT(*) AS contributions
FROM  (
          SELECT SUBSTR(timestamp, 6, 2) AS mon FROM nodes
        UNION ALL
          SELECT SUBSTR(timestamp, 6, 2) AS mon FROM ways
      )
GROUP BY month
ORDER BY contributions
LIMIT 3;


-- average monthly and yearly contributions
SELECT  SUM(contributions) / COUNT(DISTINCT year) AS avg_yearly,
        SUM(contributions) / COUNT(DISTINCT month) AS avg_monthly
FROM  (
        SELECT  year,
                month,
                COUNT(*) AS contributions
        FROM  (
                SELECT  SUBSTR(timestamp, 1, 4) AS year,
                        SUBSTR(timestamp, 1, 7) AS month
                FROM nodes
                UNION ALL
                SELECT  SUBSTR(timestamp, 1, 4) AS year,
                        SUBSTR(timestamp, 1, 7) AS month
                FROM ways
              )
        GROUP BY year, month
      );


-- count the ways
SELECT COUNT(*) AS count_ways
FROM ways;


-- common way tags
SELECT  key,
        COUNT(*) AS count_ways
FROM ways_tags
GROUP BY key
HAVING count_ways > 100000
ORDER BY count_ways DESC;


-- count the nodes
SELECT COUNT(*) AS count_nodes
FROM nodes;


-- common node tags
SELECT  key,
        COUNT(*) AS count_nodes
FROM nodes_tags
GROUP BY key
HAVING count_nodes > 10000
ORDER BY count_nodes DESC;


-- common amenities
SELECT  value,
        COUNT(*) AS count
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
HAVING count >= 200
ORDER BY count DESC;


-- restaurant categories
SELECT  value,
        COUNT(*) AS count_restaurants
FROM nodes_tags
WHERE key = 'cuisine'
GROUP BY value
ORDER BY count_restaurants DESC
LIMIT 10;





/*  ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  /
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/  */
