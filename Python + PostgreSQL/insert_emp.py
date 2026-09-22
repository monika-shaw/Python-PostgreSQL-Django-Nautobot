import psycopg

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="company_db",
    user="postgres",
    password="Monika12!@"
)

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO employees
    (name, age, department, salary)
    VALUES ('Neha', 26, 'Finance', 55000)
""")

connection.commit()

print("Employee inserted successfully")

cursor.close()
connection.close()