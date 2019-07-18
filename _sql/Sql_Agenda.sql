CREATE database if not exists Agenda;
use Agenda;
create table usuario(
id int primary key auto_increment not null,
nome varchar(50) ,
telefone varchar(15) 
);