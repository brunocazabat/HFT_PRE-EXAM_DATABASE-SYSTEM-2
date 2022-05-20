from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from PIL.Image import Resampling
from src_piz import list_all_piz
from src_utils import add_photo


# update all data in database
def update_piz(self):
    update_values = (self.pizza_name1.get(), self.first_ingredient1.get(), self.second_ingredient1.get(),
                     self.third_ingredient1.get(), self.fourth_ingredient1.get(), self.fifth_ingredient1.get(),
                     self.sixth_ingredient1.get(),
                     self.photo_label['text'].rstrip(), self.id)
    self.curs.execute("UPDATE Pizzas SET pizza_name=(%s), first_ingredient=(%s), second_ingredient=(%s), "
                      "third_ingredient=(%s), fourth_ingredient=(%s), "
                      "fifth_ingredient=(%s), sixth_ingredient=(%s), photo=(%s) WHERE pizza_id=(%s)", update_values)
    self.conn.commit()
    list_all_piz.list_all_piz(self)
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

        messagebox.showinfo('Pizza Updated', 'The pizza ' + self.pizza_name1.get() + ' is updated')


# update all data in database
def update_data_piz(self):
    self.update_data_window = Toplevel()
    self.update_data_window.title('Update Pizza information')
    frame = Frame(self.update_data_window, bd=2, relief=SUNKEN)
    frame.grid()
    query = self.list_box.get(ACTIVE)
    if not query:
        self.update_data_window.destroy()
    self.id = query[3]
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
                                  command=lambda: add_photo.add_photo(self, self.update_data_window)).grid(row=1,
                                                                                                           column=1)

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

    self.update_button = ttk.Button(frame, text='Update Data', command=lambda: update_piz(self)).grid(row=9,
                                                                                                      column=1)
    ttk.Button(self.update_data_window, text='Close', command=lambda: self.update_data_window.destroy()).grid(row=10,
                                                                                                              column=1)
