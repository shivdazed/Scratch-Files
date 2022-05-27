#ongoing menu interface
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

class menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('1000x600')
        self.master.title("Menu for Customer")
        self.titleLabel = Label(master, text="Menu Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        # self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)
        self.billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.billsTV['columns'] = ("Item Index", "Item/Dish", "Type of Dish", "Price")
        self.billsTV.column("#0", width=0, stretch=NO)
        self.billsTV.column("Item Index", anchor=W, width=40)
        self.billsTV.column("Item/Dish", anchor=W, width=160)
        self.billsTV.column("Type of Dish", anchor=W, width=100)
        self.billsTV.column("Price", anchor=W, width=60)
        self.billsTV.grid(row=1, column=0, columnspan=3)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=1, column=2, columnspan=1, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Type of Dish")
        self.billsTV.heading('#4', text="Price")

        self.temp_billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.temp_billsTV['columns'] = ("Item Index", "Item/Dish", "Type of Dish", "Price")
        self.temp_billsTV.column("#0", width=0, stretch=NO)
        self.temp_billsTV.column("Item Index", anchor=W, width=40)
        self.temp_billsTV.column("Item/Dish", anchor=W, width=160)
        self.temp_billsTV.column("Type of Dish", anchor=W, width=100)
        self.temp_billsTV.column("Price", anchor=W, width=60)
        self.temp_billsTV.grid(row=1, column=3, columnspan=10,padx=40)
        self.temp_billsTV.heading('#0')
        self.temp_billsTV.heading('#1', text="Index")
        self.temp_billsTV.heading('#2', text="Item/Dish")
        self.temp_billsTV.heading('#3', text="Type of Dish")
        self.temp_billsTV.heading('#4', text="Price")

        ###fake data
        data = [
            [1, "Rava Dosa", "South Indian", 150],
            [2, "Masala Dosa", "South Indian", 120],
            [3, "Sada Dosa", "South Indian", 70],
            [4, "Idli Plate", "South Indian", 40],
            [5, "Vada Plate", "South Indian", 50],
            [6, "Chinese Bhel", "Chinese", 30],
            [7, "Manhurian Soup", "Chinese", 30],
            [8, "Singapore Soup", "Chinese", 30],
            [9, "Chicken 65", "Chinese", 30],
            [10, "Chicken Crispy", "Cinese", 150],
            [11, "Chicken Manchurian", "Chinese", 120],
            [12, "Egg Fried Rice", "Chinese", 70],
            [13, "Egg Fried Noodles", "Chinese", 40],
            [14, "Chicken Fried Rice", "Chinese", 50],
            [15, "Chicken Fried Noodles", "Chinese", 30],
            [16, "Chicken Triple Rice", "Chinese", 30],
            [17, "Chicken Triple Noodles", "Chinese", 30],
            [18, "Veg Triple Rice", "Chinese", 30],
            [19, "Veg Triple Noodles", "Chinese", 30]
        ]
        quantity_values = [
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
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20
        ]
        prices=[

        ]
        index_items = [
            "Rava Dosa",
            "Masala Dosa",
            "Sada Dosa",
            "Idli Plate",
            "Vada Plate",
            "Chinese Bhel",
            "Manhurian Soup",
            "Singapore Soup",
            "Chicken 65",
            "Chicken Crispy",
            "Chicken Manchurian",
            "Egg Fried Rice",
            "Egg Fried Noodles",
            "Chicken Fried Rice",
            "Chicken Fried Noodles",
            "Chicken Triple Rice",
            "Chicken Triple Noodles",
            "Veg Triple Rice",
            "Veg Triple Noodles",

        ]
        # striped rows
        self.billsTV.tag_configure('oddrow', background='white')
        self.billsTV.tag_configure('evenrow', background='lightblue')

        # add our data
        global count
        count = 0

        for record in data:
            if count % 2 == 0:
                self.billsTV.insert(parent='', index='end', iid=count, text='',
                                    values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
            else:
                self.billsTV.insert(parent='', index='end', iid=count, text='',
                                    values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
            # increment counter
            count += 1
        self.entry_item_dish_entrybox = Label(master, text="Enter Item INDEX", font="Arial 20", fg="green")
        self.entry_item_dish_entrybox.grid(row=11, column=2, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.item_name_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        self.item_name_entry.grid(row=12, column=2, padx=20)

        self.entry_item_qty_entrybox = Label(master, text="Enter Item Quantity", font="Arial 20", fg="green")
        self.entry_item_qty_entrybox.grid(row=11, column=3, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.item_qty_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        self.item_qty_entry.grid(row=12, column=3, padx=20)
        #buttons
        self.cart_add= Button(master,text='Add to\nCart',width=10, height=2)
        self.cart_add.grid(row=13,column=2,padx=(20,0),pady=(10,0))
        self.cart_del = Button(master, text='Remove from\nCart', width=10, height=2)
        self.cart_del.grid(row=13, column=3, padx=(20, 0), pady=(10, 0))

        self.cart_del = Button(master, text='Proceed to\n Payment', width=10, height=2)
        self.cart_del.grid(row=14, column=3, padx=(20, 0), pady=(10, 0))
        global i
        i = 1
        # trv.insert("", 'end', iid=1,
        #           values=(i, 'Alex', 'Four', 78, 'Male'))

        l0 = tk.Label(master, text='Add Item',
                      font=('Helvetica', 16), width=30, anchor="c")
        l0.grid(row=2, column=1, columnspan=4)

        l1 = tk.Label(master, text='Item Selected: ', width=10, anchor="c")
        l1.grid(row=3, column=1)

        # add one text box

        l2 = tk.Label(master, text='Quantity: ', width=10)
        l2.grid(row=3, column=3)

        # add list box for selection of class
        options = StringVar(master)
        options.set("")  # default value
        options1 = StringVar(master)
        options1.set("")
        options2 = StringVar(master)
        options2.set("")
        optionlist_items = [
            "Rava Dosa",
            "Masala Dosa",
            "Sada Dosa",
            "Idli Plate",
            "Vada Plate",
            "Chinese Bhel",
            "Manhurian Soup",
            "Singapore Soup",
            "Chicken 65",
            "Chicken Crispy",
            "Chicken Manchurian",
            "Egg Fried Rice",
            "Egg Fried Noodles",
            "Chicken Fried Rice",
            "Chicken Fried Noodles",
            "Chicken Triple Rice",
            "Chicken Triple Noodles",
            "Veg Triple Rice",
            "Veg Triple Noodles",
        ]
        optionlist_qty = [1,
                          2,
                          3,
                          4,
                          5,
                          6,
                          7,
                          8,
                          9,
                          10,
                          11,
                          12,
                          13,
                          14,
                          15,
                          16,
                          17,
                          18,
                          19

                          ]
        t1 = OptionMenu(master, options, *optionlist_items)
        t1.grid(row=3, column=2)

        opt1 = OptionMenu(master, options1, *optionlist_qty)
        opt1.grid(row=3, column=4)

        l3 = tk.Label(master, text='Price of Selected Quantity: ', width=10)
        l3.grid(row=5, column=1)

        # add one text box
        t3 = OptionMenu(master, options2, "nothing")
        t3.grid(row=5, column=2)

        # radio_v = OptionMenu(my_w, options, "Three", "Four", "Five")
        #
        # r1 = tk.Radiobutton(my_w, text='Male', variable=radio_v, value='Male')
        # r1.grid(row=5, column=3)
        #
        # r2 = tk.Radiobutton(my_w, text='Female', variable=radio_v, value='Female')
        # r2.grid(row=5, column=4)

        b1 = tk.Button(master, text='Add Record', width=10,
                       command=lambda: add_data())
        b1.grid(row=6, column=2)
        my_str = tk.StringVar()
        l5 = tk.Label(master, textvariable=my_str, width=10)
        l5.grid(row=8, column=1)

        def add_data():
            my_name = options.get()  # read items
            my_class = options1.get()  # read qty
            my_mark = options2.get()  # read price
            my_gender = options.get()  # read gender
            global i
            i = i + 1
            t_price = int(options1[i].get()) * int(options2[i].get())
            self.temp_billsTV.insert("", 'end',
                       values=(i - 1, my_name, my_class,t_price, my_gender))

            # t1.delete('1.0', END)  # reset the text entry box
            # t3.delete('1.0', END)  # reset the text entry box
            my_str.set("Data added ")
            t1.focus()
            l5.after(3000, lambda: my_str.set(''))  # remove the message


def main():
    admin = tk.Tk()
    app = menu_display(admin)
    admin.mainloop()

if __name__ == '__main__':
    main()
