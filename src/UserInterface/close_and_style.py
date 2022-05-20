from tkinter import ttk
from src.Utils import close_connection


# add additional style rules and add the close button
def close_and_style(self):
    style = ttk.Style()
    style.configure("TButton", font="Serif 10", padding=10)
    style.configure("TEntry", font="Serif 10", padding=10)

    close_button = ttk.Button(self, text='Close', command=lambda: close_connection.close_connection(self))
    close_button.grid(row=7, column=4, padx=5, pady=(20, 0))
