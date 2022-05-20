from tkinter import *
from tkinter import messagebox


# delete data from database and listbox
def delete_data_piz(self, list_box):
    query = list_box.get(ACTIVE)
    if query:
        piz_id = query[3]
        self.curs.execute("DELETE FROM Pizzas WHERE pizza_id=(%s)", (piz_id,))
        self.conn.commit()
        list_box.delete(ACTIVE)
        messagebox.showinfo('Pizza Deleted', 'The pizza ' + query[3] + ' is deleted')
