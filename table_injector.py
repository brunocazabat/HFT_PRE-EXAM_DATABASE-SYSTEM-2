import psycopg2

try:
    conn = psycopg2.connect("host='localhost' port = '5432' dbname='dbpizzaprojecthft' user='bruno' password='admin'")
except:
    print("I am unable to connect to the database")

curs = conn.cursor()

try:
    curs.execute(open('pizza_schema.sql', 'r').read())
except:
    print("I can't drop our test database!")

conn.close()
curs.close()
