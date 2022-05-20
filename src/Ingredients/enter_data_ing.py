import psycopg2
from tkinter import *
from tkinter import ttk, messagebox
from src.Ingredients import list_all_ing
from src.Utils import add_photo


# enter data on entry boxes
def enter_data_ing(self, list_box):
    self.addData_Window = Toplevel()
    self.addData_Window.title('Add Ingredients Data')

    self.curs.execute("SELECT * FROM Ingredients")
    value = str(len(self.curs.fetchall()) + 1)

    ttk.Label(self.addData_Window, text='Ingredient ID: ').grid(row=1, column=0)
    self.id = ttk.Entry(self.addData_Window)
    self.id.grid(row=1, column=1)
    self.id.insert(0, value)

    ttk.Label(self.addData_Window, text='Ingredient Name: ').grid(row=2, column=0)
    self.ingredient_name = ttk.Entry(self.addData_Window)
    self.ingredient_name.grid(row=2, column=1)

    ttk.Label(self.addData_Window, text='Upload Ingredient Photo').grid(row=3, column=0)
    self.photo_button = ttk.Button(self.addData_Window, text='Browse',
                                   command=lambda: add_photo.add_photo(self, self.addData_Window)).grid(row=3, column=1)
    self.photo_label = Label(self.addData_Window)
    self.photo_label.grid(row=4, column=1)

    self.add_button = ttk.Button(self.addData_Window, text='Add Data',
                                 command=lambda: add_data_ing(self, list_box)).grid(row=5, column=1)
    ttk.Button(self.addData_Window, text='Close', command=lambda: self.addData_Window.destroy()).grid(row=6, column=1)


# data add on the listbox and also on database
def add_data_ing(self, list_box):
    try:
        parameters = (self.id.get(), self.ingredient_name.get(), self.photo_label['text'].rstrip())
        self.curs.execute("INSERT INTO Ingredients VALUES (%s, %s, %s)", parameters)
        self.conn.commit()
        parameters = (self.id, self.ingredient_name)
        for parameter in parameters:
            parameter.delete(0, END)
            parameter.insert(0, '')
        messagebox.showinfo('Ingredient Added', 'Your ingredient has been successfully added')
        list_all_ing.list_all_ing(self, list_box)
    except psycopg2.DataError as e:
        if self.conn:
            self.conn.rollback()
        messagebox.showerror('Error', 'Please enter correctly all informations')
