create database python_db;

use python_db;

create table users(
id int primary key auto_increment,
uname varchar(30),
age int,
city varchar(30)
);

select * from users;
