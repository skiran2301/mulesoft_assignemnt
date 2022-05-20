import mysql.connector #importing mysql connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Kiran@2306') #connecting to database
mycursor=mydb.cursor()  #creating cursor object 
mycursor.execute("create database kirandb")  #creating database named kirandb







# mycursor.execute("insert into movies values('PUSHPA','ALLU ARJUN','RASHMIKS','2021','SUKUMAR');")
# mycursor.execute("insert into movies values('BAHUBALI','PRABHAS','ANUSHKS','2017','RAJAMOULI');")
# mycursor.execute("insert into movies values('VVR','RAM CHARAN','KIARA','2019','BOYAPATI');")
# # mycursor.execute("")
# # mycursor.execute("")
# # mycursor.execute("select * from movies;") #executing a query to display all the rows of movies table

# # mycursor.execute("select movie_name from movies where lead_actor='YASH';") #query to display movie name in which lead actor is YASH

# result=mycursor.fetchall() #fetching all the data from myscursor and storing in result variable
# for i in result:   #using for loop to fetch the data row by row
#     print(i)  