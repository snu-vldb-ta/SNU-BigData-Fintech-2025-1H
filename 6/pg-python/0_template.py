import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)

cursor = conn.cursor()

#Your SQL here
sql ='''

)'''
cursor.execute(sql)
print("SQL executed successfully........")

#End connection
conn.commit()
conn.close()