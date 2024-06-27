
--####################################
--Step 1 
--Open --> sql server --> run a command 
	
		Select @@version
		
--Step 2
https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms

--OLTP  -->AdventureWorks2022.bak

--step 3 
--create the folder in C drive with your name and copy the backup file

--####################################
Extension for the SQl server file =.sql 
--session id 1- 50 for system / internal process
currently 32767 users can connet simultaneously to my sql server

 INstance name =THELON\DEMO
 login name =THELON\Balje
 session id =51
 databasename =master
 
--####################################
Datatypes in SQl server .
Numeric
Exact number
--tinyint	Range(0 to 255), 1 Byte
	--DECLARE: This is used to declare a variable.
	--SET: This is used to assign a value to a variable.
	--SELECT: This is used to read/ print data from a variable 
	@= temporary 
	 name = variable(number , char, date time)
	 @name= temporary variable
--##########################################################

--tinyint	Range(0 to 255), 1 Byte
	    declare @value  tinyint
		SET @value=255
		select @value

		declare @value  tinyint
		SET @value=0
		select @value

  declare @value  tinyint
		SET @value=-1
		select @value
		
  declare @ename  tinyint
		SET @ename=254
		select @ename
--##########################################################
--smallint	Range(-32,768 to 32,767),	2 Bytes


	declare @value  smallint
	SET @value=-1
	select @value
		

	declare @value  smallint
	SET @value=-4567890
	select @value

--##########################################################		
--int	Range(-2,147,483,648 to 2,147,483,647),	4 Bytes
	
	declare @value  int
	SET @value=-4567890
	select @value  ,datalength(@value)  

	declare @value1  int
	SET @value1=-4567890
	select @value1 as Number ,datalength(@value) Byte 
	

	declare @value  int
	SET @value=-2147483648
	select @value as Number ,datalength(@value) Byte 

	declare @value  int
	SET @value= 8888899999
	select @value as Number ,datalength(@value) Byte 

--##########################################################		
--bigint	Range(-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)	8 Bytes

	declare @value  bigint
	SET @value= 8888899999
	select @value as Number ,datalength(@value) Byte 

	declare @value  bigint
	SET @value= 9223372036854775807
	select @value as Number ,datalength(@value) Byte 





















































































































































































































































































































































































































































































































































































