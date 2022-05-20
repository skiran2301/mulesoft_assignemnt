import mysql.connector #importing mysql connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Kiran@2306',database='kirandb') #connecting to database
mycursor=mydb.cursor()
select_all="select * from movies" #query to display all the data from movies table
select_by_name="select movie_name from movies where actor_name='ram charan'" #query to display the movie name based on the actor name
# mycursor.execute(select_by_name)
mycursor.execute(select_all) 
#run any one query at a time

for movie in mycursor:
    print(movie)