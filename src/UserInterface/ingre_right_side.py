from tkinter import *
from tkinter import ttk
from src.Ingredients import list_all_ing, delete_data_ing, enter_data_ing, show_data_ing
from src.Ingredients import update_data_ing


# generate all right side of the UI
def ingre_right_side(self):
    ing_lbl = ttk.Label(self, text="Ingredients List")
    ing_lbl.grid(row=0, column=5, padx=5)
    list_box_ing = Listbox(self, selectmode=EXTENDED, width=50)
    list_box_ing.grid(row=0, column=5, columnspan=5, rowspan=4, padx=5)
    list_all_ing.list_all_ing(self, list_box_ing)

    add_ing_button = ttk.Button(self, text='Add an ingredient', command=lambda: enter_data_ing.enter_data_ing(self, list_box_ing))
    add_ing_button.grid(row=6, column=5, pady=(20, 0))
    show_ing_button = ttk.Button(self, text='Show ingredient details', command=lambda: show_data_ing.show_data_ing(self, list_box_ing))
    show_ing_button.grid(row=6, column=6, pady=(20, 0))
    update_ing_button = ttk.Button(self, text='Update ingredient information', command=lambda: update_data_ing.update_data_ing(self, list_box_ing))
    update_ing_button.grid(row=6, column=7, pady=(20, 0))
    delete_ing_button = ttk.Button(self, text='Delete ingredient', command=lambda: delete_data_ing.delete_data_ing(self, list_box_ing))
    delete_ing_button.grid(row=6, column=8, pady=(20, 0))
