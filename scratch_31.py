# completed scratch file for read and write functions for cart treeview
from tkinter import *
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
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2).place(relx=1, x=-2,y=2,anchor=NE)
        self.billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.billsTV['columns'] = ("Item Index", "Item/Dish", "Type of Dish", "Price")
        self.billsTV.column("#0", width=0, stretch=NO)
        self.billsTV.column("Item Index", anchor=W, width=40)
        self.billsTV.column("Item/Dish", anchor=W, width=160)
        self.billsTV.column("Type of Dish", anchor=W, width=100)
        self.billsTV.column("Price", anchor=W, width=60)
        self.billsTV.grid(row=1, column=1, columnspan=2,padx=20)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=1, column=2,columnspan=1, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Type of Dish")
        self.billsTV.heading('#4', text="Price")
        #lefttable
        self.temp_billsTV1 = ttk.Treeview(height=15, selectmode='browse')
        self.temp_billsTV1['columns'] = ("Item Index", "Item/Dish","Quantity",)
        self.temp_billsTV1.column("#0", width=0, stretch=NO)
        self.temp_billsTV1.column("Item Index", anchor=W, width=28)
        self.temp_billsTV1.column("Item/Dish", anchor=W, width=120)
        self.temp_billsTV1.column("Quantity", anchor=CENTER, width=80)
        #righttable
        self.temp_billsTV2 = ttk.Treeview(height=15, selectmode='browse')
        self.temp_billsTV2['columns'] = ("Price", "Total for Qty Sel",)
        self.temp_billsTV2.column("#0", width=0, stretch=NO)
        self.temp_billsTV2.column("Price", anchor=CENTER, width=50)
        self.temp_billsTV2.column("Total for Qty Sel", anchor=CENTER, width=90)
        #self.temp_billsTV.column("Price of Selected Ele", anchor=W, width=60)
        # self.temp_billsTV.column("Price of Selected Qty", anchor=W, width=60)
        #lefttable
        self.temp_billsTV1.grid(row=1, column=3, columnspan=12, padx=130)
        self.temp_billsTV1.heading('#0')
        self.temp_billsTV1.heading('#1', text="Index")
        self.temp_billsTV1.heading('#2', text="Item/Dish")
        self.temp_billsTV1.heading('#3', text="Quantity")
        #right table
        self.temp_billsTV2.grid(row=1, column=7, columnspan=23, padx=160)
        self.temp_billsTV2.heading('#0')
        self.temp_billsTV2.heading('#1', text="Price")
        self.temp_billsTV2.heading('#2', text="Total for Qty Sel")


        #self.temp_billsTV.heading('#4', text="Price of Selected Ele")
        #self.temp_billsTV.heading('#4', text="Price of Selected Qty")
        # # def readEntries(self):
        #     # l=[]
        #     for child in self.temp_billsTV.get_children():
        #         print(self.temp_billsTV.item(child)["values"])





        ##fake data
        # data = {
        #     [1: ["Rava Dosa", "South Indian", 150],
        #     [2: ["Masala Dosa", "South Indian", 120],
        #     [3: ["Sada Dosa", "South Indian", 70],
        #     [4: ["Idli Plate", "South Indian", 40],
        #     [5: ["Vada Plate", "South Indian", 50],
        #     [6: ["Chinese Bhel", "Chinese", 30],
        #     [7: ["Manhurian Soup", "Chinese", 30],
        #     [8: ["Singapore Soup", "Chinese", 30],
        #     [9: ["Chicken 65", "Chinese", 30],
        #     [10: ["Chicken Crispy", "Cinese", 150],
        #     [11: ["Chicken Manchurian", "Chinese", 120],
        #     12: ["Egg Fried Rice", "Chinese", 70],
        #     13: ["Egg Fried Noodles", "Chinese", 40],
        #     14: ["Chicken Fried Rice", "Chinese", 50],
        #     15: ["Chicken Fried Noodles", "Chinese", 30],
        #     16: ["Chicken Triple Rice", "Chinese", 30],
        #     17: ["Chicken Triple Noodles", "Chinese", 30],
        #     18: ["Veg Triple Rice", "Chinese", 30],
        #     19: ["Veg Triple Noodles", "Chinese", 30]
        # }
        # ["Rava Dosa", 70],
        # ["Masala Dosa", 75],
        # ["Sada Dosa", 60],
        # ["Idli Plate", 40],
        # ["Vada Plate", 50],
        # ["Chinese Bhel", 25],
        # ["Manhurian Soup", 50],
        # ["Singapore Soup", 75],
        # ["Chicken 65", 120],
        # ["Chicken Crispy", 135],
        # ["Chicken Manchurian", 130],
        # ["Egg Fried Rice", 85],
        # ["Egg Fried Noodles", 90],
        # ["Chicken Fried Rice", 100],
        # ["Chicken Fried Noodles", 110],
        # ["Chicken Triple Rice", 130],
        # ["Chicken Triple Noodles", 150],
        # ["Veg Triple Rice", 110],
        # ["Veg Triple Noodles", 124],

        data = [
            [1, "Rava Dosa", "South Indian", 70],
            [2, "Masala Dosa", "South Indian", 75],
            [3, "Sada Dosa", "South Indian", 60],
            [4, "Idli Plate", "South Indian", 40],
            [5, "Vada Plate", "South Indian", 50],
            [6, "Chinese Bhel", "Chinese", 25],
            [7, "Manchurian Soup", "Chinese", 50],
            [8, "Singapore Soup", "Chinese", 75],
            [9, "Chicken 65", "Chinese", 120],
            [10, "Chicken Crispy", "Chinese", 135],
            [11, "Chicken Manchurian", "Chinese", 130],
            [12, "Egg Fried Rice", "Chinese", 85],
            [13, "Egg Fried Noodles", "Chinese", 90],
            [14, "Chicken Fried Rice", "Chinese", 100],
            [15, "Chicken Fried Noodles", "Chinese", 110],
            [16, "Chicken Triple Rice", "Chinese", 130],
            [17, "Chicken Triple Noodles", "Chinese", 150],
            [18, "Veg Triple Rice", "Chinese", 110],
            [19, "Veg Triple Noodles", "Chinese", 124],
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
        # self.entry_item_dish_entrybox = Label(master, text="Enter Item INDEX", font="Arial 20", fg="green")
        # self.entry_item_dish_entrybox.grid(row=11, column=2, columnspan=1, padx=(0, 0), pady=(0, 0))
        # self.item_name_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        # self.item_name_entry.grid(row=12, column=2, padx=20)
        #
        # self.entry_item_qty_entrybox = Label(master, text="Enter Item Quantity", font="Arial 20", fg="green")
        # self.entry_item_qty_entrybox.grid(row=11, column=3, columnspan=1, padx=(0, 0), pady=(0, 0))
        # self.item_qty_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        # self.item_qty_entry.grid(row=12, column=3, padx=20)
        # buttons
        # self.cart_add = Button(master, text='Add to\nCart', width=10, height=2)
        # self.cart_add.grid(row=13, column=2, padx=(20, 0), pady=(10, 0))
        # self.cart_del = Button(master, text='Remove from\nCart', width=10, height=2)
        # self.cart_del.grid(row=13, column=3, padx=(20, 0), pady=(10, 0))

        # self.cart_del = Button(master, text='Proceed to\n Payment', width=10, height=2)
        # self.cart_del.grid(row=14, column=3, padx=(20, 0), pady=(10, 0))
        global i
        i = 1
        # trv.insert("", 'end', iid=1,
        #           values=(i, 'Alex', 'Four', 78, 'Male'))

        # l0 = tk.Label(master, text='Add Item',
        #               font=('Helvetica', 16), width=30, anchor="c")
        # l0.grid(row=2, column=1, columnspan=4)

        l1 = tk.Label(master, text='Item Selected: ', width=10, anchor="c")
        l1.grid(row=5, column=1)

        # add one text box

        l2 = tk.Label(master, text='Quantity: ', width=10)
        l2.grid(row=5, column=2)

        # add list box for selection of class
        options = StringVar(master)#options of item
        options.set("")  # default value
        options1 = IntVar(master)#options for quantity
        options1.set("")
        options2 = IntVar()
        optionlist_items_list= [
                    ["Rava Dosa",70],
                    ["Masala Dosa",75],
                    ["Sada Dosa",60],
                    ["Idli Plate", 40],
                    ["Vada Plate", 50],
                    ["Chinese Bhel", 25],
                    ["Manhurian Soup", 50],
                    ["Singapore Soup", 75],
                    ["Chicken 65", 120],
                    ["Chicken Crispy", 135],
                    ["Chicken Manchurian", 130],
                    ["Egg Fried Rice", 85],
                    ["Egg Fried Noodles", 90],
                    ["Chicken Fried Rice", 100],
                    ["Chicken Fried Noodles", 110],
                    ["Chicken Triple Rice", 130],
                    ["Chicken Triple Noodles", 150],
                    ["Veg Triple Rice", 110],
                    ["Veg Triple Noodles", 124],
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
        option_list_price=[
            70,
            75,
            60,
            40,
            50,
            25,
            50,
            75,
            120,
            135,
            130,
            85,
            90,
            100,
            110,
            130,
            150,
            110,
            124,
        ]
        k=0
        j=0
        n = len(optionlist_items_list)
        items = []
        prices = []
        for price in optionlist_items_list:
            if k in range(n):
                prices.append(optionlist_items_list[k][1])
            k = k + 1

        items = []
        for item in optionlist_items_list:
            if j in range(n):
                items.append(optionlist_items_list[j][0])
            j = j + 1

        t1 = OptionMenu(master, options,*items)
        t1.grid(row=10, column=1)

        opt1 = OptionMenu(master, options1, *optionlist_qty)
        opt1.grid(row=10, column=2)

        # l3 = tk.Label(master, text='Price of Selected Quantity: ', width=10)
        # l3.grid(row=5, column=1)

        # add one text box
       #t3 = OptionMenu(master, options2,*option_list_price)


        # radio_v = OptionMenu(my_w, options, "Three", "Four", "Five")
        #
        # r1 = tk.Radiobutton(my_w, text='Male', variable=radio_v, value='Male')
        # r1.grid(row=5, column=3)
        #
        # r2 = tk.Radiobutton(my_w, text='Female', variable=radio_v, value='Female')
        # r2.grid(row=5, column=4)
        def readandWritebillEntries():#read entries and calculate total for particular quantity selected
            ites = options.get()  # read items
            qty = options1.get()  # read qty
            # prices = options.get()  # read gender
            global i
            i = i + 1
            # price = options2[i]  # read prices
            self.temp_billsTV1.insert("", 'end',
                                      values=(i - 1, ites, qty))
            # t1.delete('1.0', END)  # reset the text entry box
            # t3.delete('1.0', END)  # reset the text entry box
            my_str.set("Data added ")
            t1.focus()
            l5.after(3000, lambda: my_str.set(''))
            l=[]
            #total = 0
            #read from cart table(treeview1) with Name of Dish and Quantity
            for child in self.temp_billsTV1.get_children():
                l.append(self.temp_billsTV1.item(child)["values"])
                print(l)
            #item obtained processing
            item_obtained=0
            for h in l:
                item_obtained=h[1]
                print(item_obtained)
            #quantity obtained processing
            qty_obtained = 0
            for y in l:
                qty_obtained=(y[2])
                print(qty_obtained)
            #matching of selected element with respective price
            price_of_sel_el = 0
            for u in range(n):
                if item_obtained==items[u]:
                    price_of_sel_el=prices[u]
            #reference print functions
            print(f"The price of {item_obtained} = {price_of_sel_el} and the quantity selected = {qty_obtained} ")

            total_price_qty_of_ele_sel= qty_obtained*price_of_sel_el
            print(f"Total price for selected element-{item_obtained}={total_price_qty_of_ele_sel}")
            #insertion of obtained values into cart treeview for grandtotal

            #i = i + 1
            self.temp_billsTV2.insert("", 'end',
                                     values=(price_of_sel_el, total_price_qty_of_ele_sel))
            #read from treeview for finding grand totaltotal
            t_nested_l = []
            for child in self.temp_billsTV2.get_children():
                t_nested_l.append(self.temp_billsTV2.item(child)["values"])

            print(t_nested_l)
            #unpacking total from total list
            unpacked_total_list =[]
            for g in t_nested_l:
                tot_obtained = g[1]
                unpacked_total_list.append(tot_obtained)

            print(f"list of totals ={unpacked_total_list}")
            #loop to find grand total
            total = 0
            for q in unpacked_total_list:
                total = total + q
            return total

        b1 = tk.Button(master, text='Add Record', width=10,
                       command=lambda: readandWritebillEntries())
        b1.grid(row=7, column=5)
        b2 = tk.Button(master, text='Remove Record', width=12,
                       command=lambda: readandWritebillEntries())
        b2.grid(row=8, column=5)

        #r=b1

        def G_total():
            t_nested_l = []
            for child in self.temp_billsTV2.get_children():
                t_nested_l.append(self.temp_billsTV2.item(child)["values"])

            print(t_nested_l)
            # unpacking total from total list
            unpacked_total_list = []
            for g in t_nested_l:
                tot_obtained = g[1]
                unpacked_total_list.append(tot_obtained)

            print(f"list of totals ={unpacked_total_list}")
            # loop to find grand total
            total = 0
            for q in unpacked_total_list:
                total = total + q
            print(total)
            grand_Total = Label(master,text=f"Grand Total:{total}",font="Arial 20", fg="green")
            grand_Total.grid(row=4, column=9,padx=30)


        b2 = tk.Button(master, text='Grand Total', width=10,
                       command= lambda:G_total())
        b2.grid(row=8, column=6)
            # price_for_selcted_qty = ob*
            # #     # for i in range(len(l)):
                #     price = l[i+1][1]*l[i+2]
                #     total = total + price
                #     my_str1 = (str(total))
                # # price = int(sb[i].get()) * menu[i][1]
                # # total = total + price
                #     self.temp_billsTV.insert("", 'end', iid=i, text=l[i][1], values=my_str1)

        my_str = tk.StringVar()
        l5 = tk.Label(master, textvariable=my_str, width=10)
        l5.grid(row=8, column=1)

        # def add_data():
        #     ites = options.get()  # read items
        #     qty = options1.get()  # read qty
        #     #prices = options.get()  # read gender
        #     global i
        #     i = i + 1
        #     #price = options2[i]  # read prices
        #     self.temp_billsTV1.insert("", 'end',
        #                              values=(i - 1, ites, qty))
        #     # t1.delete('1.0', END)  # reset the text entry box
        #     # t3.delete('1.0', END)  # reset the text entry box
        #     my_str.set("Data added ")
        #     t1.focus()
        #     l5.after(3000, lambda: my_str.set(''))  # remove the message


def main():
    admin = tk.Tk()
    app = menu_display(admin)
    admin.mainloop()


if __name__ == '__main__':
    main()
