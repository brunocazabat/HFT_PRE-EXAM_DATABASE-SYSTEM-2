import psycopg2
from tkinter import *
from tkinter import ttk
from src_piz import list_all_piz, delete_data_piz, enter_data_piz, show_data_piz, update_data_piz
from src_ing import list_all_ing, delete_data_ing, enter_data_ing, show_data_ing, update_data_ing
from src_utils import close_connection


class DatabaseProject:
    update_data_window = None
    data_show_window = None
    addData_Window = None

    def __init__(self, window):
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

        # configure window, buttons and Entry
        window.title('The Ultimate Pizza Selector')
        window.geometry('450x450')
        style = ttk.Style()
        style.configure("TButton", font="Serif 10", padding=10)
        style.configure("TEntry", font="Serif 10", padding=10)
        bottomFrame = Frame(window)
        bottomFrame.pack(side=BOTTOM)

        ttk.Label(window, text="Pizzas List").pack()
        self.list_box = Listbox(window, selectmode=EXTENDED, width=65)
        self.list_box.pack()
        list_all_piz.list_all_piz(self)

        self.Pizzas_button = ttk.Button(window, text='Add a pizza', command=lambda: enter_data_piz.enter_data_piz(self)).pack(side=LEFT)
        self.show_button = ttk.Button(window, text='Show pizza details', command=lambda: show_data_piz.show_data_piz(self)).pack(side=LEFT)
        self.delete_button = ttk.Button(window, text='Delete pizza', command=lambda: delete_data_piz.delete_data_piz(self)).pack(side=RIGHT)
        self.update_button = ttk.Button(window, text='Update pizza list', command=lambda: update_data_piz.update_data_piz(self)).pack(side=RIGHT)
        ttk.Button(bottomFrame, text='Close', command=lambda: close_connection.close_connection(self, window)).pack()


if __name__ == '__main__':
    root = Tk()
    data = DatabaseProject(root)
    root.mainloop()
