--1. Insert a new record in your Orders table.
	INSERT INTO Orders 
	(OrderId, CustomerId, SalesmanId, OrderDate, Amount) 
	VALUES (5004, 1575, 102, '2024-06-04', 2000)

--2. 
	--Add Primary key constraint for SalesmanId column in Salesman table. 
	ALTER TABLE Salesman add primary key(SalesmanId);

	--Add default constraint for City column in Salesman table. 
	ALTER TABLE Salesman
	ADD CONSTRAINT City
	DEFAULT 'Bengaluru' FOR City

	--Add Foreign key constraint for SalesmanId column in Customer table. 
	ALTER TABLE Customer
	ADD CONSTRAINT FK_SalesmanId
	FOREIGN KEY (SalesmanId) REFERENCES Salesman(SalesmanId);

	--Add not null constraint in Customer_name column for the Customer table.
	ALTER TABLE Customer  
	ALTER COLUMN CustomerName VARCHAR(255) NOT NULL 

--3. Fetch the data where the Customer’s name is ending with ‘N’ also get the purchase amount value greater than 500.
	SELECT * FROM Customer where CustomerName LIKE '%N' AND PurchaseAmount > 500

--4. Using SET operators, retrieve the first result with unique SalesmanId values from two tables, 
--   and the other result containing SalesmanId with duplicates from two tables.

	SELECT SalesmanId FROM Salesman
	INTERSECT
	SELECT SalesmanId FROM Customer

	SELECT SalesmanId FROM Salesman
	UNION
	SELECT SalesmanId FROM Customer

--5. Display the below columns which has the matching data. 
--   Orderdate, Salesman Name, Customer Name, Commission, and City which has the
--   range of Purchase Amount between 500 to 1500.

	SELECT ordrs.Orderdate, sales.Name, sales.Commission, sales.City, ordrs.Amount
	FROM Orders AS ordrs LEFT JOIN Salesman AS sales
	ON  ordrs.SalesmanId=sales.SalesmanId
	WHERE  ordrs.Amount >= 500 AND ordrs.Amount <= 1500

--6. Using right join fetch all the results from Salesman and Orders table
	SELECT * FROM Salesman AS sales LEFT JOIN Orders AS ordr
	ON sales.SalesmanId=ordr.SalesmanId
