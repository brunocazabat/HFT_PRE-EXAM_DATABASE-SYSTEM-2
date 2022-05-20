from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL.Image import Resampling


# show all data in database
def show_data_ing(self, list_box):
    self.data_show_window = Toplevel()
    self.data_show_window.title('Ingredient Details')
    frame = Frame(self.data_show_window, bd=2, relief=SUNKEN)
    frame.grid()

    query = list_box.get(ACTIVE)
    if not query:
        self.data_show_window.destroy()
    if query:
        ing_id = query[3]
        self.curs.execute("SELECT * FROM ingredients WHERE ingredient_id=(%s)", (ing_id,))
        rows = self.curs.fetchall()
        for data in rows:
            if data[2]:
                self.image = Image.open(data[2].rstrip())
                resized = self.image.resize((200, 200), Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(resized)
                label_image = Label(self.data_show_window, image=self.photo)
                label_image.grid(row=0, column=1)

            ttk.Label(frame, text='Ingredient ID: ').grid(row=1, column=0)
            ttk.Label(frame, text=data[0]).grid(row=1, column=2)

            ttk.Label(frame, text='Ingredient Name: ').grid(row=2, column=0)
            ttk.Label(frame, text=data[1]).grid(row=2, column=2)

            ttk.Button(frame, text='Close', command=lambda: self.data_show_window.destroy()).grid(row=3, column=1)
