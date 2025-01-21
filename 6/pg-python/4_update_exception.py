import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)

#Setting auto commit false
conn.autocommit = False

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing the query to update the records
sql = '''UPDATE scott_emp SET sal = sal + 1000 WHERE job = 'PRESIDENT' '''
try:
   # Execute the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()
except:
   # Rollback in case there is any error
   print("Roll back!")
   conn.rollback()

# Closing the connection
conn.commit()
conn.close()