import psycopg2
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from PIL.Image import Resampling
from src_piz import list_all_piz
from src_ing import list_all_ing


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
        self.list_all_piz()

        self.Pizzas_button = ttk.Button(window, text='Add a pizza', command=lambda: self.enter_data()).pack(side=LEFT)
        self.show_button = ttk.Button(window, text='Show pizza details', command=lambda: self.show_data()).pack(side=LEFT)
        self.delete_button = ttk.Button(window, text='Delete pizza', command=lambda: self.delete_data()).pack(side=RIGHT)
        self.update_button = ttk.Button(window, text='Update pizza list', command=lambda: self.update()).pack(side=RIGHT)
        ttk.Button(bottomFrame, text='Close', command=lambda: self.close_connection(window)).pack()

    # list all data in listbox
    def list_all_piz(self):
        self.curs.execute("SELECT * FROM Pizzas")
        self.list_box.delete(0, END)
        rows = self.curs.fetchall()
        for row in rows:
            self.list_box.insert(0, str(row[0]) + ': ' + row[1] + ' ' + row[2] + ' ' + row[3])

    # delete data from database and listbox
    def delete_data(self):
        query = self.list_box.get(ACTIVE)
        if query:
            id = query[0]
            self.curs.execute("DELETE FROM Pizzas WHERE pizza_id=(%s)", (id,))
            self.conn.commit()
            self.list_box.delete(ACTIVE)
            messagebox.showinfo('Pizza Deleted', 'The pizza ' + query[1] + ' is updated')

    # enter data on entry boxes
    def enter_data(self):
        self.addData_Window = Toplevel()
        # self.addData_Window.geometry('800x400')
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
                                       command=lambda: self.add_photo(self.addData_Window)).grid(row=9, column=1)
        self.photo_label = Label(self.addData_Window)
        self.photo_label.grid(row=10, column=1)

        self.add_button = ttk.Button(self.addData_Window, text='Add Data', command=lambda: self.add_data()).grid(row=11,
                                                                                                                 column=1)
        ttk.Button(self.addData_Window, text='Close', command=lambda: self.addData_Window.destroy()).grid(row=12,
                                                                                                          column=1)

    # data add on the listbox and also on database
    def add_data(self):
        try:
            parameters = (self.id.get(), self.pizza_name.get(), self.first_ingredient.get(), self.second_ingredient.get(),
                          self.third_ingredient.get(), self.fourth_ingredient.get(), self.fifth_ingredient.get(), self.sixth_ingredient.get(),
                          self.photo_label['text'].rstrip())
            self.curs.execute("INSERT INTO Pizzas VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", parameters)
            self.conn.commit()
            parameters = (self.id, self.pizza_name, self.first_ingredient, self.second_ingredient, self.third_ingredient, self.fourth_ingredient,
                          self.fifth_ingredient, self.sixth_ingredient)
            for parameter in parameters:
                parameter.delete(0, END)
                parameter.insert(0, '')
            messagebox.showinfo('Pizza Added', 'Your pizza recipe has been successfully added')
            self.list_all_piz()
        except psycopg2.DataError as e:
            if self.conn:
                self.conn.rollback()
            messagebox.showerror('Error', 'Please enter correctly all ingredients')

    def show_data(self):
        self.data_show_window = Toplevel()
        # self.data_show_window.geometry('400x400')
        self.data_show_window.title('Pizza Details')
        frame = Frame(self.data_show_window, bd=2, relief=SUNKEN)
        frame.grid()

        query = self.list_box.get(ACTIVE)
        if not query:
            self.data_show_window.destroy()
        if query:
            id = query[0]
            self.curs.execute("SELECT * FROM Pizzas WHERE pizza_id=(%s)", (id,))
            rows = self.curs.fetchall()
            for data in rows:
                if data[8]:
                    self.image = Image.open(data[8].rstrip())
                    resized = self.image.resize((200, 200), Resampling.LANCZOS)
                    self.photo = ImageTk.PhotoImage(resized)
                    label_image = Label(self.data_show_window, image=self.photo)
                    label_image.grid(row=0, column=1)

                ttk.Label(frame, text='Pizza ID: ').grid(row=1, column=0)
                ttk.Label(frame, text=data[0]).grid(row=1, column=2)

                ttk.Label(frame, text='Pizza Name: ').grid(row=2, column=0)
                ttk.Label(frame, text=data[1]).grid(row=2, column=2)

                ttk.Label(frame, text='First Ingredient: ').grid(row=3, column=0)
                ttk.Label(frame, text=data[2]).grid(row=3, column=2)

                ttk.Label(frame, text='Second Ingredient: ').grid(row=4, column=0)
                ttk.Label(frame, text=data[3]).grid(row=4, column=2)

                ttk.Label(frame, text='Third Ingredient: ').grid(row=5, column=0)
                ttk.Label(frame, text=data[4]).grid(row=5, column=2)

                ttk.Label(frame, text='Fourth Ingredient: ').grid(row=6, column=0)
                ttk.Label(frame, text=data[5]).grid(row=6, column=2)

                ttk.Label(frame, text='Fifth Ingredient: ').grid(row=7, column=0)
                ttk.Label(frame, text=data[6]).grid(row=7, column=2)

                ttk.Label(frame, text='Sixth Ingredient: ').grid(row=8, column=0)
                ttk.Label(frame, text=data[7]).grid(row=8, column=2)

                ttk.Button(frame, text='Close', command=lambda: self.data_show_window.destroy()).grid(row=9, column=1)

    def update(self):
        self.update_data_window = Toplevel()
        self.update_data_window.title('Update Pizza informations')
        frame = Frame(self.update_data_window, bd=2, relief=SUNKEN)
        frame.grid()
        query = self.list_box.get(ACTIVE)
        if not query:
            self.update_data_window.destroy()
        self.id = query[0]
        self.curs.execute("SELECT * FROM Pizzas WHERE pizza_id=(%s)", (self.id,))
        rows = self.curs.fetchall()
        for data in rows:
            if data[8]:
                self.image = Image.open(data[8].rstrip())
                resized = self.image.resize((200, 200), Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(resized)
                label_image = Label(self.update_data_window, image=self.photo)
                label_image.grid(row=0, column=1)

            photo_button = ttk.Button(self.update_data_window, text='Browse',
                                      command=lambda: self.add_photo(self.update_data_window)).grid(row=1, column=1)

            ttk.Label(frame, text='Pizza ID: ').grid(row=0, column=0)
            self.id1 = ttk.Label(frame)
            self.id1.grid(row=0, column=1)
            self.id1['text'] = data[0]

            ttk.Label(frame, text='Pizza Name: ').grid(row=1, column=0)
            self.pizza_name1 = ttk.Entry(frame)
            self.pizza_name1.grid(row=1, column=1)
            self.pizza_name1.insert(0, data[1])

            ttk.Label(frame, text='First Ingredient: ').grid(row=2, column=0)
            self.first_ingredient1 = ttk.Entry(frame)
            self.first_ingredient1.grid(row=2, column=1)
            self.first_ingredient1.insert(0, data[2])

            ttk.Label(frame, text='Second Ingredient: ').grid(row=3, column=0)
            self.second_ingredient1 = ttk.Entry(frame)
            self.second_ingredient1.grid(row=3, column=1)
            self.second_ingredient1.insert(0, data[3])

            ttk.Label(frame, text='Third Ingredient: ').grid(row=4, column=0)
            self.third_ingredient1 = ttk.Entry(frame)
            self.third_ingredient1.grid(row=4, column=1)
            self.third_ingredient1.insert(0, data[4])

            ttk.Label(frame, text='Fourth Ingredient: ').grid(row=5, column=0)
            self.fourth_ingredient1 = ttk.Entry(frame)
            self.fourth_ingredient1.grid(row=5, column=1)
            self.fourth_ingredient1.insert(0, data[5])

            ttk.Label(frame, text='Fifth Ingredient: ').grid(row=6, column=0)
            self.fifth_ingredient1 = ttk.Entry(frame)
            self.fifth_ingredient1.grid(row=6, column=1)
            self.fifth_ingredient1.insert(0, data[6])

            ttk.Label(frame, text='Sixth Ingredient: ').grid(row=7, column=0)
            self.sixth_ingredient1 = ttk.Entry(frame)
            self.sixth_ingredient1.grid(row=7, column=1)
            self.sixth_ingredient1.insert(0, data[7])

            ttk.Label(self.update_data_window, text='Upload Photo').grid(row=8, column=0)
            self.photo_label = ttk.Label(self.update_data_window, text=data[8])
            self.photo_label.grid(row=8, column=1)

        self.update_button = ttk.Button(frame, text='Update Data', command=lambda: self.update_data()).grid(row=9, column=1)
        ttk.Button(self.update_data_window, text='Close', command=lambda: self.update_data_window.destroy()).grid(row=10, column=1)

    def update_data(self):
        update_values = (self.pizza_name1.get(), self.first_ingredient1.get(), self.second_ingredient1.get(),
                         self.third_ingredient1.get(), self.fourth_ingredient1.get(), self.fifth_ingredient1.get(), self.sixth_ingredient1.get(),
                         self.photo_label['text'].rstrip(), self.id)
        self.curs.execute("UPDATE Pizzas SET pizza_name=(%s), first_ingredient=(%s), second_ingredient=(%s), "
                          "third_ingredient=(%s), fourth_ingredient=(%s), "
                          "fifth_ingredient=(%s), sixth_ingredient=(%s), photo=(%s) WHERE pizza_id=(%s)", update_values)
        self.conn.commit()
        self.list_all_piz()
        self.curs.execute("SELECT * FROM Pizzas WHERE pizza_id=(%s)", (self.id,))
        rows = self.curs.fetchall()
        for data in rows:
            self.id1['text'] = ''
            self.id1['text'] = data[0]
            self.pizza_name1.delete(0, END)
            self.pizza_name1.insert(0, data[1])
            self.first_ingredient1.delete(0, END)
            self.first_ingredient1.insert(0, data[2])
            self.second_ingredient1.delete(0, END)
            self.second_ingredient1.insert(0, data[3])
            self.third_ingredient1.delete(0, END)
            self.third_ingredient1.insert(0, data[4])
            self.fourth_ingredient1.delete(0, END)
            self.fourth_ingredient1.insert(0, data[5])
            self.fifth_ingredient1.delete(0, END)
            self.fifth_ingredient1.insert(0, data[6])
            self.sixth_ingredient1.delete(0, END)
            self.sixth_ingredient1.insert(0, data[7])

            self.image = Image.open(data[8].rstrip())
            resized = self.image.resize((200, 200), Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(resized)

            label_image = Label(self.update_data_window, image=self.photo)
            label_image.grid(row=0, column=1)

            messagebox.showinfo('Pizzas Updated', 'The pizza ' + self.pizza_name1.get() + ' is updated')

    # close database connection
    def close_connection(self, window):
        self.curs.close()
        del self.curs
        self.conn.close()  # <--- Close the connection
        if self.update_data_window or self.data_show_window or self.addData_Window:
            self.update_data_window.destroy()
            self.data_show_window.destroy()
            self.addData_Window.destroy()
        window.destroy()

    def add_photo(self, window):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
        self.photo_label['text'] = filename

        self.image = Image.open(self.photo_label['text'].rstrip())
        resized = self.image.resize((200, 200), Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized)
        label_image = Label(window, image=self.photo)
        label_image.grid(row=0, column=1)


if __name__ == '__main__':
    root = Tk()
    data = DatabaseProject(root)
    root.mainloop()
