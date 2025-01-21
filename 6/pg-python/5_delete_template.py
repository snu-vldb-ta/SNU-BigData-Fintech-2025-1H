import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)

#Setting auto commit false
conn.autocommit = False

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing the query to delete records
sql = "DELETE FROM scott_emp WHERE job = '%s'" % ('PRESIDENT')

try:
   # Execute the SQL command
   cursor.execute(sql)

   # Commit your changes in the database
   conn.commit()
except:
   print("Roll back!")
   # Roll back in case there is any error
   conn.rollback()

# Closing the connection
conn.commit()
conn.close()