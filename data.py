import psycopg2

connection = psycopg2.connect(
    host='localhost',
    dbname='My First',
    user='postgres',
    password='BabyLord22',
    port=5432
)

cursor = connection.cursor()

create_table = '''

    CREATE TABLE IF NOT EXISTS students (

        id SERIAL PRIMARY KEY,

        name VARCHAR(100),

        age INTEGER,

        email VARCHAR(100)

    )

'''

cursor.execute(create_table)

connection.commit()





