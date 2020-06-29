/*
create sample database for testing CRUD transactions using Python Flask
*/
use CRUD

IF OBJECT_ID('dbo.tbl_entity', 'U') IS NOT NULL 
  DROP TABLE dbo.tbl_entity; 

create table tbl_entity
	(
	id INT identity(1,1) not null 
	,name nvarchar(30)
	,lastname nvarchar(50)
	)

insert into tbl_entity (name, lastname) values ('paul', 'huizinga')
insert into tbl_entity (name, lastname) values ('ilse', 'huizinga')
insert into tbl_entity (name, lastname) values ('meike', 'huizinga')
insert into tbl_entity (name, lastname) values ('marjan', 'willemse')

select * from tbl_entity

