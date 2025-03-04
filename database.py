import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='7799')

if conn.is_connected():
    print('connection estlablished')
print(conn)

#
#mycursor=conn.cursor()
#mycursor.execute('create database webgui')
#print(mycursor)





import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='7799',database='webgui')

mycursor=conn.cursor()





mycursor.execute('CREATE TABLE registration (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),course VARCHAR(255),fee DECIMAL(10, 2))')
#values = (studentname, coursename, fee)
mycursor.execute('show tables')

for x in mycursor:
    print(x)




