
--Primary key , FOreign key, Joins

--#######################################

Create database DEMO

use DEMO

--Primary key  (unique + not null)
--1 primary key in 1 table 
--clustered index will created(sort and store in asc , search faster)
--************************************
 --unique (unique values)
 --non clustered index will be created(search faster)

CREATE TABLE Department
  (
      did INT primary key ,
      ename VARCHAR(50) ,
      gender VARCHAR(50) ,
      phnum INT unique ,
      dept VARCHAR(50) 
   )

INSERT INTO Department  VALUES
  (1, 'David', 'Male', 5001, 'Sales'),
  (5, 'Shane', 'Female', 5502, 'Finance'),
  (6, 'Shed', 'Male', 8000, 'Sales'),
  (7, 'Vik', 'Male', 7200, 'HR'),
  (2, 'Jim', 'Female', 6000, 'HR'),
  (13, 'Julie', 'Female', 7100, 'IT'),
  (14, 'Elice', 'Female', 6801,'Marketing'),
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
  (1, 'David', 'Male', 5001, 'Sales')

  SELECT * FROM Department

--#######################################################
--Foreign key 


Create database School 

use School

CREATE TABLE Students (
    StudentID INT primary key ,
    eName VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    DateOfBirth DATE
)
CREATE TABLE Teachers (
    TeacherID INT primary key ,
    Name VARCHAR(255),
    Email VARCHAR(255) ,
    HireDate DATE
)

CREATE TABLE Courses (
    CourseID INT,
    Title VARCHAR(255),
    AssignedTeacherID INT,
	 foreign key (AssignedTeacherID) references Teachers(TeacherID)
  )

  Alter table Courses
   add constraint uk_did unique(courseid)

  CREATE TABLE Enrollments (
    EnrollmentID INT,
    StuID INT,
    CouID INT,
    EnrollmentDate DATE,
	 foreign key (StuID) references  Students (StudentID),
	 foreign key (couid) references Courses (CourseID) 
)


--#################################################################
Select * from Students
Select * from Teachers
Select * from Courses
Select * from Enrollments
--Insert happen in which table (primary table  or unique table)
	INSERT INTO Teachers VALUES
	(1,'John Doe', 'john.doe@email.com', '2021-01-10'),
	(2,'Jane Smith', 'jane.smith@email.com', '2022-02-15'),
	(3,'Jim Beam', 'jim.beam@email.com', '2020-03-20')

	INSERT INTO Students  VALUES
	(101,'Alice Johnson', 'alice.johnson@email.com', '2005-04-15'),
	(102,'Bob Marley', 'bob.marley@email.com', '2004-07-20'),
	(103,'Charlie Brown', 'charlie.brown@email.com', '2006-08-30')

INSERT INTO Courses VALUES
(1,'Mathematics 101', 1),
(2,'History 101', 2),
(3,'Science 101', 3)

INSERT INTO Enrollments  VALUES
(1,101, 1, '2022-09-01'),
(2,102, 2, '2022-09-01'),
(3,103, 3, '2022-09-01')


--Delete happen in which table (foreign table)
Delete from Students
Delete from Teachers
Delete from Courses
Delete from Enrollments
--#################################################################

Create database Joins

Use Joins

-- Create Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50)
);


INSERT INTO Customers (CustomerID, CustomerName)
VALUES
    (1, 'John Smith'),
    (2, 'Jane Doe'),
    (3, 'Alice Johnson'),
    (4, 'Bob Williams'),
    (15, 'Emily Brown'),
    (6, 'Michael Davis'),
    (17, 'Olivia Wilson'),
    (8, 'William Taylor'),
    (19, 'Sophia Martinez'),
    (10, 'Liam Anderson');


-- Create Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE
);


INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES
    (101, 1, '2023-08-01'),
    (102, 2, '2023-08-02'),
    (103, 3, '2023-08-03'),
    (104, 4, '2023-08-04'),
    (115, 5, '2023-08-05'),
    (106, 6, '2023-08-06'),
    (117, 7, '2023-08-07'),
    (108, 8, '2023-08-08'),
    (119, 9, '2023-08-09'),
    (110, 10, '2023-08-10');


-- Create Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10, 2)
);


INSERT INTO Products (ProductID, ProductName, Price)
VALUES
    (501, 'Widget', 10.99),
    (502, 'Gadget', 24.99),
    (503, 'Accessory', 5.99),
    (504, 'Tool', 15.49),
    (515, 'Toy', 7.95),
    (506, 'Device', 49.99),
    (517, 'Appliance', 89.00),
    (508, 'Book', 12.50),
    (519, 'Clothing', 29.95),
    (510, 'Jewelry', 59.00);


-- Create OrderDetails table
CREATE TABLE OrderDetails (
    DetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);

INSERT INTO OrderDetails (DetailID, OrderID, ProductID, Quantity)
VALUES
    (1001, 101, 501, 3),
    (1002, 101, 502, 2),
    (1003, 102, 503, 5),
    (1004, 103, 504, 1),
    (1005, 104, 505, 2),
    (1006, 105, 506, 1),
    (1007, 106, 507, 1),
    (1008, 107, 508, 3),
    (1009, 108, 509, 2),
    (1010, 109, 510, 1);



Select top 1 * from Customers
Select top 1 * from Orders
Select top 1  * from OrderDetails
Select top 1 * from products


--Customers & Orders=CustomerID
--Orders & OrderDetails=OrderID
--OrderDetails & products=ProductID
--Customers & products=CustomerID--OrderID--ProductID

Syntax:
	 SELECT columns,columns....FROM
	table1 (Any) JOIN table2 ON table1.common_column = table2.common_column
	table3 on   table3.common_column = table2.common_column
--inner join 
-- FInd customers who have orders
Select top 1 * from Customers
Select top 1 * from Orders

Select * from Customers as C inner join Orders As o
 on C.CustomerID=o.CustomerID

 Select * from Customers  inner join Orders 
 on Customers.CustomerID=Orders.CustomerID

Select * from 
Customers as C inner join Orders As o on C.CustomerID=o.CustomerID
inner join OrderDetails OD on OD.OrderID= O.orderid


Select * from 
Customers as C inner join Orders As o on C.CustomerID=o.CustomerID
inner join OrderDetails OD on OD.OrderID= O.orderid
inner join Products P on OD.ProductID=P.ProductID


Select C.*, P.* from 
Customers as C inner join Orders As o on C.CustomerID=o.CustomerID
inner join OrderDetails OD on OD.OrderID= O.orderid
inner join Products P on OD.ProductID=P.ProductID


Select CustomerName,OrderDate,p.ProductID,ProductName from 
Customers as C inner join Orders As o on C.CustomerID=o.CustomerID
inner join OrderDetails OD on OD.OrderID= O.orderid
inner join Products P on OD.ProductID=P.ProductID


--##############################
--Alias temporary name 

	--columnname as tempname 
	--columnname  tempname 

	--tablename as tempname 
	--tablename tempname 

--##############################
--left  outer join 
	Select * from Customers as C left  join  Orders As o
	 on C.CustomerID=o.CustomerID

	Select * from Customers as C left  outer join  Orders As o
	 on C.CustomerID=o.CustomerID

	 --task to dispaly the customer  where order is missing 
 
	Select * from Customers as C left  outer join  Orders As o
	 on C.CustomerID=o.CustomerID
	 where o.OrderID is null
--##############################
--Right  outer join 
	Select * from Customers as C Right  join  Orders As o
	 on C.CustomerID=o.CustomerID

	Select * from Customers as C Right  outer join  Orders As o
	 on C.CustomerID=o.CustomerID

--task to dispaly the  order  where customer info is missing 
 
	Select * from Customers as C Right  outer join  Orders As o
	 on C.CustomerID=o.CustomerID
	 where C.CustomerID is null



Select * from 
Customers as C Right join Orders As o on C.CustomerID=o.CustomerID
Right join OrderDetails OD on OD.OrderID= O.orderid
Right join Products P on OD.ProductID=P.ProductID


--##############################
--Full  outer join 
	Select * from Customers as C Full  join  Orders As o
	 on C.CustomerID=o.CustomerID

	Select * from Customers as C Full  outer join  Orders As o
	 on C.CustomerID=o.CustomerID

--task to dispaly the  order  where customer info is missing 
 ---task to dispaly the customer  where order is missing 
 
	Select * from Customers as C Full  outer join  Orders As o
	 on C.CustomerID=o.CustomerID
	 where C.CustomerID is null or  o.CustomerID is null


--Natural join 

	Select * from Customers as C   join  Orders As o
	 on C.CustomerID=o.CustomerID

--###############################################################################



















































































































































































































































































































































































































