import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="postgres", user='postgres', password='postgres', host='localhost', port='5432'
)

# Setting auto commit false
conn.autocommit = False

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("DROP TABLE scott_emp")
cursor.execute("DROP TABLE scott_dept")

print("Table dropped... ")

# Closing the connection
conn.commit() # 안하면 자동 롤백
conn.close()
