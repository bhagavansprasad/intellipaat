--Windows function , cte, userdefined functions



--###########################################################

Primary key(Unique + not null)



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


  SELECT * FROM Department

  
  alter table department 
  alter column did int not null

  alter table department 
  add constraint PK_DID primary key(did)
--Ranking function 

--Ranking _function()  OVER (PARTITION BY column_name ORDER BY column_name asc/desc)
--=PARTITION BY=group by

  SELECT did,ename,gender,dept,salary, 
  RANK() over(order by salary desc) as Ranks, 
  Dense_RANK() over(order by salary desc) as DenseRanks, 
  Row_NUmber() over(order by salary desc) as RowNum
  FROM Department




    SELECT gender,dept,salary,
	NTILE(3) over(order by dept asc) Tile
  FROM Department


 SELECT gender,dept,salary,
	NTILE(20) over(order by dept desc) Tile
  FROM Department
   where dept like '%fin%'
   

     SELECT did,ename,gender,dept,salary, 
   Row_NUmber() over(order by salary desc) as RowNum
  FROM Department
   where Row_NUmber() over(order by salary desc) =2


--CTE (Common table expression)
--temporary result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE

	WITH CTE_Name 
	AS
	(
		-- CTE query definition goes here
		SELECT column1, column2, ...
		FROM table_name
		WHERE condition
	)
	-- Statement using the CTE
	SELECT * FROM CTE_Name








with testdata
as
(
	
     SELECT did as EMPID,salary as PHNUM
  FROM Department
)

select * from testdata where EMPID =1



--Write a cte to display the high sal 
  with highsal
  as
  (SELECT did,ename,gender,dept,salary, 
   Row_NUmber() over(order by salary desc) as RowNum
  FROM Department)
  select * from highsal where RowNum=1
 --#########################################  
	with highsal
	as
	(SELECT did,ename,gender,dept,salary, 
	 Row_NUmber() over(order by salary desc) as RowNum
	FROM Department
	)
  select * from highsal where RowNum=4


  declare @name varchar(20)
  set @Name ='alpha'
  --#############################
  --Partition by 
	SELECT did,ename,gender,dept,salary, 
	 Row_NUmber() over(partition by dept order by salary desc) as RowNum
	FROM Department

--write a cte to display high sal from each dept 
with maxval
as 
(
	SELECT did,ename,gender,dept,salary, 
	 Row_NUmber() over(partition by dept order by salary desc) as RowNum
	FROM Department
)
select * from maxval where rownum =1

with maxval
as 
(
	SELECT did,ename,gender,dept,salary, 
	 Row_NUmber() over(partition by dept order by salary desc) as RowNum
	FROM Department
)
select * from maxval where rownum =2




Select * from Department 
order by did asc

	SELECT did,ename,gender,dept,salary, 
	 Row_NUmber() over(partition by did, ename order by did asc) as RowNum
	FROM Department

with duprec
as
(	SELECT did,ename,gender,dept,salary, 
	 Row_NUmber() over(partition by did, ename order by did asc) as RowNum
	FROM Department
)
select * from duprec where rownum>1


--remove duplicate

	with duprec
	as
	(	SELECT did,ename,gender,dept,salary, 
		 Row_NUmber() over(partition by did, ename order by did asc) as RowNum
		FROM Department
	)
	delete from duprec where rownum>1

--lag & lead 

--lag() access data from a previous row 
--lead()  access data from a subsequent row 
		SELECT did,ename,gender,dept,salary,LAG(salary)  over(order by did asc) as Lags,
		salary-LAG(salary)  over(order by did asc) as Sub_Lags,lead(salary)  over(order by did asc) as leads,
		salary-lead(salary)  over(order by did asc) as Sub_leads
		
		FROM Department

--##########################################################################
--User defined function 
	--Scalar-Valued Functions

	--Table-Valued Functions



select MAX(salary ) from Department

--square of a number 

	 number = number * number 
	 2= 2*2*2
	 
declare @num float 
set @num =2 
set @num =@num*@num*@num  
print @num

	CREATE FUNCTION function_name (@parameter1 datatype , @parameter2 datatype,...)
	RETURNS return_datatype
	AS
	BEGIN
		-- Function logic here
		DECLARE @result_variable return_datatype;
		SET @result_variable = -- Your calculation or logic here

		RETURN @result_variable;
	END;

--Create Function 
	Create Function squares()
	 returns float
	as 
	begin 
		declare @num float 
		set @num =2 
		return  @num*@num*@num 

	end 

--call function 
	select dbo.squares()

--Alter Function 
	Alter Function squares( @num float )
	returns float
	as 
	begin 
		return  @num*@num*@num 
	end 

--call function 
	select dbo.squares(4.1)

--#################################################################
 
CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Description NVARCHAR(255),
    Price DECIMAL(10, 2)
);


INSERT INTO Product(ProductID, ProductName, Description, Price) VALUES
(1, 'Laptop', 'High-performance laptop', 1200.00),
(2, 'Smartphone', 'Latest model smartphone', 700.00),
(3, 'Keyboard', 'Mechanical keyboard', 150.00),
(4, 'Mouse', 'Wireless mouse', 40.00),
(5, 'Monitor', '27-inch 4K monitor', 330.00),
(6, 'Tablet', '8-inch tablet with Wi-Fi', 200.00),
(7, 'Charger', 'Fast charging adapter', 20.00),
(8, 'Headphones', 'Noise-cancelling headphones', 150.00),
(9, 'Webcam', '1080p HD webcam', 90.00),
(10, 'Desk Lamp', 'LED desk lamp', 45.00);


select * from product


price =100
discount =10%

discounted price =90

--Discount price =price -(price * Discount/100)
select  100-(100*10/100)

select * from product

Create function discount1 (@Price float, @dis float)
returns float 
as 
begin 
	return @price -(@price*@dis/100)

end 



select *,
dbo.discount(Price, 10) as Discounted_Price
from product


Create emi calculator 
create  calculator











select MAX(10)

select MAX(salary) from Department 


select dbo.discount(10, 20)

select *,dbo.discount(Price, 10) as Discounted_Price
from product





--#################################################################
--Table-Valued Functions(work with select)
		CREATE FUNCTION function_name (@parameter1 datatype [, @parameter2 datatype, ...])
		RETURNS TABLE
		AS
		RETURN (
			-- A single SELECT statement
			SELECT column1, column2, ...
			FROM tables   WHERE conditions
		);
--create function 
		Create function readdata()
		returns table 
		as

		return(select * from Department) 

--call function 
		select * from readdata()

---Create function which will tell me highest slary 
Create function highsal(@num int)
		returns table 
		as
		return(
					with highsal
					as
						(SELECT did,ename,gender,dept,salary, 
						 Row_NUmber() over(order by salary desc) as RowNum
						FROM Department
						)
					select * from highsal where RowNum=@num
				)
--call a function 
	select * from highsal(2)



--#####################################################

create function diffdb()
returns table
as
return
(
	Select PP.BusinessEntityID as Empid,FirstName,LastName
	,NationalIDNumber,JobTitle,BirthDate,Gender,HireDate,LoginID
	 from 

	AdventureWorks2022.Person.Person PP inner join 
	AdventureWorks2022.HumanResources.Employee HE
	on PP.BusinessEntityID=HE.BusinessEntityID
 )


 --call function 
 select * from diffdb()  order by Empid desc




 --select * from databasename. schemaname.tablename 

































































































































































































































































































































