-- create stats table for osmDB
-- stats generated by sqlite3_analyzer

BEGIN;
CREATE TABLE stats(
    name       STRING,           /* Name of table or index */
    path       INTEGER,          /* Path to page from root */
    pageno     INTEGER,          /* Page number */
    pagetype   STRING,           /* 'internal', 'leaf' or 'overflow' */
    ncell      INTEGER,          /* Cells on page (0 for overflow) */
    payload    INTEGER,          /* Bytes of payload on this page */
    unused     INTEGER,          /* Bytes of unused space on this page */
    mx_payload INTEGER,          /* Largest payload size of all cells */
    pgoffset   INTEGER,          /* Offset of page in file */
    pgsize     INTEGER           /* Size of the page */
);
COMMIT;





/*  ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  /
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/  */
