from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL.Image import Resampling


# add a photo to your pizza recipe or ingredient
def add_photo(self, window):
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("png files", "*.png"), ("all files", "*.*")))
    self.photo_label['text'] = filename
    self.image = Image.open(self.photo_label['text'].rstrip())
    resized = self.image.resize((200, 200), Resampling.LANCZOS)
    self.photo = ImageTk.PhotoImage(resized)
    label_image = Label(window, image=self.photo)
    label_image.grid(row=0, column=1)
