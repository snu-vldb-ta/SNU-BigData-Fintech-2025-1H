import psycopg2
import pandas as pd

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#join query
cursor.execute('''SELECT * from scott_emp emp, scott_dept dept where emp.deptno = dept.deptno''')
result = cursor.fetchall();
print(result)

colnames = [desc[0] for desc in cursor.description]
df = pd.DataFrame(result, columns=colnames)

print(df)

conn.commit()
conn.close()
