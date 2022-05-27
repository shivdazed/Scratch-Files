#Payementmodule
import pymysql
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
"""
making of payment section and total bill
"""
class payment():
    def __init__(self, master):
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('600x500')

        self.titleLabel = Label(master, text="Customer Payment Page", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))


        self.billsTV = ttk.Treeview(height=15,selectmode='browse')
        self.billsTV['columns']= ("Item Index","Item/Dish","Quantity","Price")
        self.billsTV.column("#0",width=0,stretch=NO)
        self.billsTV.column("Item Index",anchor=W,width=40)
        self.billsTV.column("Item/Dish",anchor=W,width=160)
        self.billsTV.column("Quantity",anchor=W,width=100)
        self.billsTV.column("Price",anchor=W,width=60)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=9, column=0, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Quantity")
        self.billsTV.heading('#4', text="Price")
        self.billsTV.grid(row=9, column=0)

        ##checking database
#        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
#        curs=conn.cursor()
#        curs.execute("select* from active_reigistry")
        self.billsTV.grid()


        #define number of columns
       # self.trv["columns"] = ()

#        import customer_pos
#  def customer_main_menu(self):

#        self.newWindow = tk.Toplevel(self.master)
#        self.app = cash_booking_display(self.newWindow)

admin = tk.Tk()
app = payment(admin)
admin.mainloop()
