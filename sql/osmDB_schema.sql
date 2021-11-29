------------------------------------------------------------------------------
-- WGU - Udacity: Data Wrangling
-- OpenStreetMap - ATX
-- osmDB schema
------------------------------------------------------------------------------

create table nodes
(
    id        integer not null
        constraint nodes_pk
            primary key,
    lat       real,
    lon       real,
    user      text,
    uid       integer,
    version   integer,
    changeset integer,
    timestamp text
);


create table nodes_tags
(
    id    integer
        references nodes,
    key   text,
    value text,
    type  text
);


create table ways
(
    id        integer not null
        constraint ways_pk
            primary key,
    user      text,
    uid       integer,
    version   text,
    changeset integer,
    timestamp text
);


create table ways_nodes
(
    id       integer not null
        references ways,
    node_id  integer not null
        references nodes,
    position integer not null
);


create table ways_tags
(
    id    integer not null
        references ways,
    key   text    not null,
    value text    not null,
    type  text
);





/*  ____                           ______                __
   / __ )_________  ____  ____ ___/_  __/___  ____ _____/ /
  / __  / ___/ __ \/ __ \/_  // _ \/ / / __ \/ __ `/ __  /
 / /_/ / /  / /_/ / / / / / //  __/ / / /_/ / /_/ / /_/ /
/_____/_/   \____/_/ /_/ /___|___/_/  \____/\__,_/\__,_/  */
