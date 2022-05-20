from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL.Image import Resampling


# show all data in database
def show_data_piz(self, list_box):
    self.data_show_window = Toplevel()
    self.data_show_window.title('Pizza Details')
    frame = Frame(self.data_show_window, bd=2, relief=SUNKEN)
    frame.grid()

    query = list_box.get(ACTIVE)
    if not query:
        self.data_show_window.destroy()
    if query:
        piz_id = query[3]
        self.curs.execute("SELECT * FROM Pizzas WHERE pizza_id=(%s)", (piz_id,))
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
