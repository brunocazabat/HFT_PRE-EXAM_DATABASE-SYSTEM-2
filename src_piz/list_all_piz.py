from tkinter import *


# list all data in listbox
def list_all_piz(self, list_box):
    self.curs.execute("SELECT * FROM Pizzas")
    list_box.delete(0, END)
    rows = self.curs.fetchall()
    for row in rows:
        list_box.insert(0, 'N° ' + str(row[0]) + ' : ' + row[1] + ' pizza')
