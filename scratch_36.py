#payments processing file
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

class payment_menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Payment Module")
        self.master.geometry('600x700')
        self.titleLabel = Label(master, text="Payment Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        #self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)


        self.billsTV = ttk.Treeview(height=15,selectmode='browse')
        self.billsTV['columns']= ("Index","Item/Dish","Quantity","Price")
        self.billsTV.column("#0",width=0,stretch=NO)
        self.billsTV.column("Index",anchor=W,width=40)
        self.billsTV.column("Item/Dish",anchor=W,width=160)
        self.billsTV.column("Quantity",anchor=W,width=100)
        self.billsTV.column("Price",anchor=W,width=60)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=9, column=2, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Quantity")
        self.billsTV.heading('#4', text="Price")
        self.billsTV.grid(row=9, column=1,columnspan=10,padx=10)

        #labels
        self.grand_total= Label(master, text="Grand Total:", font="Arial 40", fg="green")
        self.grand_total.grid(row=11, column=1, padx=(0, 0), pady=(0, 0))
        self.mode_payment= Label(master, text="Select Mode of Payment:", font="Arial 20", fg="green")
        self.mode_payment.grid(row=12, column=1,  padx=(0, 0), pady=(0, 0))
        self.cash_recieved= Label(master, text="Cash Recieved:", font="Arial 20", fg="green")
        self.cash_recieved.grid(row=13, column=1,  padx=(0, 0), pady=(15, 0))
        self.credit_card_info = Label(master, text="Credit Card Info:", font="Arial 20", fg="green")
        self.credit_card_info.grid(row=14, column=1, columnspan=1, padx=(0, 0), pady=(15, 0))
        #entry widgets
        self.cash_recieved_entry = Entry(master, font=('calibre', 20, 'bold'), bg='red', width=20)
        self.cash_recieved_entry.grid(row=13, column=2,columnspan=1, padx=20,pady=25)
        self.credit_card_info= Entry(master, font=('calibre', 20, 'bold'), bg='red', width=20)
        self.credit_card_info.grid(row=14, column=2,columnspan=1 ,padx=20,pady=25)
        #OptionMenu
        def selected():
            pass
        self.options=['Cash','Credit']
        self.clicked = StringVar()
        self.drop = OptionMenu(master, self.clicked, *self.options, command=selected)
        self.drop.grid(row=12, column=2,pady=10)

        #buttons
        self.make_payment_button= Button(master,text='Make\nPayment',width=10, height=2)
        self.make_payment_button.grid(row=15,column=2,padx=(20,0),pady=(10,0))
        def insert_data():
            pass
    #back button
    # def widget_clearer(self):
    #     for widget in self.master.winfo_children():
    #         widget.destroy()
    #
    # def cashier_main_menu_display(self):
    #     self.app = cash_menu(self.master)
    #
    # def back_button(self):
    #     self.widget_clearer()
    #     self.cashier_main_menu_display()

def main():
    admin = tk.Tk()
    app = payment_menu_display(admin)
    admin.mainloop()


if __name__ == '__main__':
    main()

