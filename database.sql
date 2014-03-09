create database kerengga;
create table category (
  id int not null auto_increment primary key,
  parent_id int,
  player_id int,
  url varchar(500),
  description varchar(500)
 );
