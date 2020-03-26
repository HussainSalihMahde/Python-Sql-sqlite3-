import sqlite3 as s

#TODO add new file name with .db and connect to it or your database file
sql = s.connect('login.db')
#TODO to give ability to control
c = sql.cursor()

#TODO to create the table and its info
# c.execute(''' CREATE TABLE employee (
#               id primary key,
#               name varchar(20),
#               password int(1)
#          ) ''')

name = input("Enter Your Name : ")
pas = int(input("Enter Your Password : "))

# for execute some sql command
c.execute("INSERT INTO employee VALUES(1,?,?)",(name,pas))

#to confirm the command
sql.commit()

#close the connection
sql.close()
