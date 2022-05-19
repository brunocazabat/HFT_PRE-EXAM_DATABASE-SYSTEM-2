from tkinter import *


# list all data in listbox
def list_all_ing(self):
    self.curs.execute("SELECT * FROM ingredients")
    self.list_box.delete(0, END)
    rows = self.curs.fetchall()
    for row in rows:
        self.list_box.insert(0, 'N° ' + str(row[0]) + ': ' + row[1])
