import mysql.connector #importing mysql connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Kiran',database='kirandb') #connecting to database
mycursor=mydb.cursor()  #creating cursor object 
#creating movies table 
mycursor.execute("create table movies(movie_name varchar(20), actor_name varchar(15), actress_name varchar(15), director_name varchar(15), release_year varchar(4));")
