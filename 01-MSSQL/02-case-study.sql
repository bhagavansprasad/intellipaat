CREATE DATABASE casestudy2
use casestudy2

CREATE TABLE LOCATION (
	Location_ID INT PRIMARY KEY,
	City VARCHAR(50)
);

INSERT INTO LOCATION (Location_ID, City) VALUES 
	(122, 'New York'),
	(123, 'Dallas'),
	(124, 'Chicago'),
	(167, 'Boston');

CREATE TABLE DEPARTMENT (
	Department_Id INT PRIMARY KEY,
	Name VARCHAR(50),
	Location_Id INT,
	FOREIGN KEY (Location_Id) REFERENCES LOCATION(Location_ID)
);

INSERT INTO DEPARTMENT (Department_Id, Name, Location_Id) VALUES 
	(10, 'Accounting', 122),
	(20, 'Sales', 124),
	(30, 'Research', 123),
	(40, 'Operations', 167);

CREATE TABLE JOB (
	Job_ID INT PRIMARY KEY,
	Designation VARCHAR(50)
);

INSERT  INTO JOB VALUES
	(667, 'CLERK'),
	(668,'STAFF'),
	(669,'ANALYST'),
	(670,'SALES_PERSON'),
	(671,'MANAGER'),
	(672, 'PRESIDENT')


CREATE TABLE EMPLOYEE(
	EMPLOYEE_ID INT,
	LAST_NAME VARCHAR(20),
	FIRST_NAME VARCHAR(20),
	MIDDLE_NAME CHAR(1),
	JOB_ID INT FOREIGN KEY
	REFERENCES JOB(JOB_ID),
	MANAGER_ID INT,
	HIRE_DATE DATE,
	SALARY INT,
	COMM INT,
	DEPARTMENT_ID  INT FOREIGN KEY
	REFERENCES DEPARTMENT(DEPARTMENT_ID)
)

INSERT INTO EMPLOYEE VALUES
	(7369,'SMITH','JOHN','Q',667,7902,'17-DEC-84',800,NULL,20),
	(7499,'ALLEN','KEVIN','J',670,7698,'20-FEB-84',1600,300,30),
	(7505,'DOYLE','JEAN','K',671,7839,'04-APR-85',2850,NULl,30),
	(7506,'DENNIS','LYNN','S',671,7839,'15-MAY-85',2750,NULL,30),
	(7507,'BAKER','LESLIE','D',671,7839,'10-JUN-85',2200,NULL,40),
	(7521,'WARK','CYNTHIA','D',670,7698,'22-FEB-85',1250,500,30)

SELECT * FROM LOCATION
SELECT * FROM DEPARTMENT 
SELECT * FROM JOB
SELECT * FROM EMPLOYEE

--Simple Queries:
--1. List all the employee details.
	SELECT * FROM EMPLOYEE

--2. List all the department details.
	SELECT * FROM DEPARTMENT 

--3. List all job details.
	SELECT * FROM JOB

--4. List all the locations.
	SELECT * FROM LOCATION

--5. List out the First Name, Last Name, Salary, Commission for all Employees.
	SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID FROM EMPLOYEE

--6. List out the Employee ID, Last Name, Department ID for all employees and alias
--   Employee ID as "ID of the Employee", Last Name as "Name of the Employee", Department ID as "Dep_id".
	SELECT 
		EMPLOYEE_ID AS 'ID of the Employee', 
		LAST_NAME AS 'Name of the Employee', 
		DEPARTMENT_ID AS 'Dep_id'
	FROM EMPLOYEE

--7. List out the annual salary of the employees with their names only.
	SELECT 
		CONCAT(FIRST_NAME, ' ', MIDDLE_NAME, ' ', LAST_NAME) AS 'Employee Name',
		SALARY
	FROM EMPLOYEE

--WHERE Condition:
--1. List the details about "Smith".
	SELECT * FROM EMPLOYEE WHERE 'Smith' IN (FIRST_NAME, MIDDLE_NAME, LAST_NAME)

--2. List out the employees who are working in department 20.
	SELECT * FROM EMPLOYEE WHERE DEPARTMENT_ID=20

--3. List out the employees who are earning salary between 2000 and 3000.
	SELECT * FROM EMPLOYEE WHERE SALARY BETWEEN 2000 AND 3000

--4. List out the employees who are working in department 10 or 20.
	SELECT * FROM EMPLOYEE WHERE DEPARTMENT_ID IN(10, 20)

--5. Find out the employees who are not working in department 10 or 30.
	SELECT * FROM EMPLOYEE WHERE DEPARTMENT_ID NOT IN(10, 30)

--6. List out the employees whose name starts with 'L'.
	SELECT * FROM EMPLOYEE WHERE FIRST_NAME LIKE 'L%' OR MIDDLE_NAME LIKE 'L%' OR LAST_NAME LIKE 'L%'

--7. List out the employees whose name starts with 'L' and ends with 'E'.
	SELECT * FROM EMPLOYEE WHERE FIRST_NAME LIKE 'L%E' OR MIDDLE_NAME LIKE 'L%E' OR LAST_NAME LIKE 'L%E'

--8. List out the employees whose name length is 4 and start with 'J'.
	SELECT * FROM EMPLOYEE 
		WHERE (FIRST_NAME LIKE 'J%' OR MIDDLE_NAME LIKE 'J%' OR LAST_NAME LIKE 'J%') 
		AND (LEN(FIRST_NAME) = 4 OR LEN(MIDDLE_NAME) = 4  OR LEN(LAST_NAME) = 4)

--9. List out the employees who are working in department 30 and draw the salaries more than 2500.
	SELECT * FROM EMPLOYEE 
		WHERE DEPARTMENT_ID=30 AND
		SALARY > 2500

--10. List out the employees who are not receiving commission.
	SELECT * FROM EMPLOYEE 
		WHERE COMM IS NULL

--ORDER BY Clause:
--1. List out the Employee ID and Last Name in ascending order based on the Employee ID.
	SELECT EMPLOYEE_ID, LAST_NAME FROM EMPLOYEE ORDER BY EMPLOYEE_ID

--2. List out the Employee ID and Name in descending order based on salary.
	SELECT EMPLOYEE_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME FROM EMPLOYEE ORDER BY SALARY

--3. List out the employee details according to their Last Name in ascending-order.
	SELECT * FROM EMPLOYEE ORDER BY LAST_NAME ASC

--4. List out the employee details according to their Last Name in ascending order and then Department ID in descending order.
	SELECT * FROM EMPLOYEE 
	ORDER BY LAST_NAME ASC, DEPARTMENT_ID DESC

--GROUP BY and HAVING Clause:
--1. List out the department wise maximum salary, minimum salary and average salary of the employees.
	SELECT 
		DEPARTMENT_ID,
		MAX(SALARY) AS 'Maximum Salary',
		MIN(SALARY) AS 'Minimum Salary',
		AVG(SALARY) AS 'Average Salary'
	FROM EMPLOYEE
	GROUP BY DEPARTMENT_ID

--2. List out the job wise maximum salary, minimum salary and average salary of the employees.
	SELECT 
		JOB_ID,
		MAX(JOB_ID) AS 'Maximum Salary',
		MIN(JOB_ID) AS 'Minimum Salary',
		AVG(JOB_ID) AS 'Average Salary'
	FROM EMPLOYEE
	GROUP BY JOB_ID

--3. List out the number of employees who joined each month in ascending order.
	SELECT 
		JOB_ID,
		MAX(JOB_ID) AS 'Maximum Salary',
		MIN(JOB_ID) AS 'Minimum Salary',
		AVG(JOB_ID) AS 'Average Salary'
	FROM EMPLOYEE
	GROUP BY JOB_ID


--4. List out the number of employees for each month and year in ascending order based on the year and month.
	SELECT 
		MONTH(HIRE_DATE) AS 'Joined Month',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY MONTH(HIRE_DATE), YEAR(HIRE_DATE)
	ORDER BY MONTH(HIRE_DATE), YEAR(HIRE_DATE) DESC

--5. List out the Department ID having at least four employees.
	SELECT 
		DEPARTMENT_ID,
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY DEPARTMENT_ID
	HAVING COUNT(EMPLOYEE_ID) >= 4

--6. How many employees joined in February month.
	SELECT 
		MONTH(HIRE_DATE) AS 'Joined Month',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY MONTH(HIRE_DATE)
	HAVING MONTH(HIRE_DATE) = 2

--7. How many employees joined in May or June month.
	SELECT 
		MONTH(HIRE_DATE) AS 'Joined Month',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY MONTH(HIRE_DATE)
	HAVING MONTH(HIRE_DATE) IN (5, 6)

--8. How many employees joined in 1985?
	SELECT 
		YEAR(HIRE_DATE) AS 'Joined Year',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY YEAR(HIRE_DATE)
	HAVING YEAR(HIRE_DATE) = 1985

--9. How many employees joined each month in 1985?
	SELECT 
		YEAR(HIRE_DATE) AS 'Joined Year',
		MONTH(HIRE_DATE) AS 'Joined Month',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY YEAR(HIRE_DATE), MONTH(HIRE_DATE)
	HAVING YEAR(HIRE_DATE) = 1985

--10. How many employees were joined in April 1985?
	SELECT 
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY MONTH(HIRE_DATE), YEAR(HIRE_DATE)
	HAVING MONTH(HIRE_DATE) = 4 AND YEAR(HIRE_DATE) = 1985

--11. Which is the Department ID having greater than or equal to 3 employees joining in April 1985?
	SELECT 
		DEPARTMENT_ID,
		YEAR(HIRE_DATE) AS 'Joined Year',
		MONTH(HIRE_DATE) AS 'Joined Month',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE
	GROUP BY MONTH(HIRE_DATE), YEAR(HIRE_DATE), DEPARTMENT_ID
	HAVING MONTH(HIRE_DATE) = 4 AND YEAR(HIRE_DATE) = 1985 AND COUNT(EMPLOYEE_ID) >= 3

--Joins:
--1. List out employees with their department names.
	SELECT *, D.Name from EMPLOYEE AS E
	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id

--2. Display employees with their designations.
	SELECT *, J.Designation from EMPLOYEE AS E
	LEFT JOIN JOB AS J
	ON E.JOB_ID = J.Job_ID

--3. Display the employees with their department names and city.
	SELECT *, 
	D.Name AS 'Dept Name',
	L.City AS 'City'
	from EMPLOYEE AS E
	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id
	LEFT JOIN LOCATION AS L
	ON D.Location_Id = L.Location_ID

--4. How many employees are working in different departments? Display with department names.
	SELECT 
		D.Name AS 'Dept Name',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE AS E
	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id
	GROUP BY D.Name

	GROUP BY MONTH(HIRE_DATE), YEAR(HIRE_DATE), DEPARTMENT_ID
	HAVING MONTH(HIRE_DATE) = 4 AND YEAR(HIRE_DATE) = 1985 AND COUNT(EMPLOYEE_ID) >= 3

--5. How many employees are working in the sales department?
	SELECT 
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE AS E
	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id
	GROUP BY D.Name
	HAVING D.Name = 'Sales'

--6. Which is the department having greater than or equal to 3 employees and display the department names in ascending order.
	SELECT 
		D.Name AS 'Dept Name',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE AS E
	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id
	GROUP BY D.Name
	HAVING COUNT(EMPLOYEE_ID) >= 3

--7. How many employees are working in 'Dallas'?
	SELECT 
		L.City AS 'City',
		COUNT(EMPLOYEE_ID) AS 'Number of Employees'
	FROM EMPLOYEE AS E

	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id

	LEFT JOIN LOCATION AS L
	ON D.Location_Id = L.Location_ID
	GROUP BY L.City
	HAVING L.City = 'Dallas'

--8. Display all employees in sales or operation departments.
	SELECT * 
	FROM EMPLOYEE AS E
	LEFT JOIN DEPARTMENT AS D
	ON E.DEPARTMENT_ID = D.Department_Id
	WHERE D.Name IN ('Sales', 'Operations')

--CONDITIONAL STATEMENT
--1. Display the employee details with salary grades. Use conditional statement to create a grade column.
--Interpreted Grade Range
--	0     - 999 D
--	1000 - 1999 C
--	2000 - 2999 B
--	     > 3000 A
	SELECT *,
	IIF (E.Salary >= 0 AND E.Salary  <= 999, 'D GRADE', 
		IIF (E.Salary >= 1000 AND E.Salary  <= 1999, 'C GRADE', 
			IIF (E.Salary >= 2000 AND E.Salary  <= 2999, 'B GRADE',
				IIF (E.Salary >= 3000, 'A GRADE', 'NULL GRADE'))))
	FROM EMPLOYEE AS E
	ORDER BY SALARY ASC

--2. List out the number of employees grade wise. Use conditional statement to create a grade column.
	SELECT
	IIF (E.Salary >= 0 AND E.Salary  <= 999, 'D GRADE', 
		IIF (E.Salary >= 1000 AND E.Salary  <= 1999, 'C GRADE', 
			IIF (E.Salary >= 2000 AND E.Salary  <= 2999, 'B GRADE',
				IIF (E.Salary >= 3000, 'A GRADE', 'NULL GRADE')))) AS GRADE,
	COUNT(*) AS num_employees
	FROM EMPLOYEE AS E
	GROUP BY 
		IIF (E.Salary >= 0 AND E.Salary  <= 999, 'D GRADE', 
			IIF (E.Salary >= 1000 AND E.Salary  <= 1999, 'C GRADE', 
				IIF (E.Salary >= 2000 AND E.Salary  <= 2999, 'B GRADE',
					IIF (E.Salary >= 3000, 'A GRADE', 'NULL GRADE'))))

--3. Display the employee salary grades and the number of employees between 2000 to 5000 range of salary.
	SELECT
	IIF (E.Salary >= 0 AND E.Salary  <= 999, 'D GRADE', 
		IIF (E.Salary >= 1000 AND E.Salary  <= 1999, 'C GRADE', 
			IIF (E.Salary >= 2000 AND E.Salary  <= 2999, 'B GRADE',
				IIF (E.Salary >= 3000, 'A GRADE', 'NULL GRADE')))) AS GRADE,
	COUNT(*) AS num_employees
	FROM EMPLOYEE AS E
	WHERE salary BETWEEN 2000 AND 5000
	GROUP BY 
		IIF (E.Salary >= 0 AND E.Salary  <= 999, 'D GRADE', 
			IIF (E.Salary >= 1000 AND E.Salary  <= 1999, 'C GRADE', 
				IIF (E.Salary >= 2000 AND E.Salary  <= 2999, 'B GRADE',
					IIF (E.Salary >= 3000, 'A GRADE', 'NULL GRADE'))))
	
--Subqueries:
--1. Display the employees list who got the maximum salary.
	SELECT * FROM EMPLOYEE WHERE SALARY = (
		SELECT MAX(SALARY) FROM EMPLOYEE
	)

--2. Display the employees who are working in the sales department.
	SELECT *, D.Name FROM EMPLOYEE AS E
		LEFT JOIN DEPARTMENT AS D
		ON E.DEPARTMENT_ID = D.Department_Id	
		WHERE EMPLOYEE_ID = (
			SELECT EMPLOYEE_ID
			FROM EMPLOYEE AS E
			LEFT JOIN DEPARTMENT AS D
			ON E.DEPARTMENT_ID = D.Department_Id
			WHERE D.Name = 'Sales'
			)

--3. Display the employees who are working as 'Clerk'.
	SELECT *
		FROM EMPLOYEE AS E
		LEFT JOIN JOB AS J
		ON E.JOB_ID = J.Job_ID
		WHERE EMPLOYEE_ID = (
			SELECT EMPLOYEE_ID
			FROM EMPLOYEE AS E
			LEFT JOIN JOB AS J
			ON E.JOB_ID = J.Job_ID
			WHERE J.Designation = 'CLERK'
			)

--4. Display the list of employees who are living in 'Boston'.
	SELECT *FROM EMPLOYEE AS E
		WHERE EMPLOYEE_ID = (
			SELECT EMPLOYEE_ID
			FROM EMPLOYEE AS E
			LEFT JOIN DEPARTMENT AS D
			ON E.DEPARTMENT_ID = D.Department_Id
			LEFT JOIN LOCATION AS L
			ON D.Location_Id = L.Location_ID
			WHERE L.City = 'Boston'
			)

--5. Find out the number of employees working in the sales department.
	SELECT COUNT(*) FROM EMPLOYEE AS E
		LEFT JOIN DEPARTMENT AS D
		ON E.DEPARTMENT_ID = D.Department_Id	
		WHERE EMPLOYEE_ID = (
			SELECT EMPLOYEE_ID
			FROM EMPLOYEE AS E
			LEFT JOIN DEPARTMENT AS D
			ON E.DEPARTMENT_ID = D.Department_Id
			WHERE D.Name = 'Sales'
			)

--6. Update the salaries of employees who are working as clerks on the basis of 10%.
	BEGIN TRY
		BEGIN TRANSACTION
			SELECT * FROM EMPLOYEE 

			--A C T U A L   Q U E R Y
			UPDATE EMPLOYEE SET 
				Salary = Salary + (Salary * 10/100)
				WHERE EMPLOYEE_ID = (
					SELECT EMPLOYEE_ID
					FROM EMPLOYEE AS E
					LEFT JOIN JOB AS J
					ON E.JOB_ID = J.Job_ID
					WHERE J.Designation = 'CLERK'
					)

			SELECT * FROM EMPLOYEE 
		--COMMIT TRANSACTION 
			--NONE TO COMMIT
		ROLLBACK TRANSACTION
			Print 'Transaction is rollbacked, BECAUSE I DONT WANT TO MODIFY THE DATA'
	END TRY
	BEGIN CATCH
		ROLLBACK TRANSACTION
		Print 'Transaction is rollbacked, DUE TO EXCEPTION'
	END CATCH

--7. Display the second highest salary drawing employee details.
	SELECT * FROM EMPLOYEE WHERE Salary = (
		SELECT MAX(Salary) FROM EMPLOYEE WHERE Salary != (
			SELECT MAX(Salary) AS Maximum_Salary FROM EMPLOYEE
			)
		)

--8. List out the employees who earn more than every employee in department 30.
	SELECT * FROM EMPLOYEE WHERE Salary = (
		SELECT MAX(Salary) FROM EMPLOYEE WHERE DEPARTMENT_ID = 30
			)

--9. Find out which department has no employees.
	SELECT DEPARTMENT_ID FROM DEPARTMENT WHERE DEPARTMENT_ID NOT IN (
		SELECT 
		E.DEPARTMENT_ID
		FROM EMPLOYEE AS E
		LEFT JOIN DEPARTMENT AS D
		ON E.DEPARTMENT_ID = D.Department_Id
		GROUP BY E.DEPARTMENT_ID
	)

--10. Find out the employees who earn greater than the average salary for their department.
	SELECT * FROM EMPLOYEE AS E1
		WHERE SALARY >= (
			SELECT 
			AVG(SALARY)
			FROM EMPLOYEE AS E2
			WHERE E2.DEPARTMENT_ID = E1.DEPARTMENT_ID
			GROUP BY E2.DEPARTMENT_ID
	)

	SELECT * FROM EMPLOYEE order by salary
	SELECT * FROM DEPARTMENT
	SELECT * FROM LOCATION
	SELECT * FROM JOB


--EMPLOYEE           LOCATION
--	EMPLOYEE_ID         Location_ID
--	LAST_NAME           City
--	FIRST_NAME          
--	MIDDLE_NAME      DEPARTMENT
--	JOB_ID              Department_Id
--	MANAGER_ID          Name
--	HIRE_DATE           Location_Id
--	SALARY              
--	COMM             JOB
--	DEPARTMENT_ID       Job_ID
--						Designation

