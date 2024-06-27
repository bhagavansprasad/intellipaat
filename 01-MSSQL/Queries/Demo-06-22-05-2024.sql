--Aggregate function  , group by using having, order by ASC desc, top 
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
  (NULL, null, null, null,null)
  
INSERT INTO Department  VALUES
  (16, NUll, NUll, 5000, NUll)
  SELECT * FROM Department

 --Aggregate function in SQL server
	
  SELECT * FROM Department

--Count(*) / Count(column Name)

--COUNT(*) it will include the Null
  SELECT COUNT(*) as Count_Rec FROM Department	
--Count(column Name) it will not include the Null values
    SELECT COUNT(did) as Count_Rec FROM Department	
	
    SELECT COUNT(ename) as Count_Rec FROM Department where gender='male'	

	  SELECT * FROM Department

--MAX() it will not include the Null values
	SELECT MAX(did) as HighVal FROM Department
	
	SELECT MAX(salary) as HighVal FROM Department	
	
    SELECT MAX(ename) as HighVal FROM Department 

--Min() it will not include the Null values
	SELECT Min(did) as LowVal FROM Department
	
	SELECT Min(salary) as LowVal FROM Department	
	
    SELECT Min(ename) as LowVal FROM Department 
--These function will work on the Numeric data
--AVG() it will not include the Null values

	SELECT AVG(did) as AVGVal FROM Department
	
	SELECT AVG(salary) as AVGVal FROM Department	
	

--Sum() it will not include the Null values


	SELECT Sum(did) as SumVal FROM Department
	
	SELECT Sum(salary) as SumVal FROM Department	

--##########################################################
	SELECT 
	Sum(salary)+100000 as SumVal
	,AVG(did)/4 as AVGVal
	,Min(salary)*2 as LowVal
	,Max(salary)-50000 as HighVal
	,COUNT(did) as Count_Rec 
	FROM Department	
--Group by 

select 1+2, 3*4, 5-3, 6/2


	  SELECT * FROM Department where salary =(select min(salary) from Department)
select 1+1

select 'A'+'b'

--Group BY (break our resultset into subset)
Syntax:
	--SELECT column1, aggregate_function(column2)
	--FROM table_name
	--WHERE condition
	--GROUP BY column1, column2, ...;

	  SELECT did,ename,gender,salary,dept FROM Department
	

	SELECT did FROM Department
	group by did 

	SELECT gender FROM Department
	group by gender 

	
	SELECT gender, COUNT(*) As counts FROM Department
	group by gender 

		
	SELECT gender, COUNT(*) As counts,
	sum(salary)  as total FROM Department
	group by gender 
	
	SELECT gender, COUNT( did) As counts,
	sum(salary)  as total FROM Department
	group by gender 



	
	SELECT * FROM Department








	SELECT
	COUNT( did) As counts -- will not include null values 
	,COUNT( *) As counts1 -- will include null values 
	FROM Department




	select dept,gender,
	SUM(salary) as Total 
	from Department 
	group by  gender,dept
	   	  
		select AVG(Salary) 	from Department 


--aggregated resultset 
	select dept,gender,
	SUM(salary) as Total 
	from Department 
	group by  gender,dept
	   	  
--- filtering using the having 
	select dept,gender,
	SUM(salary) as Total 
	from Department 
	 --where gender ='male'
	group by  gender,dept
	having sum(salary) >15000

	

--select 
-- COLUMNnames 
-- from tablename 
--  where column=values 
--   GROUP by columnnames
--   having  column=values 
--  order by columnnames asc


 --LOGICAL PROCESSING ORDER OF THE SELECT  STATTEMENT 
  --Sequence to execute in sql server 
  --FROM
  --ON   --JOIN
  --WHERE
  --GROUP BY 
  --WITH (CUBE/ ROLLUP)
  --HAVING 
  --SELECT 
  --DISTINCT
  --ORDER BY 
  --TOP 

--Order by asc/desc
use AdventureWorks2022

select BusinessEntityID, FirstName , LastName from  Person.Person

	select* from Department 
	order by did asc

	select* from Department 
	order by did desc

select BusinessEntityID, FirstName , LastName from  Person.Person
order by BusinessEntityID asc, FirstName asc

select FirstName , LastName from  Person.Person
order by  FirstName asc, LastName desc

select FirstName , LastName from  Person.Person
order by  FirstName desc, LastName asc


Create table test (enames nvarchar(100))

insert into test values 
(N'Яблоко'),
(N'りんご'),
(N'hello')


select * from test
 order by enames asc

 select * from Person.Person

 --Top n


  select top 1 * from Person.Person


  
  select top 10 * from Person.Person


  -- Find me the high records  rec from table 
  
  select MAX(BusinessEntityID) as maxid from Person.Person
    
  select* from Person.Person 
  where BusinessEntityID=  ( select MAX(BusinessEntityID)from Person.Person)
	
	select top 1 * from Person.Person 
	order by  BusinessEntityID desc

--################################################################




















































































































































































































































































































