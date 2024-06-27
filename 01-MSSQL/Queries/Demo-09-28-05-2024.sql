
--Cross join , self join ,merge, set operators
--##########################################################
--Cross join

Create database DEMO

use DEMO


CREATE TABLE Meals(MealName VARCHAR(100))
CREATE TABLE Drinks(DrinkName VARCHAR(100))

INSERT INTO Drinks VALUES('Orange Juice'), ('Tea'), ('Cofee')
INSERT INTO Meals VALUES('Omlet'), ('Fried Egg'), ('Sausage')


Select * from Drinks 
Select * from  Meals


Select * from Drinks cross join  Meals

CREATE TABLE emp (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50)
)

INSERT INTO emp (employee_id, employee_name)
VALUES
    (1, 'John Smith'),
    (2, 'Jane Doe'),
    (3, 'Bob Johnson');



CREATE TABLE dep (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);



INSERT INTO dep (department_id, department_name)
VALUES
    (101, 'HR'),
    (102, 'Engineering'),
    (103, 'Sales');



select * from emp 
select * from dep


select * from emp cross join dep
where  department_id=101

select * from emp cross join Drinks cross join  Meals

---################################################################
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

use AdventureWorks2022

select * from Person.Person pp

select * from HumanResources.Employee he
--Join(Compare)
	select * from Person.Person pp inner join HumanResources.Employee he
	on pp.BusinessEntityID=he.BusinessEntityID

--Equi join (equality=)

	select * from Person.Person pp , HumanResources.Employee he
	where pp.BusinessEntityID=he.BusinessEntityID

--Self join 

CREATE TABLE info (
    EmployeeID int PRIMARY KEY,
    EmployeeName varchar(255),
    ManagerID int
);

INSERT INTO info (EmployeeID, EmployeeName, ManagerID) VALUES
(1, 'Alice Johnson', NULL),
(2, 'Bob Smith', 1),
(3, 'Catherine Brown', 1),
(4, 'Daniel Garcia', 1),
(5, 'Emma Wilson', 1),
(6, 'Franklin Moore', 2),
(7, 'Georgia Taylor', 2),
(8, 'Henry Anderson', 2),
(9, 'Isabel Thomas', 3),
(10, 'Jack Martinez', 3),
(11, 'Kylie Robinson', 3),
(12, 'Liam Clark', 4),
(13, 'Mia Rodriguez', 4),
(14, 'Noah Lewis', 4),
(15, 'Olivia Lee', 5),
(16, 'Parker Walker', 5),
(17, 'Quinn Hall', 5),
(18, 'Ryan Allen', 6),
(19, 'Sophia Young', 6),
(20, 'Tyler Hernandez', 6);

select * from info


--task employee name & manager name 
	select EmployeeID, EmployeeName from info
	select ManagerID, EmployeeName as ManagerName  from info
	select * from info

	select Emp.EmployeeName,MGR.EmployeeName as ManagerName 
	from info as Emp  left join  info Mgr
	on Emp.ManagerID=Mgr.EmployeeID


		select * from info emp







CREATE TABLE Employees (
    EmployeeID int NOT NULL PRIMARY KEY,
    Name varchar(255) NOT NULL,
    DepartmentID int
)

CREATE TABLE Departments (
    DepartmentID int NOT NULL,
    DepartmentName varchar(255) NOT NULL
)


INSERT INTO Employees (EmployeeID, Name, DepartmentID) VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 103),
(4, 'David', 101),
(5, 'Eva', 104);


INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(101, 'Human Resources'),
(102, 'Finance'),
(103, 'IT'),
(104, 'Marketing'),
(101, 'HR')


select * from Employees
select * from Departments


select * from Employees ee inner join Departments dd
on ee.DepartmentID=dd.DepartmentID





--#############################
--Merge Syntax
		MERGE  target_table USING source_table 		ON merge_condition
		WHEN MATCHED THEN
			UPDATE SET column1 = value1, column2 = value2, ...
		WHEN NOT MATCHED BY TARGET THEN
			INSERT (column1, column2, ...) VALUES (value1, value2, ...)
		WHEN NOT MATCHED BY SOURCE THEN
			DELETE;


CREATE TABLE SourceProducts(
    ProductID INT,
    ProductName VARCHAR(50),
    Price	DECIMAL(9,2)
)
GO
    
INSERT INTO SourceProducts(ProductID,ProductName, Price) VALUES(1,'Table',100)
INSERT INTO SourceProducts(ProductID,ProductName, Price) VALUES(2,'Desk',80)
INSERT INTO SourceProducts(ProductID,ProductName, Price) VALUES(3,'Chair',50)
INSERT INTO SourceProducts(ProductID,ProductName, Price) VALUES(4,'Computer',300)
GO
    
CREATE TABLE TargetProducts(
    ProductID INT,
    ProductName VARCHAR(50),
    Price	DECIMAL(9,2)
)
GO
    
INSERT INTO TargetProducts(ProductID,ProductName, Price) VALUES(1,'Tablesss',9)
INSERT INTO TargetProducts(ProductID,ProductName, Price) VALUES(2,'Deskss',8)
INSERT INTO TargetProducts(ProductID,ProductName, Price) VALUES(5,'Bed',50)
INSERT INTO TargetProducts(ProductID,ProductName, Price) VALUES(6,'Cupboard',300)
GO
    
    
SELECT * FROM SourceProducts
SELECT * FROM TargetProducts

--Merge 

merge TargetProducts TP using SourceProducts as SP 
on TP.Productid=sp.productid
--Update 
	when matched then 
		update set 
		TP.ProductName=Sp.ProductName,
		Tp.Price=sp.Price
;

--##################################
merge TargetProducts TP using SourceProducts as SP 
on TP.Productid=sp.productid
--INsert 
	when not matched by target then 
		insert(ProductID,ProductName, Price)
		 values(sp.ProductID,sp.ProductName, sp.Price)
;


--##################################
merge TargetProducts TP using SourceProducts as SP 
on TP.Productid=sp.productid
--Delete 
	when not matched by Source then 
	delete
	;

SELECT * FROM SourceProducts
SELECT * FROM TargetProducts



--##################################
merge TargetProducts TP using SourceProducts as SP 
on TP.Productid=sp.productid
--Update 
	when matched then 
		update set 
		TP.ProductName=Sp.ProductName,
		Tp.Price=sp.Price
--INsert 
	when not matched by target then 
		insert(ProductID,ProductName, Price)
		 values(sp.ProductID,sp.ProductName, sp.Price)

--Delete 
	when not matched by Source then 
	delete
;
--##################################################################
--SQL set operators
Create table employee
( empid int, ename varchar(20), eage int , dob date)


Create table department 
(depid int ,empname varchar(20),salary int ,age int  ,
Company varchar(20) Default 'IBM')

INSERT INTO EMPLOYEE values 
(101,'ALPHA',21,'2010-08-11') ,
(103,'BETA',22,'2009-08-11'),
(102,'CHARLIE',21,'2010-08-11'),
(105,'DELTA',25,'2008-08-11'),
(106,'ECHO',23,'2006-08-11'),
(104,'FOX',21,'2004-08-11'),
(109,'CHARLIE',24,'2010-08-11'),
(107,NULL,25,'2008-08-11')


insert into department values 
(101,'Alpha',6000,21,'Vendor'), 
(102,'fox',7000,21,'Vendor'), 
(105,'Echo',5100,29,'Vendor'),
(103,'beta',5100,29,'Vendor'),
(104,'fox',5100,21,'Vendor'), 
(105,'tim',5100,25,'Vendor')

select * from employee
select * from department

--Union all (Combine + duplicate)
	select 	empid,ename,eage from employee
	 union all
	select depid,empname,age from department order by  empid asc


--Error
	--All queries combined using a UNION, INTERSECT or EXCEPT operator must
	--have an equal number of expressions in their target lists.\


--Union (Combine + Unique)
	select 	empid,ename,eage from employee
	 union
	select depid,empname,age from department order by  empid asc


--Intersect (Common, uniquely)
	select 	empid,ename,eage from employee
	 Intersect
	select depid,empname,age from department order by  empid asc

--Except (Minus)
	select 	empid,ename,eage from employee
	 Except
	select depid,empname,age from department order by  empid asc


	select column1,column2,column3,column4... from t1
	set operators
	select column1,column2,column3,column4... from t2
	set operators
	select column1,column2,column3,column4... from t3
	set operators
	select column1,column2,column3,column4... from t4 order by columnname 

