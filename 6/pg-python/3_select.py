import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)

#Setting auto commit false
conn.autocommit = False

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from scott_emp''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching all row from the table
result = cursor.fetchall();
print(result)

#join query
cursor.execute('''SELECT * from scott_emp emp, scott_dept dept where emp.deptno = dept.deptno''')
result = cursor.fetchall();
print(result)


conn.commit()
conn.close()