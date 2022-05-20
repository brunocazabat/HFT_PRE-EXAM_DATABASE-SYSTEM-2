import psycopg2
from tkinter import *
from src.UserInterface import pizzas_left_side, ingre_right_side, close_and_style
from src.UserInterface import column_row_gen


class MainDatabaseProject(Frame):
    update_data_self = None
    data_show_self = None
    addData_self = None

    def __init__(self):
        super().__init__()
        # connect database
        try:
            self.conn = psycopg2.connect("host='localhost' dbname='dbpizzaprojecthft' user='bruno' password='admin'")
            print("Successfully connected to the Pizza PostgreSQL DataBase.")
        except psycopg2.ProgrammingError:
            print("I am unable to connect to the database")
        self.curs = self.conn.cursor()
        try:
            pass
        except psycopg2.ProgrammingError:
            with self.conn as cursor:
                cursor.execute(open('pizza_schema.sql', 'r').read())
        self.initui()

    def initui(self):
        # configure self, buttons and Entry
        self.master.title('The Ultimate Pizza Selector')

        # generate all UI
        column_row_gen.column_row_gen(self)
        pizzas_left_side.pizzas_left_side(self)
        ingre_right_side.ingre_right_side(self)
        close_and_style.close_and_style(self)

        self.pack()


def main():
    root = Tk()
    app = MainDatabaseProject()
    root.mainloop()


if __name__ == '__main__':
    main()
