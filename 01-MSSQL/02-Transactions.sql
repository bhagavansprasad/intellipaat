Set of SQL operations Performaced in a sequence 
use sample_data
SELECT * FROM Employee WHERE EmployeeID=1
SELECT * FROM Employee WHERE EmployeeID=111

SET TRANSACTION ISOLATION LEVEL READ COMMITTED
BEGIN TRANSACTION
	UPDATE e
	SET e.LastName ='Yadav'
	FROM Employee AS e
	WHERE EmployeeID = 1
ROLLBACK TRANSACTION
COMMIT TRANSACTION
END

------------------------
BEGIN TRY
	SELECT 1/0
END TRY
BEGIN CATCH
	PRINT 'Cathch block is hit'
	DECLARE @ErrorMessage VARCHAR(1000)
	SET @ErrorMessage = ERROR_MESSAGE()
	SELECT @ErrorMessage
END CATCH
------------------------
CREATE OR ALTER PROCEDURE spName
AS
BEGIN
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	BEGIN TRY
		BEGIN TRANSACTION
			UPDATE e
			SET e.LastName ='Yadav'
			FROM Employee AS e
			WHERE EmployeeID = 1

			INSERT INTO Employee(EmployeeID, FirstName, LastName, Salary, Address)
			SELECT 111, 'Hello', 'World', 1111, 'India'

			--UPDATE Employee
			--SET EmployeeID = 1/0
			--WHERE EmployeeID = 1
		COMMIT TRANSACTION
		SELECT 'TransactionCommitted'
	END TRY
	BEGIN CATCH
		ROLLBACK TRANSACTION
		SELECT 'TransactionRolledBack'
		PRINT 'Cathch block is hit'
		DECLARE @ErrorMessage VARCHAR(1000)
		SET @ErrorMessage = ERROR_MESSAGE()
		SELECT @ErrorMessage
	END CATCH
END

EXEC spName


------------SUB Query------------
SELECT * 
FROM Employee
WHERE Salary > (SELECT AVG(Salary) FROM Employee)

