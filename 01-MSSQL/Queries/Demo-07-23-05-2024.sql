--Constraint in SQL server(check , default ,unique , not null, identity)
--Indexing (clustered , non clustered  composite )
--################################################################

create table test( val nvarchar(100))

insert into test  values 
('a'),('A'),('á'),('a'),('Á'),('B')


select * from test




select * from test order by val collate latin1_general_ci_ai

select * from test order by val collate latin1_general_cs_as



--################################################################
Create database DEMO

use DEMO

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
  (NULL, null, null, null,null)
  
INSERT INTO Department  VALUES
  (16, NUll, NUll, 5000, NUll)

  SELECT * FROM Department



--NUll values 
--Duplicate values 
-- column and data type, values  mistmatch 
--not ordered 
-- search not fast 

--Syntax:create table tablename ( columnName Datatype constraint )
CREATE TABLE Department
  (
      did INT not null unique,
      ename VARCHAR(50) not null ,
      gender VARCHAR(50) not null ,
      salary INT not null check(salary >=5000),
	  age tinyint check(age between 18 and 60),
      dept VARCHAR(50)  not null default 'Undefined values'
   )
--Table defnition 
--Syntax: sp_help 'tablname'
	sp_help 'department'

--###########################################
INSERT INTO Department  VALUES
  (1, 'David', 'Male', 5000, 21,'Sales')

  select * from department

--Violation of UNIQUE KEY 
INSERT INTO Department  VALUES
 ( 2, 'David', 'Male', 5000, 21,'Sales')
--Violation of Cannot insert the value NULL into column
 INSERT INTO Department  VALUES
 ( 3, NUll, 'Male',6000, 21,NULL)


 --Violation of INSERT statement conflicted with the CHECK constraint
	INSERT INTO Department  VALUES
  (5, 'Shane', 'Female', 5000,22, 'Finance')

  	INSERT INTO Department  VALUES
  (6, 'Shane', 'Female', 5000,18, 'Finance')


  select * from department
 --Msg 213, Level 16, State 1, Line 110
--Column name or number of supplied values does not match table definition.
  	
	INSERT INTO Department(  did,ename,gender,salary,age)
	VALUES   (7, 'Shane', 'Female', 5000,18)
--########################################
--Scenario 
			CREATE TABLE employee
		  (
			  id INT,
			  name VARCHAR(50) NOT NULL,
			  gender VARCHAR(50) NOT NULL,
			  salary INT NOT NULL,
			  department VARCHAR(50) NOT NULL
		   )
		   			 
--You need to add the constraint to the exisitng table 
		alter table tablename 
		alter column columnname datattype not null

		alter table tablename 
		add constraint constraint_name unique(columnname)
		
		alter table tablename 
		add constraint constraint_name check(col >= values)
				
		alter table tablename 
		add constraint constraint_name default 'values'

--##############################################################
--identity(seed ,increment)

--autoincrement ( numeric data)
 create table token 
 (sno int identity(1,1), cars varchar(10))

 insert into token
 values ('BMW')

 select * from token

 
 insert into token
 values ('audi')
  
 insert into token(sno,cars)
 values (7,'merc')

 --disable the identity 
 set IDENTITY_INSERT token on
   
 insert into token(sno,cars)
 values (77,'merc')

  --Enable the identity 
 set IDENTITY_INSERT token off
  
  insert into token  values ('audi')
  
 
 select * from token

 --##############################
 --Indexing (clustered , non clustered  composite )



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




--Execution plan(CNTRL+M)

--clustered Index(), determine the physical order of data in a tble 
--sort and store data in the asc order, 1 clustered index in 1 table 

--Syntax :CREATE CLUSTERED INDEX index_name ON table_name (column1 );

create clustered index CI_DID on department (did)

  SELECT * FROM Department
  where did =7


    SELECT ename FROM Department
  where ename ='david'

---Non-Clustered Index
  
--Syntax :CREATE  INDEX index_name ON table_name (column1 );

  
create index CI_Ename on department (ename)

 SELECT ename FROM Department
  where ename ='david'
--#########################################################
 SELECT ename, dept, salary FROM Department
where ename='Will' and dept='Marketing' and salary=6500
--Composite index
--Syntax :CREATE  INDEX index_name ON table_name (column1, column2 , column3);

  
	create index CI_threecol on department (ename, dept, salary)


	 SELECT ename, dept, salary FROM Department
	where ename='Will' and dept='Marketing' and salary=6500

	 SELECT ename, dept, salary FROM Department
	where ename='Will' and dept='Marketing'

	 SELECT ename, dept, salary FROM Department
	where ename='Will' and  salary=6500

	SELECT ename, dept, salary FROM Department
	where  dept='Marketing' and salary=6500


sp_help Department








































































































































































































































































































































































