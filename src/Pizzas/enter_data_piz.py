import psycopg2
from tkinter import *
from tkinter import ttk, messagebox
from src.Pizzas import list_all_piz
from src.Utils import add_photo


# enter data on entry boxes
def enter_data_piz(self, list_box):
    self.addData_Window = Toplevel()
    self.addData_Window.title('Add Pizzas Data')

    self.curs.execute("SELECT * FROM Pizzas")
    value = str(len(self.curs.fetchall()) + 1)

    ttk.Label(self.addData_Window, text='Pizza ID: ').grid(row=1, column=0)
    self.id = ttk.Entry(self.addData_Window)
    self.id.grid(row=1, column=1)
    self.id.insert(0, value)

    ttk.Label(self.addData_Window, text='Pizza Name: ').grid(row=2, column=0)
    self.pizza_name = ttk.Entry(self.addData_Window)
    self.pizza_name.grid(row=2, column=1)

    ttk.Label(self.addData_Window, text='First Ingredient: ').grid(row=3, column=0)
    self.first_ingredient = ttk.Entry(self.addData_Window)
    self.first_ingredient.grid(row=3, column=1)

    ttk.Label(self.addData_Window, text='Second Ingredient: ').grid(row=4, column=0)
    self.second_ingredient = ttk.Entry(self.addData_Window)
    self.second_ingredient.grid(row=4, column=1)

    ttk.Label(self.addData_Window, text='Third Ingredient: ').grid(row=5, column=0)
    self.third_ingredient = ttk.Entry(self.addData_Window)
    self.third_ingredient.grid(row=5, column=1)

    ttk.Label(self.addData_Window, text='Fourth Ingredient: ').grid(row=6, column=0)
    self.fourth_ingredient = ttk.Entry(self.addData_Window)
    self.fourth_ingredient.grid(row=6, column=1)

    ttk.Label(self.addData_Window, text='Fifth Ingredient: ').grid(row=7, column=0)
    self.fifth_ingredient = ttk.Entry(self.addData_Window)
    self.fifth_ingredient.grid(row=7, column=1)

    ttk.Label(self.addData_Window, text='Sixth Ingredient: ').grid(row=8, column=0)
    self.sixth_ingredient = ttk.Entry(self.addData_Window)
    self.sixth_ingredient.grid(row=8, column=1)
    ttk.Label(self.addData_Window, text='Upload Pizza Photo').grid(row=9, column=0)
    self.photo_button = ttk.Button(self.addData_Window, text='Browse',
                                   command=lambda: add_photo.add_photo(self, self.addData_Window)).grid(row=9, column=1)
    self.photo_label = Label(self.addData_Window)
    self.photo_label.grid(row=10, column=1)

    self.add_button = ttk.Button(self.addData_Window, text='Add Data',
                                 command=lambda: add_data_piz(self, list_box)).grid(row=11, column=1)
    ttk.Button(self.addData_Window, text='Close', command=lambda: self.addData_Window.destroy()).grid(row=12, column=1)


# data add on the listbox and also on database
def add_data_piz(self, list_box):
    try:
        parameters = (self.id.get(), self.pizza_name.get(), self.first_ingredient.get(), self.second_ingredient.get(),
                      self.third_ingredient.get(), self.fourth_ingredient.get(), self.fifth_ingredient.get(),
                      self.sixth_ingredient.get(), self.photo_label['text'].rstrip())
        self.curs.execute("INSERT INTO Pizzas VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", parameters)
        self.conn.commit()
        parameters = (self.id, self.pizza_name, self.first_ingredient, self.second_ingredient, self.third_ingredient,
                      self.fourth_ingredient, self.fifth_ingredient, self.sixth_ingredient)
        for parameter in parameters:
            parameter.delete(0, END)
            parameter.insert(0, '')
        messagebox.showinfo('Pizza Added', 'Your pizza recipe has been successfully added')
        list_all_piz.list_all_piz(self, list_box)
    except psycopg2.DataError as e:
        if self.conn:
            self.conn.rollback()
        messagebox.showerror('Error', 'Please enter correctly all Ingredients')
