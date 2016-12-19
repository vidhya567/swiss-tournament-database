-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.



CREATE TABLE playerinfo(pid serial PRIMARY KEY,pname varchar(50),won integer,played integer);
CREATE TABLE results(round integer,a integer,b integer,won integer);
