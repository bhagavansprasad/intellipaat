--1. Create a stored procedure to display the restaurant name, type and cuisine where the table booking is not zero.
     --   Restaurant: restaurant ID, restaurant name, cuisine type, table-booking, Rating
     --   Booking   : restaurant ID, table-booking, date, time, rating
	
--2. Create a transaction and update the cuisine type ‘Cafe’ to ‘Cafeteria’. Check the result and rollback it.

--3. Generate a row number column and find the top 5 areas with the highest rating of restaurants.

--4. Use the while loop to display the 1 to 50.
--5. Write a query to Create a Top rating view to store the generated top 5 highest rating of restaurants.
--6. Write a trigger that sends an email notification to the restaurant owner whenever a new record is inserted.

use assignments
CREATE TABLE Restaurants (
    RestaurantID INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantName VARCHAR(255) NOT NULL,
    CuisineType VARCHAR(100) NOT NULL,
    Rating DECIMAL(3, 2) CHECK (Rating >= 0 AND Rating <= 5)
);

CREATE TABLE Booking (
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantID INT,
	DBooking date,
	TBooking time,
    Rating DECIMAL(3, 2) CHECK (Rating >= 0 AND Rating <= 5),
	FOREIGN KEY (RestaurantID) REFERENCES Restaurants(RestaurantID)
);


INSERT INTO Booking (RestaurantID, DBooking, TBooking, Rating)
VALUES
(FLOOR(RAND()*(10-5+1)+1), '2024-06-01', '18:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-02', '19:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-03', '20:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-04', '18:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-05', '17:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-06', '19:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-07', '20:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-08', '18:15:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-09', '19:45:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-10', '21:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-11', '18:45:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-12', '19:15:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-13', '20:45:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-14', '18:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-15', '19:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-16', '20:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-17', '21:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-18', '18:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-19', '19:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-20', '20:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-21', '21:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-22', '18:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-23', '19:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-24', '20:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-25', '21:00:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-26', '18:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-27', '19:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-28', '20:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-29', '21:30:00', ROUND(2 + (RAND() * 3), 2)),
(FLOOR(RAND()*(20-5+1)+1), '2024-06-30', '18:00:00', ROUND(2 + (RAND() * 3), 2));

--1. Create a stored procedure to display the restaurant name, type and cuisine where the table booking is not zero.
     --   Restaurant: restaurant ID, restaurant name, cuisine type, table-booking, Rating
     --   Booking   : restaurant ID, table-booking, date, time, rating

	CREATE OR ALTER PROCEDURE List_Booked_restaurants
	AS
		SELECT bkng.RestaurantID, rest.RestaurantName, bkng.DBooking, bkng.TBooking
		FROM Booking AS bkng LEFT JOIN Restaurants AS rest
		ON  bkng.RestaurantID=rest.RestaurantID
		ORDER BY bkng.RestaurantID ASC
	GO

	exec List_Booked_restaurants

--2. Create a transaction and update the cuisine type ‘Cafe’ to ‘Cafeteria’. Check the result and rollback it.

	BEGIN TRY
		BEGIN TRANSACTION
			UPDATE Restaurants set CuisineType='Cafeteria' 
				WHERE CuisineType='Cafe'
			COMMIT TRANSACTION 
			Print 'Transaction is committed'
	END TRY
	BEGIN CATCH
		ROLLBACK TRANSACTION
		Print 'Transaction is rollback'
	END CATCH

--3. Generate a row number column and find the top 5 areas with the highest rating of restaurants.
	WITH RankedRestaurants AS (
		SELECT 
			ROW_NUMBER() OVER (ORDER BY Rating DESC) AS RowNum, *
		FROM Restaurants
	)
	SELECT * 
	FROM RankedRestaurants
	WHERE RowNum <= 5;


--4. Use the while loop to display the 1 to 50.
	DECLARE
		@i int = 1,
		@n int = 50
	WHILE @i <= @n
	BEGIN
		Print @i
		SET @i = @i + 1
	END

--5. Write a query to Create a Top rating view to store the generated top 5 highest rating of restaurants.
	DROP VIEW top_rated_Restaurants
	CREATE OR ALTER VIEW top_rated_Restaurants
	AS
    SELECT TOP 5 * FROM Restaurants ORDER BY Rating DESC

	SELECT * FROM top_rated_Restaurants


--6. Write a trigger that sends an email notification to the restaurant owner whenever a new record is inserted.
	CREATE TRIGGER when_record_inserted
	ON Restaurants
	FOR INSERT 
	AS
	BEGIN
       DECLARE @RestaurantID int
       SELECT @RestaurantID = INSERTED.RestaurantID FROM INSERTED
       declare @body varchar(500) = 'RestaurantID: ' + CAST(@RestaurantID AS VARCHAR(5)) + ' inserted.'
       EXEC msdb.dbo.sp_send_dbmail
            @profile_name = 'Bhagavan'
           ,@recipients = 'admin@gmail.com'
           ,@subject = 'New Customer Record'
           ,@body = @body
           ,@importance ='HIGH'
		Print "Triggered email in inserting record"
	END
		
	INSERT INTO Restaurants VALUES('Kadapa', 'South Indian', ROUND(2 + (RAND() * 3), 2))

