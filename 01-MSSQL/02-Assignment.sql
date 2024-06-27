use assignments
CREATE TABLE Restaurants (
    RestaurantID INT IDENTITY(1,1) PRIMARY KEY,
    RestaurantName VARCHAR(255) NOT NULL,
    CuisineType VARCHAR(100) NOT NULL,
    Rating DECIMAL(3, 2) CHECK (Rating >= 0 AND Rating <= 5)
);

INSERT INTO Restaurants (RestaurantName, CuisineType, Rating) VALUES
('Tandoori Palace', 'North Indian', ROUND(2 + (RAND() * 3), 2)),
('Curry House', 'South Indian', ROUND(2 + (RAND() * 3), 2)),
('Maharajas Feast', 'Punjabi', ROUND(2 + (RAND() * 3), 2)),
('Spice Route', 'Gujarati', ROUND(2 + (RAND() * 3), 2)),
('Saffron Delight', 'Rajasthani', ROUND(2 + (RAND() * 3), 2)),
('The Royal Peacock', 'Bengali', ROUND(2 + (RAND() * 3), 2)),
('Masala Magic', 'Keralan', ROUND(2 + (RAND() * 3), 2)),
('Bombay Bistro', 'Maharashtrian', ROUND(2 + (RAND() * 3), 2)),
('The Golden Curry', 'Goan', ROUND(2 + (RAND() * 3), 2)),
('Shahi Thali', 'North Indian', ROUND(2 + (RAND() * 3), 2)),
('Rasa Indian Cuisine', 'South Indian', ROUND(2 + (RAND() * 3), 2)),
('Mughal Mahal', 'Mughlai', ROUND(2 + (RAND() * 3), 2)),
('The Spice Bazaar', 'Indian Street Food', ROUND(2 + (RAND() * 3), 2)),
('Flavors of India', 'Punjabi', ROUND(2 + (RAND() * 3), 2)),
('Chutney Garden', 'Gujarati', ROUND(2 + (RAND() * 3), 2)),
('Namaste Kitchen', 'Rajasthani', ROUND(2 + (RAND() * 3), 2)),
('Maharanis Table', 'Bengali', ROUND(2 + (RAND() * 3), 2)),
('India Gate', 'North Indian', ROUND(2 + (RAND() * 3), 2)),
('The Curry Leaf', 'South Indian', ROUND(2 + (RAND() * 3), 2)),
('Spice Junction', 'Keralan', ROUND(2 + (RAND() * 3), 2)
);

INSERT INTO Restaurants (RestaurantName, CuisineType, Rating)
VALUES
-- Cafe type restaurants
('Brewed Awakenings', 'Cafe', ROUND(2 + (RAND() * 3), 2)),
('Morning Glory Cafe', 'Cafe', ROUND(2 + (RAND() * 3), 2)),
('Cafe Mocha', 'Cafe', ROUND(2 + (RAND() * 3), 2)),
('Sunrise Cafe', 'Cafe', ROUND(2 + (RAND() * 3), 2)),
('The Coffee Spot', 'Cafe', ROUND(2 + (RAND() * 3), 2)),
('Espresso Express', 'Cafe', ROUND(2 + (RAND() * 3), 2)),
('Quick Bite Cafeteria', 'CaFeteria', ROUND(2 + (RAND() * 3), 2)),
('Metro Cafeteria', 'CaFeteria', ROUND(2 + (RAND() * 3), 2)),
('Tech Park Cafeteria', 'CaFeteria', ROUND(2 + (RAND() * 3), 2));

--1. Create a user-defined functions to stuff the Chicken into ‘Quick Bites’. Eg: ‘Quick Chicken Bites’.
--2. Use the function to display the restaurant name and cuisine type which has the maximum number of rating.
	CREATE OR ALTER PROCEDURE Quick_Chicken_Bytes
	@tstr varchar(64)
	AS
		SELECT STRING_AGG(value, ' Chiken ') AS concatenatedString
		FROM STRING_SPLIT (@tstr , ' ')
		
		SELECT top 1 RestaurantName, CuisineType, Rating FROM Restaurants ORDER BY Rating DESC
	GO
	exec Quick_Chicken_Bytes 'Quick Bytes'

--3. Create a Rating Status column to display the rating as 
	--If Rating is
	--    Excellent >= 4
	--    >= 3.5 Good < 4
	--    >= 3   Average < 3.5
	--    Bad < 3
	SELECT RestaurantName, CuisineType, Rating, 
		IIF(Rating >=4, 'Excellent', 
			IIF(Rating >=3.5 AND Rating < 4, 'Good',
				IIF(Rating >=3 AND Rating < 3.5, 'Average', 'Bad')
			)
		)
		as status
		FROM Restaurants order by Rating DESC

--4. Find the Ceil, floor and absolute values of the rating column 
--   and display the current date
--   and separately display the year, month_name and day.
	SELECT RestaurantName, CuisineType, Rating, 
		CEILING(Rating) as CeilV, 
		FLOOR(Rating) as FloorV, 
		ABS (Rating) as Absolute,
		FORMAT(GETDATE(), 'yyyy') as Year,
		FORMAT(GETDATE(), 'MMMM') as Month,
		DATENAME(dd,GETDATE()) AS day
		FROM Restaurants order by Rating DESC

--5. Display the restaurant type and total average cost using rollup.
	SELECT CuisineType, Rating, 
		CAST(AVG(Rating) AS DECIMAL(2,1)) as AvgRating 
		FROM Restaurants 
		GROUP BY 
		ROLLUP(CuisineType, Rating)
