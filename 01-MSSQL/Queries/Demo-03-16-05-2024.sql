--datatype(string, datetime), ddl dml, system database 

--###############################################################################
--Approximate number 
 float  , 15 precision , 8 byte
	


	Precision = all the values towards the left and right of my decical point=12342341355.6324234756
	sclae= values towards the right of my decical point=6324234756
	12342341355.6324
	12345678901 2345


	declare @value  float
	SET @value= 123456789123456
	select @value as Number ,datalength(@value) Byte 

	
	declare @value  float
	SET @value= 1234567891234567
	select @value as Number ,datalength(@value) Byte 


	1.23456789123457E+15
	 
	 1.23456789123457 * 10 riased power 15

	 declare @value  float
	SET @value= 123456789.1234567 
	select @value as Number ,datalength(@value) Byte 
	
	 declare @value  float
	SET @value= 1234567898.1234567 
	select @value as Number ,datalength(@value) Byte 
	
	 declare @value  float
	SET @value= 123456789876543.1234567 
	select @value as Number ,datalength(@value) Byte 

--###############################################################################
--decimal(precision, scale)
--Precision		Storage bytes
--1 - 9				5
--10-19				9
--20-28				13
--29-38				17

	 declare @value  decimal(38,0)
	SET @value= 12345678998765432101234567899876543210
	select @value as Number ,datalength(@value) Byte 

	
	 declare @value  decimal(30,0)
	SET @value= 12345678998765432101234567899876543210
	select @value as Number ,datalength(@value) Byte 

	
	 declare @value  decimal(30,2)
	SET @value= 12345.678
	select @value as Number ,datalength(@value) Byte 
	 
	 
	 declare @value  decimal(30,2)
	SET @value= 123459876.678
	select @value as Number ,datalength(@value) Byte 
 
	 declare @value  decimal(38,5)
	SET @value= -9222348765123459344876.678
	select @value as Number ,datalength(@value) Byte 

--###############################################################################
--String 
'123 45asdcfgh @c#$% ^& '
-- Char() , 1 to 8000, 1 byte
-- static memeory allocation 
--It is a fixed length data type

Declare @test char(1)
set @test='alph'
 print @test

 
	declare @value char(10)
	SET @value= 'alpha'
	select @value as Number ,datalength(@value) Byte 

--###############################################################################

-- VarChar() , 1 to 8000, 1 byte
-- Dynamic memory allocation 
--It is a variable length data type

	declare @value char(10)
	SET @value= 'alpha'
	select @value as Number ,datalength(@value) Byte 
	
	declare @value varchar(10)
	SET @value= '!@#$%^&*()'
	select @value as Number ,datalength(@value) Byte 


--###############################################################################
Unicode 

-- nChar() , 1 to 4000, 2 byte
-- static memeory allocation 
--It is a fixed length data type


	declare @value nchar(10)  --=10 * 2
	SET @value= 'alpha'
	select @value as Number ,datalength(@value) Byte 
	
	declare @value nchar(20)  --=20 * 2
	SET @value= N'नमस्ते दुनिया'
	select @value as Number ,datalength(@value) Byte 
	
	declare @value nchar(4000)  --=20 * 2
	SET @value= N'你好，世界'
	select @value as Number ,datalength(@value) Byte 


-- nVarChar() , 1 to 4000, 1 byte
-- Dynamic memory allocation 
--It is a variable length data type


	declare @value nVarChar(10)  --=5 * 2
	SET @value= 'alpha'
	select @value as Number ,datalength(@value) Byte 
	
	declare @value nVarChar(20)  --=13 * 2
	SET @value= N'नमस्ते दुनिया'
	select @value as Number ,datalength(@value) Byte 
	
	declare @value nVarChar(8000)  --=5 * 2
	SET @value= N'你好，世界'
	select @value as Number ,datalength(@value) Byte 

		
	declare @value nVarChar(max)  --=5 * 2
	SET @value= N'你好，世界'
	select @value as Number ,datalength(@value) Byte 




--###############################################################################
--Date and time 
--date , 3 byte 
	--input='YYYY-MM-DD' or 'MM-DD-YYYY'
	--output='YYYY-MM-DD'
	declare @value date
	SET @value= '2024-05-16'
	select @value as Number ,datalength(@value) Byte 

	declare @value date
	SET @value= '05-16-2024'
	select @value as Number ,datalength(@value) Byte 

	
	declare @value date
	SET @value= '12-05-2024'
	select @value as Number ,datalength(@value) Byte
--time , 5 byte 
	--input='HH:MM:SS'
	--output 'HH:MM:SS:MMMMMMM'
	declare @value time
	SET @value= '22:10:00:123'
	select @value as Number ,datalength(@value) Byte 

--Timestamp 'YYYY-MM-DD HH:MM:SS'
	declare @value3 smalldatetime
	SET @value3= '2024-05-16 22:10:00'
	select @value3 as Number ,datalength(@value3) Byte 
		
	declare @value1 datetime
	SET @value1= '2024-05-16 22:10:00'
	select @value1 as Number ,datalength(@value1) Byte 
	
	declare @value datetime2
	SET @value= '2024-05-16 22:10:00'
	select @value as Number ,datalength(@value) Byte 
--practice
--XML datatype in sql server 
--json datatype in sql server 

--###############################################################################

--System Databases
--https://learn.microsoft.com/en-us/sql/relational-databases/databases/system-databases?view=sql-server-ver16

--master Database	
	--Records all the system-level information for an instance of SQL Server.

--model Database	
	--Is used as the template for all databases created on the instance of SQL Server.

--msdb Database	
	--Is used by SQL Server Agent for scheduling alerts and jobs.

--tempdb Database	
	--Is a workspace for holding temporary objects or intermediate result sets.

--Resource Database	
	--Is a read-only database that contains system objects that are included with SQL Server. 
	https://learn.microsoft.com/en-us/sql/relational-databases/databases/resource-database?view=sql-server-ver16
	--Installation drive>:\Program Files\Microsoft SQL Server\MSSQL<version>.<instance_name>\MSSQL\data\ 
		--Installation drive>:\Program Files\Microsoft SQL Server\MSSQL<version>.<instance_name>\MSSQL\Binn\ 
	--Name  =  mssqlsystemresource
--###############################################################################

--Create database 
	syntax: create database DatabaseName

create database HELLOWORLD

create database [SQL DEMO]

create database DEMO



--###############################################################################
--use 
--Current database name = master 

--create employee table on database= demo (ename, age , gender , id , salary)
	--create table tablename
	--( ColumnName datatype ,
	--ColumnName datatype ,ColumnName datatype ,
	--ColumnName datatype ,.....................)
use DEMO 
 create table employee
 (id int,ename varchar(20), age int , gender char(10), salary decimal(10,2))


 --create dep table on database= sql demo (ename, age , gender , id , salary)

 use [SQL DEMO]
  create table dep
 (id int,ename varchar(20), age int , gender char(10), salary decimal(10,2))


 --add email varchar(100) ln dep 
 --syntax:
	--		 Alter table Tablename 
	--		 add colummn datatype
 --Alter table to add a column
	alter table dep 
	add email varchar(100)

	alter table dep 
	add phnum bigint

 --Alter table to drop a column
  --syntax:
		-- Alter table Tablename 
		--drop colummn Columnname

	Alter table dep 
	drop column age

	
	Alter table dep 
	drop column salary
	
	Alter table dep 
	drop column id
 --Alter table to change datatype of  a column
  --syntax:
		-- Alter table Tablename 
		--Alter colummn Columnnamedatatype
	Alter table dep 
	Alter column id varchar(12)

	Alter table dep 
	Alter column phnum varchar(12)
--###############################################################################
--DROP 

--Drop table tablename 

use [SQL DEMO]
Drop table  dep


--drop database databasename
 use master
drop database  [SQL DEMO]

 use master
drop database  [DEMO]


 use master
drop database  HELLOWORLD


--###############################################################################

--QUESTION TO PRACTICE 

Create database school 

use school

create table Teachers (TeacherID int, Name varchar(20), Age int , Class varchar(20))

--1. Teachers Table:
	--Columns: TeacherID int, Name varchar(20), Age int , Class varchar(20)
	
--2. Students Table:
	--Columns: StudentID, FirstName, LastName, Age, Class, TeacherID
	
--3. Courses Table:
	--Columns: CourseID, CourseName, Department, TeacherID
	
--4. Departments Table:
	--Columns: DepartmentID, DepartmentName
	
--5. Enrollments Table:
	--Columns: EnrollmentID, StudentID, CourseID, EnrollmentDate
	
--6. Teachers_Departments Table:
	--Columns: TeacherDepartmentID, TeacherID, DepartmentID
	
----****************************************************************************************************************************************

 Create database hospital
 Use hospital

create table Doctors ( DoctorID int , FirstName varchar(20), LastName varchar(20), Specialization  varchar(20), Age int)
-- 1. Doctors Table:
   -- Columns: DoctorID, FirstName, LastName, Specialization, Age
  
-- 2. Patients Table:
   -- Columns: PatientID, FirstName, LastName, Age, AdmissionDate, DischargeDate, DoctorID
   
-- 3. Departments Table:
   -- Columns: DepartmentID, DepartmentName, HeadDoctorID
   
-- 4. Nurses Table:
   -- Columns: NurseID, FirstName, LastName, Age, DepartmentID
   
-- 5. Medications Table:
   -- Columns: MedicationID, MedicationName, Dosage
   
-- 6. Prescriptions Table:
   -- Columns: PrescriptionID, PatientID, DoctorID, MedicationID, PrescribedDate, DosageInstructions
   








--###############################################################################












--###############################################################################










--###############################################################################












--###############################################################################










--###############################################################################








































































































































































































































































































































































































































































































































