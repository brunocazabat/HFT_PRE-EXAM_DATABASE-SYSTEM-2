from tkinter import *
from tkinter import messagebox


# delete data from database and listbox
def delete_data_ing(self):
    query = self.list_box.get(ACTIVE)
    if query:
        id = query[3]
        self.curs.execute("DELETE FROM ingredients WHERE ingredient_id=(%s)", (id,))
        self.conn.commit()
        self.list_box.delete(ACTIVE)
        messagebox.showinfo('Ingredients Deleted', 'The ingredient ' + query[3] + ' is deleted')
