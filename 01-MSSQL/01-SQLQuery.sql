  CREATE TABLE employee(
    e_id int not null,
    e_name varchar(20),
    e_salary int,
    e_age int,
    e_gender varchar(20),
    e_dept varchar(20),
    primary key(e_id)
  );

  CREATE TABLE department(
    d_id int not null,
    d_name varchar(20),
    d_location varchar(20),
    primary key(d_id)
  );

  INSERT INTO employee VALUES (
    1,'sam', 95000, 45, 'Male', 'Operations' 
  );

  INSERT INTO employee VALUES (
    2,'bob', 80000, 21, 'Male', 'Spport' 
  );

  INSERT INTO employee VALUES (
    3,'Anne', 125000, 25, 'Female', 'Analytics' 
  );

  INSERT INTO employee VALUES (
    4,'BAnne', 12500, 25, 'Female', 'Programming' 
  );

  INSERT INTO employee VALUES (
    5,'Bhagavan', 12456, 28, 'Male', 'Management' 
  );

  INSERT INTO employee VALUES (
    6,'Saketh', 123432, 20, 'Male', 'Student' 
  );

  SELECT * FROM employee;

  SELECT e_id, e_name from employee;
  SELECT e_id, e_name, e_age from employee;

  SELECT DISTINCT  e_gender from employee;
  SELECT e_gender from employee;

  SELECT e_name, e_gender from employee WHERE e_gender='Female';
  SELECT e_name, e_gender from employee WHERE e_gender='male';
  SELECT * from employee WHERE e_age<30 AND e_salary > 90000;
  SELECT * from employee WHERE e_name LIKE 'B%';
  SELECT * from employee WHERE e_age LIKE '_5';
  SELECT * from employee WHERE e_age BETWEEN 25 and 50;

  INSERT INTO department VALUES(1, 'Content', 'New York');
  SELECT * FROM department;
  INSERT INTO department VALUES(2, 'Support', 'Chicago');
  INSERT INTO department VALUES
  (3, 'Analytics', 'New York'),
  (4, 'Sales', 'Boston'), 
  (5, 'Tech', 'Dallas'), 
  (6, 'Finance', 'Chicago');

  SELECT employee.e_name, employee.e_dept, department.d_name, department.d_location
  FROM employee
  INNER JOIN department ON employee.e_dept=department.d_name;

  SELECT employee.e_name, employee.e_dept, department.d_name, department.d_location
  FROM employee
  LEFT JOIN department ON employee.e_dept=department.d_name;
  SELECT * FROM employee;


  UPDATE employee SET e_dept='Support' WHERE e_dept='Spport';

  SELECT employee.e_name, employee.e_dept, department.d_id,  department.d_name
  FROM employee
  RIGHT JOIN department ON employee.e_dept=department.d_name;

  
  SELECT employee.e_name, employee.e_dept, department.d_name, department.d_id
  FROM employee
  FULL JOIN department ON employee.e_dept=department.d_name;

  UPDATE employee SET e_age=e_age+50
  FROM employee
  JOIN department ON employee.e_dept=department.d_name;

  use happy;
  select * INTO employee_s FROM employee;
  SELECT * FROM employee;
  SELECT * FROM employee_s;
  DELETE FROM employee_s WHERE e_id=5;
  DELETE FROM employee_s WHERE e_id=2;

  INSERT INTO employee_s VALUES (
    7,'Vachan', 176543, 30, 'Male', 'Student' 
  );

  INSERT INTO employee_s VALUES (
    8,'Dheer', 143, 22, 'Male', 'Management' 
  );

  MERGE employee_s AS T
  USING employee AS S
	ON T.e_id=S.e_id
  WHEN MATCHED
	then UPDATE SET T.e_salary=S.e_salary, T.e_age=S.e_age
  WHEN NOT MATCHED BY TARGET
    THEN insert (e_id, e_name, e_salary, e_age, e_gender, e_dept)
	values(S.e_id, S.e_name, S.e_salary, S.e_age, S.e_gender, S.e_dept)
  WHEN NOT MATCHED BY SOURCE
    THEN delete;


CREATE TABLE #student(
s_id int,
s_name varchar(20)
);

SELECT * FROM #student;
SELECT * FROM employee;

INSERT INTO #student values(10, 'Bhagavan')
SELECT MIN(e_age) FROM employee;
SELECT MAX(e_age) FROM employee;
SELECT MAX(e_salary) FROM employee;
SELECT COUNT(e_gender) FROM employee;
SELECT COUNT(*) FROM employee WHERE e_gender='Male';
SELECT COUNT(*) FROM employee WHERE e_gender='Female';
SELECT COUNT(e_gender) FROM employee WHERE e_gender='Female';
SELECT SUM(e_age) FROM employee;
SELECT SUM(e_salary) FROM employee;
SELECT AVG(e_age) FROM employee;

select '     bhagavan';
SELECT LTRIM('     bhagavan');
SELECT LTRIM(UPPER('     bhagavan'));
SELECT REVERSE(LTRIM(UPPER('     bhagavan')));
SELECT '     bhagavan';
SELECT SUBSTRING('bhagavan prasad kdp', 3, 5);
SELECT
CASE
	WHEN 10>20 THEN '10 > 20'
	WHEN 10<20 THEN '10 < 20'
	ELSE '10 = 20'
END;


SELECT *, gender=
CASE
	WHEN e_gender='Female' THEN 'f'
	WHEN e_gender='Male' THEN 'm'
	ELSE 'Transgender'
END
FROM employee;
go

SELECT * FROM employee;
SELECT e_id, e_name, e_age, iif(e_age>30, 'old', 'young') as employee_gen FROM employee;

CREATE FUNCTION add_five(@num as int)
RETURNS int
AS
BEGIN
RETURN(@num+5)
END;

SELECT dbo.add_five(100);

CREATE FUNCTION select_gender(@gender as varchar(20))
RETURNS table
AS
RETURN
(
SELECT * FROM employee WHERE e_gender=@gender
)

SELECT * FROM dbo.select_gender('Male');

SELECT TOP 3 * FROM employee ORDER BY e_name DESC;


SELECT * FROM employee;

SELECT AVG(e_salary), e_gender FROM employee GROUP BY e_gender ORDER BY e_gender;
SELECT AVG(e_salary), e_gender FROM employee WHERE e_age > 30 GROUP BY e_gender ORDER BY e_gender;
SELECT AVG(e_salary), e_gender FROM employee WHERE e_age > 30 GROUP BY e_gender ORDER BY AVG(e_age) DESC;

SELECT e_dept, AVG(e_salary) AS avg_salary from employee group by e_dept;
SELECT e_dept, AVG(e_salary) AS avg_salary from employee group by e_dept HAVING avg(e_salary) > 100000;


-- Union & Union All
SELECT * FROM employee 
UNION
SELECT * FROM employee_s

SELECT * FROM employee 
UNION ALL
SELECT * FROM employee_s

-- EXCEPT
SELECT * FROM employee_s
EXCEPT
SELECT * FROM employee 

SELECT * FROM employee 
EXCEPT
SELECT * FROM employee_s

DELETE FROM employee_s WHERE e_name = 'Bhagavan';

-- Intersect
SELECT * FROM employee 
INTERSECT
SELECT * FROM employee_s



-- Stored procedure
CREATE PROCEDURE employee_age
AS
SELECT e_age FROM employee
GO

exec employee_age

CREATE PROCEDURE employee_details
AS
SELECT * FROM employee
GO

exec employee_details


CREATE PROCEDURE employee_details
AS
SELECT * FROM employee
GO

exec employee_details

CREATE PROCEDURE employee_details2
@p1 int, @p2 varchar(20)
AS
SELECT * FROM employee WHERE e_age > p1 AND e_dept = p2
GO

CREATE PROCEDURE employee_details3
@p1 int, @p2 varchar(20)
AS
SELECT * FROM employee WHERE e_age > @p1 AND e_dept = @p2
GO

exec employee_details3 30, 'Support'

-- Views
CREATE VIEW female_emp AS 
select e_id, e_gender FROM employee WHERE e_gender = 'Female';

SELECT * from female_emp;
DROP VIEW female_emp;

SELECT * FROM employee

-- Transaction
BEGIN TRANSACTION
UPDATE employee set e_age=50 WHERE e_dept='Operations'
COMMIT TRANSACTION 
ROLLBACK TRANSACTION 

BEGIN TRY
	BEGIN TRANSACTION
		UPDATE employee set e_age=50 WHERE e_name='Bhagavan'
		UPDATE employee set e_salary=5555 WHERE e_name='Saketh'

		COMMIT TRANSACTION 
		Print 'Transaction is committed'
END TRY
BEGIN CATCH
	ROLLBACK TRANSACTION
	Print 'Transaction is rollback'
END CATCH

-- Exception handlling


-- Task
-- 1 Create a table 'users10k' with schema id int, name varchar(20)
-- 2 Write a procedure which inserts 10K records with id and name
-- 3 Duplicate table into two tables sample10k, sample10k_CI
-- 4 Create Cluster-Index to sample10_CI on column 'name'
-- 5 Select Execution plan for both the tables
-- 6 Run the query 'select * from sample10k WHERE name='7456bhagavan';
-- 7 Run the query 'select * from sample10k_CI WHERE name='7456bhagavan';
-- 8 Observe Query-run-time, CPU-time, Number of records read


CREATE DATABASE sample_data;
USE sample_data;
DROP TABLE users10k;
DROP TABLE sample10k;
DROP TABLE sample10k_CI;

CREATE TABLE users10k(
	id int not null,
	name varchar(20),
    primary key(id)
);

DELETE from users10k WHERE id > 0;
select * from users10k;

DROP PROCEDURE insert_n_users;
CREATE OR ALTER PROCEDURE insert_n_users
@n int, @name varchar(20)
AS
	DECLARE
		@i int = 1,
		@qry varchar(128) = '',
		@uname varchar(40) = ''
	WHILE @i <= @n
	BEGIN
		SET @i = @i + 1
		SET @uname = CONCAT(@i, @name)
		INSERT INTO users10k VALUES(@i, @uname);
	END
GO

exec insert_n_users 10000, 'bhagavan';

SELECT * INTO sample10k FROM users10k;
SELECT * INTO sample10k_CI FROM users10k;

SELECT * from users10k;
SELECT * FROM sample10k;
SELECT * FROM sample10k_CI;

--CREATE CLUSTERED INDEX IX_sample10k_CI_Id ON sample10k_CI(id)
CREATE CLUSTERED INDEX IX_sample10k_CI_name ON sample10k_CI(name)

SELECT * FROM sample10k;
SELECT * FROM sample10k_CI;

select * from sample10k WHERE id=5000;
select * from sample10k_CI WHERE id=5000;

select * from sample10k WHERE name='5000bhagavan';
select * from sample10k_CI WHERE name='5000bhagavan';

---------------------------------------
ALTER TABLE users10k add primary key(id);
ALTER TABLE sample10k add primary key(id);
ALTER TABLE sample10k_ci add primary key(id);



exec sp_help  'users10k'
DROP INDEX IX_sample10k_CI_Id ON sample10k_CI;

GO
	

USE sample_data;

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary DECIMAL(10, 2),
	Address varchar (10),
);

CREATE TABLE EmployeeDOB (
    EmployeeID INT PRIMARY KEY,
	edob DATE
);


SELECT * from Employee;
SELECT * from EmployeeDOB;

ALTER TABLE Employee
ALTER COLUMN Address VARCHAR(100);

INSERT INTO EmployeeDOB(EmployeeID, edob)
SELECT Employee.EmployeeID, CAST(DATEADD(day, ABS(CHECKSUM(NEWID())) % 5000, '2070-01-01') AS DATE) AS random_date
FROM Employee
WHERE Employee.EmployeeID > 0;

SELECT CAST(DATEADD(day, ABS(CHECKSUM(NEWID())) % 5000, '2070-01-01') AS DATE) AS random_date;


INSERT INTO Employee (EmployeeID, FirstName, LastName, Salary, Address)
VALUES
    (1, 'Amit', 'Sharma', 50000.00, 'House No. 101, Gandhi Nagar, Delhi'),
    (2, 'Priya', 'Patel', 60000.00, 'Flat No. 302, Lotus Apartments, Mumbai'),
    (3, 'Rahul', 'Desai', 55000.00, 'Plot No. 45, Jayanagar, Bangalore'),
    (4, 'Neha', 'Reddy', 65000.00, 'House No. 205, Jubilee Hills, Hyderabad'),
    (5, 'Vivek', 'Gupta', 52000.00, 'Street No. 15, Koramangala, Bangalore'),
    (6, 'Ananya', 'Singh', 58000.00, 'Apartment No. 402, Green Valley, Pune'),
    (7, 'Raj', 'Kumar', 53000.00, 'House No. 301, Indira Nagar, Lucknow'),
    (8, 'Sneha', 'Chopra', 61000.00, 'Flat No. 501, Silver Heights, Kolkata'),
    (9, 'Aakash', 'Jain', 54000.00, 'Plot No. 22, Vaishali Nagar, Jaipur'),
    (10, 'Anjali', 'Shah', 62000.00, 'Apartment No. 102, Golden Plaza, Ahmedabad'),
    (11, 'Aditya', 'Verma', 57000.00, 'House No. 703, Model Town, Chandigarh'),
    (12, 'Shreya', 'Pandey', 64000.00, 'Flat No. 802, Royal Residency, Chennai'),
    (13, 'Prateek', 'Yadav', 54000.00, 'Street No. 25, Sector 15, Noida'),
    (14, 'Arun', 'Sharma', 59000.00, 'House No. 12, MG Road, Gurgaon'),
    (15, 'Divya', 'Kaur', 53000.00, 'Apartment No. 205, DLF City, Faridabad'),
    (16, 'Anushka', 'Singhania', 63000.00, 'Flat No. 502, Silver Oaks, Mumbai'),
    (17, 'Karan', 'Mishra', 56000.00, 'Plot No. 35, Baner Road, Pune'),
    (18, 'Shivani', 'Choudhary', 60000.00, 'House No. 501, Janakpuri, Delhi'),
    (19, 'Aryan', 'Agarwal', 55000.00, 'Apartment No. 401, Lakeview Towers, Bangalore'),
    (20, 'Isha', 'Malhotra', 64000.00, 'Street No. 10, Rajouri Garden, Delhi');


CREATE OR ALTER PROCEDURE dbo.csp_GetData
(
	@EmpID int 
)
AS
BEGIN
	SELECT * from Employee WHERE EmployeeID=@EmpID;
END

EXEC csp_GetData @EmpID = 5

CREATE OR ALTER PROCEDURE dbo.csp_GetData
(
	@EmpID int 
)
AS
BEGIN
	SELECT emp.EmployeeID, emp.FirstName, edob.edob
	FROM Employee as emp
	LEFT JOIN EmployeeDOB AS edob ON edob.EmployeeID = emp.EmployeeID
	WHERE emp.EmployeeID = @EmpID
END
EXEC csp_GetData @EmpID = 5


CREATE OR ALTER PROCEDURE dbo.csp_GetData
(
	@EmpID int = 10
)
AS
BEGIN
	SELECT emp.EmployeeID, emp.FirstName, edob.edob
	FROM Employee as emp
	LEFT JOIN EmployeeDOB AS edob ON edob.EmployeeID = emp.EmployeeID
	WHERE emp.EmployeeID = @EmpID
END

EXEC csp_GetData @EmpID = 5
EXEC csp_GetData

CREATE OR ALTER PROCEDURE dbo.csp_GetData
(
	@EmpID int = NULL,
	@EmpID int = NULL
)
AS
BEGIN
	SELECT emp.EmployeeID, emp.FirstName, edob.edob
	FROM Employee as emp
	LEFT JOIN EmployeeDOB AS edob ON edob.EmployeeID = emp.EmployeeID
	WHERE emp.EmployeeID = @EmpID OR @EmpID IS NULL
END

EXEC csp_GetData @EmpID = 5
EXEC csp_GetData


CREATE OR ALTER FUNCTION select_gender(@gender as varchar(20))
RETURNS table
AS
RETURN
(
	SELECT * FROM Employee
)

SELECT * FROM dbo.select_gender('Male');


CREATE OR ALTER PROCEDURE dbo.csp_GetData
(
	@EmpID int = NULL
)
AS
BEGIN
	SELECT emp.EmployeeID, emp.FirstName, edob.edob
	FROM Employee as emp
	LEFT JOIN EmployeeDOB AS edob ON edob.EmployeeID = emp.EmployeeID
	WHERE emp.EmployeeID = @EmpID OR @EmpID IS NULL
END

EXEC csp_GetData @EmpID = 5
EXEC csp_GetData


------------------------------
CREATE OR ALTER PROCEDURE dbo.csp_GetData
(
	@EmpID int = NULL
	, @FName varchar(100)
)
AS
BEGIN
	SELECT emp.EmployeeID, emp.FirstName, emp.LastName
	FROM Employee as emp
	WHERE emp.EmployeeID = @EmpID OR emp.FirstName = @FName
END

EXEC csp_GetData @EmpID = 4, @FName = "Priya"
EXEC csp_GetData @FName = "Neha"
EXEC csp_GetData

==========VIEWS=================
CREATE OR ALTER VIEW  vw_GetEmplyeeData
AS
	SELECT EmployeeID, FirstName FROM Employee
	WHERE EmployeeID > 10

SELECT * FROM vw_GetEmplyeeData
------------------------------
CREATE OR ALTER VIEW  vw_GetEmplyeeDataBackupData
WITH SCHEMABINDING
AS
	SELECT EmployeeID, FirstName FROM dbo.EmployeeBackup

SELECT * INTO  EmployeeBackup FROM Employee; 
SELECT * FROM vw_GetEmplyeeDataBackupData; 
ALTER TABLE EmployeeBackup DROP COLUMN FirstName;
INSERT INTO vw_GetEmplyeeDataBackupData(100, "Bhagavan")
INSERT INTO vw_GetEmplyeeDataBackupData(EmployeeID, FirstName)
SELECT 21, "Bhagavan"
------------------------------
CREATE DATABASE test_data;
USE test_data;

CREATE TABLE test_table_sno 
==========VIEWS=================


--Show all databases
SELECT * FROM sys.databases ORDER BY create_date DESC;  

-- Show all tables
select * from information_schema.tables

-- Delete Databases
DROP DATABASE happy, school, hospital, test_data;

CREATE DATABASE relDB
USE relDB
USE sample_data
CREATE TABLE Students (
	StudentID int,
	sName varchar(128), 
	email varchar(128), 
	sDOB date,
	Primary Key (StudentID)
	)

CREATE TABLE Teachers (
	TeacherID int,
	tName varchar(128), 
	temail varchar(128), 
	tHireDate date,
	Primary Key (TeacherID)
	)

CREATE TABLE Course (
	CourseID int,
	cTitle varchar(128), 
	AssignedTeacherID int foreign key REFERENCES Teachers(TeacherID),
	Primary Key (CourseID)
	)

CREATE TABLE Enrollments (
	EnrollmentID int Primary Key,
	StuID int foreign key REFERENCES Students(StudentID),
	CourID int foreign key REFERENCES Course(CourseID),
	)

SELECT * from Students
SELECT * from Teachers
SELECT * from Course
SELECT * from Enrollments

INSERT INTO Students (StudentID, sName, email, sDOB) VALUES 
(1, 'Rahul Sharma', 'rahul.sharma@example.com', '2000-01-15'),
(2, 'Priya Singh', 'priya.singh@example.com', '1999-04-22'),
(3, 'Ankit Patel', 'ankit.patel@example.com', '2001-07-09'),
(4, 'Neha Gupta', 'neha.gupta@example.com', '2000-12-30'),
(5, 'Amit Verma', 'amit.verma@example.com', '1998-11-18');


INSERT INTO Teachers (TeacherID, tName, temail, tHireDate) VALUES 
(1, 'Dr. Suresh Kumar', 'suresh.kumar@example.com', '2010-09-01'),
(2, 'Mr. Rakesh Mehta', 'rakesh.mehta@example.com', '2012-06-15'),
(3, 'Ms. Anjali Rao', 'anjali.rao@example.com', '2015-08-23'),
(4, 'Prof. Vinod Menon', 'vinod.menon@example.com', '2008-03-30'),
(5, 'Dr. Kavita Nair', 'kavita.nair@example.com', '2011-11-05');

INSERT INTO Course (CourseID, cTitle, AssignedTeacherID) VALUES 
(1, 'Introduction to Computer Science', 1),
(2, 'Calculus I', 2),
(3, 'Physics I', 3),
(4, 'English Literature', 4),
(5, 'Biology 101', 5);


INSERT INTO Enrollments (EnrollmentID, StuID, CourID) VALUES 
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 1, 2),
(7, 2, 3),
(8, 3, 4),
(9, 4, 5),
(10, 5, 1);




	SELECT  Dept, gender,
	 SUM (salary) as Total 
	FROM Department group by rollup(dept,gender)

	select @@VERSION