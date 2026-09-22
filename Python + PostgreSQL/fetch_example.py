import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="company_db",
    user="postgres",
    password="Monika12!@"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")

employees = cursor.fetchall()

for employee in employees:
    print(employee)

cursor.close()
connection.close()