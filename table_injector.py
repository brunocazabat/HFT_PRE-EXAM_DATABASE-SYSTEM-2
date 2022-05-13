import psycopg2

try:
    conn = psycopg2.connect("host='localhost' port = '5432' dbname='dbpizzaprojecthft' user='bruno' password='admin'")
    print("Successfully connected to the Pizza PostgreSQL DataBase.")
except:
    print("I am unable to connect to the database")

curs = conn.cursor()

try:
    curs.execute(open('pizza_schema.sql', 'r').read())
    print("Successfully Injected basic Pizzas Recipes into the PostgreSQL DataBase.")
except:
    print("I can't drop our Pizza database! Maybe Pizzas are already here ..")

conn.close()
print("Closing Table_injector.py")
curs.close()
