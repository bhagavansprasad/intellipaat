--Renaming objects(table, database , column)
--Schema in SQl server 
--IMPORT and export
--Filter in SQL server 
--################################################################
Create database SQLDEMO

use SQLDEMO

CREATE TABLE Department
  (
      did INT,
      ename VARCHAR(50) ,
      gender VARCHAR(50) ,
      salary INT ,
      dept VARCHAR(50) 
   )

INSERT INTO Department  VALUES
  (1, 'David', 'Male', 5000, 'Sales'),
  (5, 'Shane', 'Female', 5500, 'Finance'),
  (6, 'Shed', 'Male', 8000, 'Sales'),
  (7, 'Vik', 'Male', 7200, 'HR'),
  (2, 'Jim', 'Female', 6000, 'HR'),
  (13, 'Julie', 'Female', 7100, 'IT'),
  (14, 'Elice', 'Female', 6800,'Marketing'),
  (3, 'Kate', 'Female', 7500, 'IT'),
  (4, 'Will', 'Male', 6500, 'Marketing'),
  (10, 'Laura', 'Female', 6300, 'Finance'),
  (11, 'Mac', 'Male', 5700, 'Sales'),
  (12, 'Pat', 'Male', 7000, 'HR'),
  (8, 'Vince', 'Female', 6600, 'IT'),
  (9, 'Jane', 'Female', 5400, 'Marketing'),
  (15, 'Wayne', 'Male', 6800, 'Finance')

  
INSERT INTO Department  VALUES
  (16, 'David rotenberg', 'Male', 5000, 'Sales')

  SELECT * FROM Department

  update Department
  set ename = 'balgeet'
  where did =1
--########################################
--Schema 
Create database DEmo1

use demo1

Create table HR(id int, age int, phnum int)
Create table salary(id int, age int, phnum int)
Create table deduction(id int, age int, phnum int)
Create table loans(id int, age int, phnum int)
Create table sales(id int, age int, phnum int)
Create table fin(id int, age int, phnum int)
Create table marketing (id int, age int, phnum int)
Create table product(id int, age int, phnum int)
Create table grossincome(id int, age int, phnum int)
Create table profit(id int, age int, phnum int)
Create table loss(id int, age int, phnum int)
Create table dbo.region(id int, age int, phnum int)
Create table orders(id int, age int, phnum int)





Create database DEmo2

use demo2

--Create schema schemaname

Create schema HR


Create table HR.HR(id int, age int, phnum int)
Create table HR.salary(id int, age int, phnum int)
Create table HR.deduction(id int, age int, phnum int)
Create table HR.loans(id int, age int, phnum int)
Create table HR.sales(id int, age int, phnum int)

Create schema fin
Create table fin.fin(id int, age int, phnum int)
Create table fin.marketing (id int, age int, phnum int)
Create table fin.product(id int, age int, phnum int)
Create table fin.grossincome(id int, age int, phnum int)

 
Create schema sales

Create table sales.profit(id int, age int, phnum int)
Create table sales.loss(id int, age int, phnum int)
Create table sales.region(id int, age int, phnum int)
Create table sales.orders(id int, age int, phnum int)





Create table test(id int, age int, phnum int)

--Moving the table from one schem ato another (not recommended)
alter schema hr  transfer dbo.test
alter schema hr  transfer dbo.test


--alter schema  to make the default as a hr 
	ALter  user [read]  with default_schema =hr
	
	ALter  user [read]  with default_schema =hr


create database [database]
--###############################################################
--IMPORT and export

select * from Department
select * from [empdetail]


Create database [database]
--######################################################################
--Renaming database
--Syntax: alter database [OLD database name]   modify name =[New database name]
	alter database [database]  modify name =TestSQL

--Renaming a table 
--Syntax: exec Sp_rename 'schema.oldtablename', 'newtablename'
	exec Sp_rename '[dbo].[importedata]', 'hr'

--Renaming a Column 
--Syntax: exec Sp_rename 'tablename.oldColumnName', 'NewColumnName', 'column'
	exec Sp_rename 'dbo.hr.empid', 'employeeid', 'column'

--######################################################################
Select * from Department

use AdventureWorks2022
select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID=291

 --Where using and / or operation
	select BusinessEntityID,FirstName,LastName
	 from person.person  where FirstName='david' and BusinessEntityID=17517





	 
	select BusinessEntityID,FirstName,LastName
	 from person.person  where FirstName='david' and  LastName='barber'
	 and BusinessEntityID=403 

	 	 
	select BusinessEntityID,FirstName,LastName
	 from person.person  where FirstName='david' and BusinessEntityID=403 
	 or LastName='abel'











	 	select BusinessEntityID,FirstName,LastName
	 from person.person  where FirstName='david' or  LastName='Adams'


select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID=291 
 or  BusinessEntityID=22
 or  BusinessEntityID=2222
 or  BusinessEntityID=22222
 or  BusinessEntityID=2
 or  BusinessEntityID=2222
 or  BusinessEntityID=222222

 --IN 

 select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID in(1, 21, 23 , 754, 345)

  select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID  not in(285,293,295,2170,38,211,2357)
 --equals to 
  select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID =285
 --Not equals
  select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID <>285

   select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID !=285

 --greater than 
   select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID >285

  --greater than  equal to
   select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID >=285

  --less than 
   select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID <285

  --less than  equal to
   select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID <=285

 --##########################################################
 --between
    select BusinessEntityID,FirstName,LastName
 from person.person
 where BusinessEntityID between  500 and 700

 
select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where ModifiedDate between '2009-01-07 00:00:00.000' and '2010-01-07 00:00:00.000'


 
select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where FirstName between 'a' and 'd'
  order by FirstName


  update person.person
  set FirstName ='de'
   where BusinessEntityID=19757

--##########################################################
--like % , _
select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where FirstName like 'D%'


 select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where FirstName like 'Da%'

  select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where FirstName like 'Ab%'


   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where FirstName like '%ed'



    select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where FirstName like '%OM%'



     select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where BusinessEntityID like '%111%'

 
     select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person
 where ModifiedDate like '%2009%'







 --Like _
 tom
 ___
 
   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person  where FirstName like '___'

 
 
   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person  where FirstName like '____'





 
 
   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person  where FirstName like '%A_i%'

   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person  where FirstName like '%A_i%'

 
   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person  where FirstName like 'A_i__'

 --##############################################################

 use AdventureWorks2022
  where BusinessEntityID index
   select BusinessEntityID,FirstName,LastName, ModifiedDate
 from person.person where FirstName like 'A_i__'



























































































































































































































































































































