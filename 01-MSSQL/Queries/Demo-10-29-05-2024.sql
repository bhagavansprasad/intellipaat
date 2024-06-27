--Group By rollup , cubes, pivot , unpivot , coalesce, 
-- FUnction string 

--#########################################
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


  SELECT * FROM Department

  --Group by 

  
  SELECT gender  FROM Department
  group by gender  

  
  SELECT dept FROM Department
  group by dept




create table test (id int , sales varchar(10))

insert into test values 
(1,'shoes'),
(2,NULL),
(NULL,'Keyboard'),
(NULL,Null)


select * from test


--Coalesce(columnname ,'')
	select coalesce(id,9999) as newids,
	coalesce(sales,'Undefined') as newsales from test







select id, id from test

  SELECT gender  FROM Department
  group by gender  

  



  SELECT gender, COUNT(*) as valuess  FROM Department
  group by gender  

  


    SELECT dept, SUM (salary) as SubTotal FROM Department group by dept

    SELECT SUM (salary) as GrandTotal FROM Department

--group by using rollup ( Subtotal&  grandtotal)
    SELECT Coalesce(dept, 'All Dept') as Dept
	, SUM (salary) as Total 
	FROM Department group by rollup(dept)


	SELECT  Dept, gender,
	 SUM (salary) as Total 
	FROM Department group by rollup(dept,gender)

	
	SELECT  Coalesce(dept, 'All Dept') as Dept,
	Coalesce(gender, 'All Dept') as Gender,
	 SUM (salary) as Total 
	FROM Department group by rollup(dept,gender)

--group by Cube(-- all possible combinations)
	SELECT  Coalesce(dept, 'All Dept') as Dept,
	Coalesce(gender, 'All Gender') as Gender,
	 SUM (salary) as Total 
	FROM Department group by cube(gender, dept)


CREATE TABLE SalesData (
    Year INT,
    City VARCHAR(50),
    SalesAmount DECIMAL(10, 2)
);

INSERT INTO SalesData (Year, City, SalesAmount)
VALUES
(2020, 'New York', 15000.00),
(2020, 'Los Angeles', 20000.00),
(2020, 'Chicago', 18000.00),
(2021, 'New York', 16000.00),
(2021, 'Los Angeles', 21000.00),
(2021, 'Chicago', 19000.00),
(2022, 'New York', 17000.00),
(2022, 'Los Angeles', 22000.00),
(2022, 'Chicago', 20000.00),
(2022, 'Boston', 18000.00);



select Year, City, SUM(SalesAmount) from SalesData
group by  rollup(Year, City )
 having Year =2022

select Year, City 
, SUM(SalesAmount) from SalesData
where city='Boston'
group by  cube(Year, City )

--############################################
--PIVOT AND UNPIVOT
--PIVOT Operator
--This operator is used to rotate table-valued expressions.
--It was first introduced in SQL Server 2005 version. 
--It converts data from rows to columns. 
--It splits the unique values from one column into many columns and 
--then aggregates the remaining column values required in the final result.

--Syntax 
	--SELECT <non-pivoted column>, <list of pivoted column>    
	--FROM  (<SELECT query  to produces the data>)  AS <alias name>    
	--PIVOT ( <aggregation function>(<column name that will aggregated>)    
	--FOR  [<column name that  will become column headers>]    
	--    IN ( [list of  pivoted columns]) ) AS <alias name  for  PIVOT table>    
	--<ORDER BY clause> 
	

	CREATE TABLE pivot_demo    
(    
   Region varchar(45),    
   Year int,    
   Sales int    
) 

INSERT INTO pivot_demo  VALUES 
('North', 2010, 72500),  
('South', 2010, 60500),  
('South', 2010, 52000),  
('North', 2011, 45000),  
('South', 2011, 82500),    
('North', 2011, 35600),  
('South', 2012, 32500),   
('North', 2012, 20500)  

select * from pivot_demo

select * from pivot_demo

select Year,North,South from pivot_demo as T1
 pivot
 (Sum(Sales) for Region in(North,South)) as T2


 Select Region,[2010],[2011],[2012]  from pivot_demo as T1
 pivot
 (COunt(Sales) for Year in ([2010],[2011],[2012] )) as T2



 select * from SalesData


 
 select City ,Coalesce([2020], 0) as [2020],
 Coalesce([2021], 0) as [2021],[2022] from SalesData as temptable
 pivot
 (Sum(SalesAmount) for Year in ([2020],[2021],[2022] )) as datatable



 

CREATE TABLE Data (
    Product VARCHAR(50),
    Month VARCHAR(50),
    SalesAmount DECIMAL(10, 2)
);


INSERT INTO Data (Product, Month, SalesAmount)
VALUES
    ('ProductA', null, 1000.00),
    ('ProductA', 'February', 1500.00),
    ('ProductB', 'January', 800.00),
    ('ProductB', 'February', 1200.00),
    ('ProductA', 'march', 1000.00),
    ('ProductA', 'march', 1500.00),
    ('ProductB', 'april', 800.00),
    ('ProductB', 'april', 1200.00);


	INSERT INTO Data (Product, Month, SalesAmount)
VALUES
    ('ProductA', 'OCt', 1000.00),
    ('ProductA', 'SEP', 1500.00),
    ('ProductB', 'NOV', 800.00),
    ('ProductB', 'DEc', 1200.00)

select * from data

select Product,January,February,march,april  from data as t1
pivot 
(Sum(SalesAmount)  for Month in (January,February,march,april )) as t2

---##############################################
Declare @columns nvarchar(max), @sql nvarchar(max)

select @columns=coalesce(@columns+',','')+Quotename(Month) 
from(select distinct MONTH from Data) as Months 

set @sql='
			select Product,'+@columns +' from data as t1
			pivot 
			(Sum(SalesAmount)  for Month in ('+@columns+' )) as t2'
exec sp_executesql @sql
---##############################################

declare @name varchar(100),@name1 varchar(100)
set @name =' alpha '
set @name1='beta'

 select @name+','+@name1

Declare @columns nvarchar(max), @sql nvarchar(max)

select @columns=coalesce(@columns+',','')+Quotename(Month) 
from(select distinct MONTH from Data) as Months 


---####################################################
--Create table based on the select stamenet
 
 select City ,Coalesce([2020], 0) as [2020],
 Coalesce([2021], 0) as [2021],[2022] 
 into PIVOT_SalesData
 from SalesData as temptable
 pivot
 (Sum(SalesAmount) for Year in ([2020],[2021],[2022] )) as datatable
 

 select * from PIVOT_SalesData

--Append data into existing table how to do that 
insert into PIVOT_SalesData

 select City ,Coalesce([2020], 0) as [2020],
 Coalesce([2021], 0) as [2021],[2022] 
from SalesData as temptable
 pivot
 (Sum(SalesAmount) for Year in ([2020],[2021],[2022] )) as datatable

 select * from SalesData



 ---#############################################################
 --Aggreagte Function

 --String Function 
 '12345678@#$%^&*(SDFGHJKL'

 Use AdventureWorks2022

 --len(expression/ columnname)
 select LEN(' 123 abc $%^')

 select BusinessEntityID, FirstName, LastName FRom Person.Person
  
  select LastName, LEN (lastname) as Length  FRom Person.Person
--TRIM(expression/ columnname)
-- remove the lead and trial spaces 
 select len('     al pha     ')
select len(trim('     al pha     '))

--Left & right
--extract the character from the left / right side 
  select firstname
  , LEFT(firstname,2)
  FRom Person.Person
   
   select firstname
  , right(firstname,2)
  FRom Person.Person

--Upper and lower
  select 
  upper(firstname)as n1
  , lower(firstname)as n2
   into testname
  FRom Person.Person

--Concat
select firstname, MiddleName, lastname,
CONCAT(firstname, MiddleName, lastname) as Fullname1 ,
CONCAT(firstname,';', MiddleName,';', lastname) as Fullname2 
  FRom Person.Person

--concat_ws
select firstname, MiddleName, lastname,
CONCAT_ws(';',firstname, MiddleName,lastname) as Fullname
  FRom Person.Person

  select firstname, MiddleName, lastname,
CONCAT_ws(';',firstname, MiddleName,lastname) as Fullname
  FRom Person.Person

  SELECT n1 FROM testname

  SYED 
  Syed

  SELECT n1,
  concat(Upper(LEFT(n1,1)), lower(RIGHT(n1,len(n1)-1))) as newnames
  , Upper(LEFT(n1,1))+lower(RIGHT(n1,len(n1)-1))
  FROM testname

--########################################################

select 1+1

select 'a'+'a'


select concat(1,'a')








































































































































































































































































































