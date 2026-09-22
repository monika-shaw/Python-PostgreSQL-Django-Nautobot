import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="company_db",
    user="postgres",
    password="Monika12!@"
)

print("Database connected successfully!")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print(rows)

cursor.close()
connection.close()