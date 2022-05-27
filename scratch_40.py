#completed database entry test for customer///date--saturdaymarch19th
#customer details page ongoing
from tkinter import *
import tkinter as tk
import random
#import string as stri
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

class cash_booking_display():
    def __init__(self, master):
        #initalisiations to frame
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('575x500')
        self.master.title("Customer Registry")

        self.titleLabel = Label(master, text="Customer Details Table", font="Arial 30", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=6, padx=(0, 0), pady=(0, 0))
        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()
        query1 = "TRUNCATE TABLE CustomerInfo"
        cursor.execute(query1)
        # query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
        # cursor.execute(query2)

        # # self.tableLabel = LabelFrame(master, text="Active Customer Registry", font="Arial 20")
        # # self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)
        # self.backButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
        #                                                                                                       x=-2, y=2,
        #                                                                                                       anchor=NE)

        #customer name details(left)
        self.trv = ttk.Treeview(height=9, selectmode='browse')
        self.trv['columns'] = ("Index", "Customer Name")
        self.trv.column("#0", width=0, stretch=NO)
        self.trv.column("Index", anchor=W, width=40)
        self.trv.column("Customer Name", anchor=W, width=220)
        # self.trv.column("Entry Time", anchor=W, width=80)
        self.trv.grid(row=1,column=0,columnspan=1,padx=(60,0),pady=10)

        # # self.scrollBar = Scrollbar(self.master, orient="vertical")
        # # self.scrollBar.grid(row=3, column=1, columnspan=5, sticky="NSE")
        # # self.scrollBar.config(command=self.trv.yview)
        # self.trv.configure(yscrollcommand=self.scrollBar.set)
        self.trv.heading('#0')
        self.trv.heading('#1', text="Index")
        self.trv.heading('#2', text="Customer Name")
        # self.trv.heading('#3', text="Entry Time")

        #customer reference number table
        self.trv1 = ttk.Treeview(height=9, selectmode='browse')
        self.trv1['columns'] = ("Customer Reference Number",)
        self.trv1.column("#0", width=0, stretch=NO)
        self.trv1.column("Customer Reference Number", anchor=W, width=190)
        self.trv1.grid(row=1,column=1,columnspan=3,pady=10)
        self.trv1.heading('#0')
        self.trv1.heading('#1', text="Customer Reference Number")


        # self.trv = ttk.Treeview(self.master, columns=(0,), height="4")
        # self.style = ttk.Style(self.trv)
        # self.style.configure('Treeview', rowheight=20)
        # self.trv.heading()
        # self.trv.heading('#1', text="Customer Name")
        # # self.trv.heading('#2', text="Registered Mobile Number(RMN)")
        # # self.trv.heading('#3', text="Assigined Table Number(RTN)")
        # self.trv.grid(row=3,column=0,columnspan=10,padx=(16,0))
        # # self.clockLabel = Label(master, text="Clock", font="Arial 20", fg="red").grid(row=3, column=0,padx=(0, 0), pady=(20, 0))

        #CUSTOMER ENTRY WIDGET
        self.cust_entrylabel = Label(master, text="Enter Customer Name:", font="Arial 20", fg="green")
        self.cust_entrylabel.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.customer_name_entry= Entry(master,font=('calibre',15, 'bold'),bg='red',width=20)
        self.customer_name_entry.grid(row=5,column=0,padx=30,pady=0)
        # self.time_entrylabel = Label(master, text="Enter Customer Entry Time:", font="Arial 20", fg="green")
        # self.time_entrylabel.grid(row=4, column=1, padx=(0, 0), pady=(0, 0))
        # self.customer_time_entry = Entry(master, font=('calibre', 15, 'bold'), bg='red', width=20)
        # self.customer_time_entry.grid(row=5, column=1, padx=30, pady=0)

        #Customer Review Buttons For next page
        self.open_cust_menu_Button = Button(master, text="Open Customer Menu", width=15, height=2).grid(row=7,column=0,padx=0,pady=10)
        self.confirm_selection_Button = Button(master, text="Confirm\nSelection", width=15, height=2).grid(row=6,column=0,padx=0,pady=0)
        #Customer Table Buttons
        self.add_customer_Button = Button(master, text="Add\n Customer ", width=12, height=2,command=lambda:insert_data()).grid(row=6, column=1, padx=0, pady=10)
        self.del_customer_Button = Button(master, text="Remove\n Customer ", width=12, height=2,command=lambda:remove_selected_data()).grid(row=7, column=1, padx=30, pady=0)
        # self.gen_custref_num_Button = Button(master, text="Generate Customer\n Reference Number", width=15,height=2,command=lambda:gen_cust_ref_id()).grid(row=6, column=0, padx=0, pady=0)
        self.name =StringVar()
        self.time= StringVar()
        self.i = 0

        #Functions bound to the buttons
        def remove_selected_data():
            y = self.trv1.focus()
            self.trv.delete(y)

        def insert_data():
            """
            Insertion method.
            """
            self.i = self.i + 1
            self.name = self.customer_name_entry.get()
            # self.time = self.customer_time_entry.get()
            self.trv.insert('', 'end',iid=self.i, values=(self.i,self.name))
            self.customer_name_entry.delete(0,END)
            # # Increment counter
        #def gen_cust_ref_id():
            import string as stri
            l = []
            for child in self.trv.get_children():
                l.append(self.trv.item(child)["values"])

            n_child=len(l)
            v = str(l[n_child-1][1])
            cust_name=v.upper()
            letters = stri.ascii_uppercase
            n = len(cust_name)

            f = cust_name
            a = ''.join(random.choice(f) for j in range(2))
            self.result_str = ''.join(random.choice(letters) for h in range(4))+f+a
            print(self.result_str)

            self.trv1.insert('', 'end', values=self.result_str)
            self.customer_name_entry.delete(0, END)
            v=""
            r=[]
            for child in self.trv1.get_children():
                r.append(self.trv1.item(child)["values"])
            num_childs=len(r)
            #unpackiung list of list
            p =[item for elem in r for item in elem]
            b = p[num_childs-1]

            custName = cust_name
            custRefID = b.upper()
            conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
            cursor = conn.cursor()
            # query1 = "TRUNCATE TABLE CustomerInfo"
            query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
            cursor.execute(query2)
            # cursor.execute(query1)
            conn.commit()
            conn.close()
            # if num_childs>1:
            #     t = []
            #     for a in range(num_childs-2):
            #         k = r[0][1:a]
            #         t.append(k)
            #     print(t)
            # #     # for a in k:
            # elif num_childs==1:
            #     p = r[0][0]
            #     print(p)
            #     #     t.append(k[0][])
                # for a in range(num_childs):
                #    t.append(k)
                # a = list(t[0][0:-1])
                # print(a)


                # for a in h:
                #     i.append(a)
                # print(i)



            """
            Insertion method.
            """
            # Increment counter
            # self.customer_name_entry.delete(0, END)

            # define number of columns
        # self.trv["columns"] = ()

    #        import customer_pos
    #  def customer_main_menu(self):

    #        self.newWindow = tk.Toplevel(self.master)
    #        self.app = cash_booking_display(self.newWindow)

# #back button
#     def widget_clearer(self):
#         for widget in self.master.winfo_children():
#             widget.destroy()
#
#     def cashier_main_menu_display(self):
#         self.app = cash_menu(self.master)
#
#     def back_button(self):
#         self.widget_clearer()
#         self.cashier_main_menu_display()


def main():
    admin = tk.Tk()
    app = cash_booking_display(admin)
    admin.mainloop()


if __name__ == '__main__':
    main()

# def gen_cust_ref_id():
#
#     custName = cust_name
#     custRefID= cust_ref_ID
#     conn = pymysql.connect(host="localhost",user="root",passwd="anuroop1602",db="billService")
#     cursor = conn.cursor()
#
#     query ="insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
#     cursor.execute(query)
#     conn.commit()
#     conn.close()
#
