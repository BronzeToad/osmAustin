------------------------------------------------------------------------------
-- WGU - Udacity: Data Wrangling
-- OpenStreetMap - ATX
-- Get osmDB table sizes
------------------------------------------------------------------------------

SELECT name AS table_name
     , CASE
           WHEN bytes < 1024 THEN (bytes || ' B')
           WHEN kilobytes < 1024 THEN ROUND(kilobytes, 2) || ' KB'
           ELSE ROUND(megabytes, 2) || ' MB' END AS table_size
FROM (
         SELECT name
              , SUM(payload) as bytes
              , CAST(SUM(payload) AS FLOAT) / 1024 AS kilobytes
              , (CAST(SUM(payload) AS FLOAT) / 1024) / 1024 AS megabytes
         FROM stats
         GROUP BY name
     )
ORDER BY bytes DESC;





/*  ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  /
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/  */
