--SQl server views, Stored procedures, if , if else
--###########################################################

Create database Demo

use demo

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


  SELECT did,salary, CONCAT(did,salary), cast(did as bigint )+  cast(salary as bigint )  FROM Department

--SQl server views 
virtual table 
  

    SELECT did,ename,dept FROM Department
--syntax:
--		Create view viewname 
--		as 
--		select statement

--Create view 

	Create view vw_read
	as
    SELECT did,ename,dept FROM Department

--call view 
	select * from vw_read 


--Change on table 
	delete from department 
	select * from department

--call view 
	select * from vw_read 


--Change on view 
	delete from vw_read 
	select * from vw_read

	INSERT INTO vw_read  VALUES
  (1, 'David',  'Sales'),
  (5, 'Shane',  'Finance'),
  (6, 'Shed',  'Sales')


--Drop the table department 

drop table Department 

--call view 
	select * from vw_read 
--Could not use view or function 'vw_read' because of binding errors.

--why we use view / function 

Create view VW_userinfo
as
	Select PP.BusinessEntityID as Empid,FirstName,LastName
	,NationalIDNumber,JobTitle,BirthDate,Gender,HireDate,LoginID
	from AdventureWorks2022.Person.Person PP inner join 
	AdventureWorks2022.HumanResources.Employee HE
	on PP.BusinessEntityID=HE.BusinessEntityID

select * from VW_userinfo


Create view  VW_addinfo
as
	Select BusinessEntityID,AddressLine1,City,PostalCode 
	from 
	AdventureWorks2022.Person.Address PA inner join 
	AdventureWorks2022.Person.BusinessEntityAddress PB
	on PA.AddressID=PB.AddressID

select * from VW_userinfo
select * from VW_addinfo

--Cntrl + SHift +Q
Create view VW_allinfo1
as
select * from VW_userinfo inner join  VW_addinfo
 on BusinessEntityID=Empid


 select * from VW_allinfo order by Empid





 --Index view 


CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    SaleDate DATE,
    Amount DECIMAL(10, 2)
);




INSERT INTO Sales (SaleID, SaleDate, Amount) VALUES
(1, '2024-01-01', 100.00),
(2, '2024-01-01', 150.50),
(3, '2024-01-02', 120.00),
(4, '2024-01-02', 80.00),
(5, '2024-01-03', 200.00),
(6, '2024-01-03', 50.00),
(7, '2024-01-04', 75.00),
(8, '2024-01-04', 125.50),
(9, '2024-01-05', 180.00),
(10, '2024-01-05', 90.00),
(11, '2024-01-06', 60.00),
(12, '2024-01-06', 110.00),
(13, '2024-01-07', 100.00),
(14, '2024-01-07', 130.00),
(15, '2024-01-08', 85.00),
(16, '2024-01-08', 145.00),
(17, '2024-01-09', 95.00),
(18, '2024-01-09', 105.00),
(19, '2024-01-10', 250.00),
(20, '2024-01-10', 100.00);


select * from Sales
--count()		--int 
--count_big		--bigint

Create view VW_index with schemabinding
as
select SaleDate, COUNT_BIG(*)  as Count, SUM(isnull(Amount,0))as total 
from dbo.Sales
group by SaleDate

Create unique clustered index vw_salesa on VW_index(saledate)


select * from VW_index where SaleDate='2024-01-03'


select coalesce(Null,0)
select isnull(Null,0)

--###########################################################################
If 1=1
	print 'true'
else 
	print 'false'
	
--Scenario

If 1=10
	print 'true'
else 
	print 'false'


--Scenario
Declare @val int =20
if @val <15
	print 'true'
else 
	print 'false'

--Scenario

If 10=1
	print 'true-1'
else If 1=21
	print 'true-2'
else If 11=1
	print 'true-3'
else If 16=1
	print 'true-4'
else If 1=15
	print 'true-5'
else
	print 'false'
--Scenario
declare @action varchar(20)
set @action ='Update'

If @action='Insert'
	print 'true-Insert'

else If @action='Update'
	print 'true-Update'

else If @action='Delete'
	print 'true-Delete'

else
	print 'invalid action'


	

--###########################################################################
--Stored Procedure
--Syntax:
--	CREATE PROCEDURE procedure_name
--    @parameter1 datatype [= default] [OUTPUT],
--    @parameter2 datatype [= default] [OUTPUT],
--    ...
--	AS
--	BEGIN
--		-- SQL statements here(Insert, sleect , update, delete )
--	END;

--create procedure 

	create procedure sp_read
	as
	select * from department 

--call stored procedure 

	exec sp_read

--Modify stored procedure 


	Alter procedure sp_read @id int 
	as
	select * from department where did =@id


--call stored procedure 

	exec sp_read 1

	exec sp_read @id =13

---Stored procedures  to insert, update and delete the records 

Create table test 
(id int , ename varchar(20), gender varchar(10), sal int )

Create procedure testdata 
@action  varchar(20),@id int , @ename varchar(20) = NUll, @gender varchar(10) = NUll, @sal int  = NUll
as
begin 
	
	If @action='Insert'
		Begin 
			insert into test values (@id, @ename, @gender, @sal)
		end
	else If @action='Update'
		Begin 
			update test 
			set ename =@ename, gender=@gender, sal=@sal
			where id=@id 
		end

	else If @action='Delete'
		Begin 
			delete from test where id=@id
		end

	else
		print 'invalid action'
end 

exec testdata [insert], 101, alpha, male, 20100

exec testdata 'insert', 102, 'beta', 'female', 20100
exec testdata 'insert', @id =103,@ename= 'charle',@gender= 'male',@sal= 20100

select * from test


exec testdata 'update', 103

exec testdata 'update', 102, 'fox', 'male', 9876543

exec testdata 'delete', 103

exec testdata 'delete', 102


exec  'delee', 102


---Call a object 

databasename.SchenmaName,ObjectName 











































































































































































































































































































































































































































































































































































































































































































































































