--String,date time, conversion function 

--###########################################################
'asdfghjk!@#$%^&*1234567'

--replace ( string , old value, new value)

use AdventureWorks2022

 select BusinessEntityID, firstname, MiddleName, lastname,
 REPLACE(firstname , 'KIM', 'Ajay') as newname 
  FRom Person.Person



select BusinessEntityID, firstname, MiddleName, lastname,
REPLACE(BusinessEntityID , 2, 101) as newname 
FRom Person.Person

 --STUFF(string, start, length, new_string)

adventure
123456789
adven-ture
select  stuff('adventure',6, 0, '-')

select  stuff('adventure',6, 0, '12345')

MOUNTAINS
123456789

select  stuff('MOUNTAINS',6, 0, '-TABU')
select  stuff('MOUNTAINS',6, 1, '-TABU')
select  stuff('MOUNTAINS',9, 0, '-TABU')

--CHARINDEX(substring, string, start)
MOUNTAINS
123456789
select  CHARINDEX('A', 'MOUNTAINS')
select  CHARINDEX(' ', 'Alpha beta')
select  CHARINDEX('@', 'alpha@email.com')

select  CHARINDEX('a', 'Alphabeta',7 )
Alphabeta
123456789012345
Alpha@gmail.com
--substring(string, start, length)
select  substring('Alphabeta', 6,4 )

select  substring('Alphabeta', 1,5 )

select  substring('Alpha@gmail.com', 7,LEN('Alpha@gmail.com'))

--###############################################
create table empemail
(email varchar(100))


INSERT INTO empemail VALUES 
('jane.doe@example.com'),
('john.smith@workmail.net'),
('alex.jones@university.edu'),
('lisa.wong@techhub.org'),
('mike.brown@services.co.uk'),
('sara.lee@marketplace.com'),
('dave.wilson@creativeagency.us'),
('emily.harris@globalenterprise.com'),
('carlos.garcia@networksolutions.es'),
('anna.zhao@researchinst.cn');

select * from empemail

select email ,
sUBSTRING(EMAIL,CHARINDEX('@',EMAIL)+1, LEN(email))
from empemail


--input ='jane.doe@gmail.com'
          1234567890123456789

--output ='gmail.com'

select substring('jane.doe@gmail.com',CHARINDEX('@','jane.doe@gmail.com')+1, LEN ('jane.doe@gmail.com'))



select email ,
sUBSTRING(EMAIL,CHARINDEX('@',EMAIL)+1, LEN(email))
from empemail
--################################################

CREATE TABLE T2 
( ID INT , ENAME VARCHAR(10))

INSERT INTO T2 (ID, ENAME) VALUES 
(4, 'EMMA,LEE'),
(5, 'NOAH,KIM'),
(6, 'OLIVIA,LU'),
(7, 'LIAM,CHEN'),
(8, 'SOPHIA,RAJ'),
(9, 'MASON,YU'),
(10, 'AVA,SHAH')


select ID,ENAME  from T2
--Parsename 

select 'column1.column2.column3.column4'

select Parsename('column1.column2.column3.column4',4),
 Parsename('column1.column2.column3.column4',3),
  Parsename('column1.column2.column3.column4',2),
 Parsename('column1.column2.column3.column4',1)

 select Parsename(replace('column1,column2',',','.'),2)
, Parsename(replace('column1,column2',',','.'),1)

select ID,ENAME ,
concat(parsename (replace(ENAME,',','.'),2), '@email.com')as email
from T2

select 'column1,column2-column3;column4',
replace(
	replace(
		replace('column1,column2-column3;column4',',','.')
															,'-','.')
																	,';','.')
		
input =firstname.lastname 


select 'firstname.lastname ', 'firstname','lastname'
 select 'firstname.lastname',PARSENAME('firstname.lastname',2)
 ,PARSENAME('firstname.lastname',2)
 
 
 select 'firstname.lastname',PARSENAME('firstname.lastname',2)
 ,PARSENAME('firstname.lastname',2),
  concat(PARSENAME('firstname.lastname',2),'@gmail.com')


--#############################################################################
--Date and time Function 

select BusinessEntityID,BirthDate,HireDate
from HumanResources.Employee

--current system date time
select GETDATE()

select sysdatetime()

select BusinessEntityID,BirthDate,
YEAR(BirthDate) as Years,
month(BirthDate) as Months,
day(BirthDate) as Days

from HumanResources.Employee

--datename  

--select datename(date/time, DATETIME)
select  datename(Year,getdate())
select  datename(MONTH,getdate())
select  datename(DAY,getdate())
select  datename(DAYOFYEAR,getdate())
select  datename(WEEK,getdate())
select  datename(WEEKDAY,getdate())
select  datename(QUARTER,getdate())
select  datename(HOUR,getdate())
select  datename(MINUTE,getdate())
select  datename(SECOND,getdate())
select  datename(MILLISECOND,getdate())
select  datename(NANOSECOND,getdate())
select  datename(MICROSECOND,getdate())

--datepart

select  datepart(Year,getdate())
select  datepart(MONTH,getdate())
select  datepart(DAY,getdate())
select  datepart(DAYOFYEAR,getdate())
select  datepart(WEEK,getdate())
select  datepart(WEEKDAY,getdate())
select  datepart(QUARTER,getdate())
select  datepart(HOUR,getdate())
select  datepart(MINUTE,getdate())
select  datepart(SECOND,getdate())
select  datepart(MILLISECOND,getdate())
select  datepart(NANOSECOND,getdate())
select  datepart(MICROSECOND,getdate())


--DateDiff
	select BusinessEntityID,BirthDate,HireDate,
	datediff(YEAR,BirthDate,HireDate) as Years,
	datediff(MONTH,BirthDate,HireDate)as Months,
	datediff(DAY,BirthDate,HireDate)as days,
	datediff(WEEK,BirthDate,HireDate) as weeks,
	datediff(HOUR,BirthDate,HireDate)as hours,
	datediff(MINUTE,BirthDate,HireDate)as minutes
	from HumanResources.Employee
--############################################
--dateadd

	select BusinessEntityID,BirthDate,
	DATEADD(year, 10,BirthDate) ,
	DATEADD(MONTH, 10,BirthDate) ,
	DATEADD(DAY, 10,BirthDate)
	from HumanResources.Employee


	select BusinessEntityID,BirthDate,
	DATEADD(year,-20,BirthDate) ,
	DATEADD(MONTH, -100,BirthDate) ,
	DATEADD(DAY, -356,BirthDate)
	from HumanResources.Employee

--convert the time from one zone to another
 select GETDATE() as Est ,
 GETDATE() at time zone  'eastern standard time'at time zone   'central standard time' as IST
 --##################################
 --Conversion FUnction in SQl server.

--int into Char or varchar 
1001 ='1001'

 --Char or varchar  --> into numeric ( yes only if the data is numeric)
 --datetime into  --> Char or varchar(yes)

 
 select cast(1 as varchar) + 'A'
 
 select Convert(varchar,1) + 'A'

 select BusinessEntityID, firstname,
 cast(BusinessEntityID as varchar)+firstname as ID
 from Person.person
 
 
 select BusinessEntityID, firstname,
 convert(varchar,BusinessEntityID)+firstname as ID
 from Person.person 


 select GETDATE()

 
 select CONVERT(varchar, GETDATE(),1)
 select CONVERT(varchar, GETDATE(),4)
 select CONVERT(varchar, GETDATE(),5)
 select CONVERT(varchar, GETDATE(),6)
 select CONVERT(varchar, GETDATE(),11)
 select CONVERT(varchar, GETDATE(),21)
 select CONVERT(varchar, GETDATE(),33)
 select CONVERT(varchar, GETDATE(),35)
 select CONVERT(varchar, GETDATE(),104)

 select CONVERT(varchar, GETDATE(),8)
 select CONVERT(varchar, GETDATE(),14)
 select CONVERT(varchar, GETDATE(),24)
 select CONVERT(varchar, GETDATE(),108)

 select CONVERT(varchar, GETDATE(),0)
 select CONVERT(varchar, GETDATE(),13)
 select CONVERT(varchar, GETDATE(),20)
 select CONVERT(varchar, GETDATE(),21)
 select CONVERT(varchar, GETDATE(),27)
 select CONVERT(varchar, GETDATE(),127)
 --#################################
 --Format(expression , culture, currencyformat)

 select rate , 
 FORMAT(rate*62 , 'c', 'en-in'), 
 FORMAT(Rate*82 , 'c', 'en-us'), 
 FORMAT(rate , 'c', 'ba-ru'), 
 FORMAT(rate , 'c', 'ku-Arab-IQ')
 
 from  HumanResources.EmployeePayHistory
 
 select GETDATE()

 select GETDATE(),
 FORMAT(GETDATE(), 'MM ,dd-yyyy')

  select GETDATE(),
 FORMAT(GETDATE(), 'MMM ,dd-yyyy')

 
  select GETDATE(),
 FORMAT(GETDATE(), 'MMMM ,dd-yyyy')

  
  select GETDATE(),
 FORMAT(GETDATE(), 'ddd,dd-MMMM-yyyy')

  select GETDATE(),
 FORMAT(GETDATE(), 'dddd,dd-MMMM-yyyy')

 
  select '2024-05-30 23:40:16.420',
 FORMAT(cast('2024-05-30 23:40:16.420' as DATETIME), 'MMMM ,dd-yyyy')

  select GETDATE(),
 FORMAT(GETDATE(), 'MM/dd-yyyy')

 --###############################################################



















































































































































































































































































































































































































































































































































































