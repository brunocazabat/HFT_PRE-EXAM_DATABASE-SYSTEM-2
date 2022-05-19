from tkinter import *
from tkinter import messagebox


# delete data from database and listbox
def delete_data_piz(self):
    query = self.list_box.get(ACTIVE)
    if query:
        id = query[3]
        self.curs.execute("DELETE FROM Pizzas WHERE pizza_id=(%s)", (id,))
        self.conn.commit()
        self.list_box.delete(ACTIVE)
        messagebox.showinfo('Pizza Deleted', 'The pizza ' + query[3] + ' is deleted')
