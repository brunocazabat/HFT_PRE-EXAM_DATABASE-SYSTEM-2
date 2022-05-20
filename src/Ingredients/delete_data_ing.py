from tkinter import *
from tkinter import messagebox


# delete data from database and listbox
def delete_data_ing(self, list_box):
    query = list_box.get(ACTIVE)
    if query:
        ing_id = query[3]
        self.curs.execute("DELETE FROM Ingredients WHERE ingredient_id=(%s)", (ing_id,))
        self.conn.commit()
        list_box.delete(ACTIVE)
        messagebox.showinfo('Ingredients Deleted', 'The ingredient ' + query[3] + ' is deleted')
