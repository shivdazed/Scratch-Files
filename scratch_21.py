#Program testing comboboxes and adding items to listboxes
from tkinter import*
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("750x750")
listbox_Dish = Listbox(window, height = 10,
                  width = 25,
                  bg = "grey",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "white")
listbox_Qty = Listbox(window, height = 10,
                  width = 2,
                  bg = "grey",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "white")

def selected_dishes(event):
    listbox_Dish.insert(0,clicked_dishes.get())
def selected_qty(event):
    listbox_Qty.insert(0, clicked_num_items.get())


#mylabel = Label(window,text=clicked.get()).grid(row=1,column=1)
options = [
    ["1.Rava Dosa", "South Indian"],
    ["2.Masala Dosa", "South Indian"],
    ["3.Sada Dosa", "South Indian"],
    ["4.Idli Plate", "South Indian"],
    ["5.Vada Plate", "South Indian"],
    ["6.Chinese Bhel", "Chinese"],
    ["7.Manhurian Soup", "Chinese"],
    ["8.Singapore Soup", "Chinese"],
    ["9.Chicken 65", "Chinese"],
    ["10.Chicken Crispy", "Cinese"],
    ["11.Chicken Manchurian", "Chinese"],
    ["12.Egg Fried Rice", "Chinese"],
    ["13.Egg Fried Noodles", "Chinese"],
    ["14.Chicken Fried Rice", "Chinese"],
    ["Chicken Fried Noodles", "Chinese"],
    ["15.Chicken Triple Rice", "Chinese"],
    ["16.Chicken Triple Noodles", "Chinese"],
    ["17.Veg Triple Rice", "Chinese"],
    ["18.Veg Triple Noodles", "Chinese"],
]
quantity=[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]
#for i in range(len(options)):
     #listbox.insert(i,options[i])
#dropdown menu for Menu Items
clicked_dishes = StringVar()
drop_dishes = OptionMenu(window, clicked_dishes, *options,command=selected_dishes)
drop_dishes.grid(row=4,column=2)
#dropdown menu for Quantity of Menu Items
clicked_num_items = StringVar()
drop_num_items = OptionMenu(window, clicked_num_items, *quantity,command=selected_qty)
drop_num_items.grid(row=4,column=4)



listbox_Dish.grid(row=5,column=5)
listbox_Qty.grid(row=5,column=6)
window.mainloop()