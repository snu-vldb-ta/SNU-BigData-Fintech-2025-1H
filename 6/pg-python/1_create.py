import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)

cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS scott_EMP")
cursor.execute("DROP TABLE IF EXISTS scott_DEPT")

#Creating table as per requirement
sql ='''CREATE TABLE scott_DEPT
(
    DEPTNO numeric(2) not null CONSTRAINT PK_DEPT PRIMARY KEY,
    DNAME VARCHAR(14) ,
    LOC VARCHAR(13) 
);

CREATE TABLE scott_EMP
(
    EMPNO numeric(4) not null CONSTRAINT PK_EMP PRIMARY KEY,
    ENAME VARCHAR(10),
    JOB VARCHAR(9),
    MGR numeric(4),
    HIREDATE DATE,
    SAL numeric(7,2),
    COMM numeric(7,2),
    DEPTNO numeric(2) CONSTRAINT FK_DEPTNO REFERENCES scott_DEPT
);

'''
cursor.execute(sql)
print("Table created successfully........")

conn.commit()
conn.close()