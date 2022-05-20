from tkinter import *
from tkinter import ttk
from src.Pizzas import show_data_piz, update_data_piz, delete_data_piz, enter_data_piz, list_all_piz


# generate all left side of the UI
def pizzas_left_side(self):
    piz_lbl = ttk.Label(self, text="Pizzas List")
    piz_lbl.grid(row=0, column=0, padx=5)
    list_box_piz = Listbox(self, selectmode=EXTENDED, width=50)
    list_box_piz.grid(row=0, column=0, columnspan=5, rowspan=4, padx=5)
    list_all_piz.list_all_piz(self, list_box_piz)

    add_piz_button = ttk.Button(self, text='Add a pizza', command=lambda: enter_data_piz.enter_data_piz(self, list_box_piz))
    add_piz_button.grid(row=6, column=0, pady=(20, 0))
    show_piz_button = ttk.Button(self, text='Show pizza details', command=lambda: show_data_piz.show_data_piz(self, list_box_piz))
    show_piz_button.grid(row=6, column=1, pady=(20, 0))
    update_piz_button = ttk.Button(self, text='Update pizza information', command=lambda: update_data_piz.update_data_piz(self, list_box_piz))
    update_piz_button.grid(row=6, column=2, pady=(20, 0))
    delete_piz_button = ttk.Button(self, text='Delete pizza', command=lambda: delete_data_piz.delete_data_piz(self, list_box_piz))
    delete_piz_button.grid(row=6, column=3, pady=(20, 0))
