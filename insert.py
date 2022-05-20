import mysql.connector #importing mysql connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Kiran@2306',database='kirandb') #connecting to database
mycursor=mydb.cursor()
sql_query="insert into movies values(%s,%s,%s,%s,%s)"  #writing a sql query for insertion
#creating a list of tuple with movie details
movies_list=[('PUSHPA','ALLU ARJUN','RASHMIKS','SUKUMAR','2021'),('BAHUBALI','PRABHAS','ANUSHKA','RAJAMOULI','2017'),('VVR','RAM CHARAN','KIARA','BOYAPATI','2019'),]
mycursor.executemany(sql_query,movies_list) #executemany to execute all the insertions together
mydb.commit()