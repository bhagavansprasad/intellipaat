    declare @count nchar(10)
    SET @count = 'a'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nchar(10)
    SET @count = 'abcd'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nchar(20)
    SET @count = 'సరే'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count nvarchar(10)
    SET @count = 'a'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nvarchar(10)
    SET @count = 'abcd'
    select @count as Number, datalength(@count) as DataTypeLen

    declare @count nvarchar(20)
    SET @count = 'సరే'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count date
    SET @count = '2024-05-20'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count date
    SET @count = '20-05-2024'
    select @count as Number, datalength(@count) as DataTypeLen


	declare @count time
    SET @count = '10:15:20'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count time
    SET @count = '10:15:20:2'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count time
    SET @count = '10:15:20:23'
    select @count as Number, datalength(@count) as DataTypeLen

	declare @count time
    SET @count = '10:15:20:234'
    select @count as Number, datalength(@count) as DataTypeLen


	declare @count1 smalldatetime
	declare @count2 datetime
	declare @count3 datetime2
    SET @count1 = '2024-10-15 10:15:20:234'
    SET @count2 = '2024-10-15 10:15:20:234'
    SET @count3 = '2024-10-15 10:15:20:234'
    select @count1 as Number, datalength(@count1) as DataTypeLen
    select @count2 as Number, datalength(@count2) as DataTypeLen
    select @count3 as Number, datalength(@count3) as DataTypeLen
