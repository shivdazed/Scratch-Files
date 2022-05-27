# # strin= "    My name is NAuroop"
# #
# # print(strin[0:4])
# # for a in strin:
# #     print(a)
# #
# # print(len(strin))
# #
# # if ("NAuroop" in strin) or("Anuroop" not in strin):
# #     print("Mistake Present and sorry Anuroop your name was saved incorrectly please try again")
# #
# # print(strin[8:17])
# # print(strin.upper())
# # print(strin.lower())
# # print(strin.strip())#removes whitespaces
# # print(strin.replace("NAuroop","Anuroop"))
# # print(strin.split())#The split() method returns a list where the text between the specified separator becomes the list items.
# #
# #
# age = int(input("Enter your age:"))
# name = input("Enter your name:")
# text= "Your name is {1}, you are {0}"#
# print(text.format(age,name))

# l = ["apple", "banana", "cherry", "apple", "cherry"]
# for ele in l:
#     print(ele)
# print(len(l))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
#
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#
# l = ["apple", "banana", "cherry", "apple", "cherry"]
#
# for item in range(len(l)):
#     print(l[item])
#
# i = 0
# while i < len(l):
#     print(l[i])
#     i = i+1
import random
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# o = int(input("Enter a number"))
#
# n = [ x for x in range(1,o+1) if x<10]
#
# print(n)
#####Classes
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def nameDisplay(self):
#         print("Your name is:",self.name)
#
#
# p = Person("Anuroop",29)
# p.nameDisplay()
# print(p.age)

#
# # Import the required libraries
# from tkinter import *
# from tkinter import ttk
#
# # Create an instance of tkinter frame
# win= Tk()
#
# # Set the size of the tkinter window
# win.geometry("700x350")
#
# # Create an instance of Style widget
# style= ttk.Style()
# style.theme_use('clam')
#
# # Add a Treeview widget and set the selection mode
# tree= ttk.Treeview(win, column=("c1", "c2"), show='headings', height= 8, selectmode="browse")
# tree.column("#1", anchor=CENTER, stretch= NO)
# tree.heading("#1", text="Fname")
# tree.column("#2", anchor=CENTER, stretch=NO)
# tree.heading("#2", text="Lname")
#
# # Insert the data in Treeview widget
# tree.insert('', 'end', text= "1",values=('Alex', 'M'))
# tree.insert('', 'end', text="2",values=('Belinda','Cross'))
# tree.insert('', 'end', text="3",values=('Ravi','Malviya'))
# tree.insert('', 'end', text="4",values=('Suresh','Rao'))
# tree.insert('', 'end', text="5",values=('Amit','Fernandiz'))
# tree.insert('', 'end', text= "6",values=('Raghu','Sharma'))
# tree.insert('', 'end',text= "7",values=('David','Nash'))
# tree.insert('', 'end',text= "8",values=('Ethan','Plum'))
# tree.insert('', 'end', text= "9", values=('Janiece','-'))
#
# # Adding a vertical scrollbar to Treeview widget
# treeScroll = ttk.Scrollbar(win)
# treeScroll.configure(command=tree.yview)
# tree.configure(yscrollcommand=treeScroll.set)
# treeScroll.pack(side= RIGHT, fill= BOTH)
# tree.pack()
#
# win.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import BOTTOM, TOP, RIGHT, LEFT, SUNKEN, W, X, Y, NO, VERTICAL, HORIZONTAL, DISABLED, NONE, S, N, E, W


class myApp:
    def __init__(self, wnd):
        self.wnd = wnd
        self.wnd.title(f"My App")
        self.wnd.geometry('1300x700')
        self.wnd.resizable(False, False)

        self.top_frame = tk.Frame(master=self.wnd, width=1300, height=90, highlightcolor="black",
                                  highlightbackground="black", bg='yellow')
        self.center = tk.Frame(master=self.wnd, width=1300, height=600, highlightcolor="black",
                               highlightbackground="black", )
        self.status_frame = tk.Frame(master=self.wnd, width=1300, height=22, highlightcolor="black",
                                     highlightbackground="black", highlightthickness=1, bg='red')

        self.wnd.grid_rowconfigure(0, weight=1)
        self.wnd.grid_rowconfigure(1, weight=1)
        self.wnd.grid_rowconfigure(2, weight=1)

        self.top_frame.grid(row=0, column=0, sticky="n")
        self.center.grid(row=1, column=0, sticky="n")
        self.status_frame.grid(row=2, sticky="nsew")

        ##############################

        self.center.grid_columnconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)

        self.ctr_left = tk.Frame(self.center, width=900, height=600, highlightcolor="black",
                                 highlightbackground="black", highlightthickness=1)
        self.ctr_right = tk.Frame(self.center, width=400, height=600, highlightcolor="black",
                                  highlightbackground="black", highlightthickness=1)

        self.ctr_left.grid(row=0, column=0, sticky="nsew")
        self.ctr_right.grid(row=0, column=1, sticky="nsew")

        ###############################

        self.ctr_left.grid_rowconfigure(0, weight=1)
        self.ctr_left.grid_rowconfigure(1, weight=1)

        self.frm1 = tk.Frame(self.ctr_left, width=900, height=550, highlightcolor="black", highlightbackground="black",
                             bg='green')
        self.frm2 = tk.Frame(self.ctr_left, width=900, height=50, highlightcolor="black", highlightbackground="black",
                             highlightthickness=1, bg='purple')

        self.frm1.grid(row=0, column=0, sticky="nw")
        self.frm2.grid(row=1, column=0, sticky="sw")

        ################################

        self.ctr_right.grid_rowconfigure(0, weight=1)
        self.ctr_right.grid_rowconfigure(1, weight=1)

        self.frm3 = tk.Frame(self.ctr_right, width=400, height=550, highlightcolor="black", highlightbackground="black",
                             bg='orange')
        self.frm4 = tk.Frame(self.ctr_right, width=400, height=50, highlightcolor="black", highlightbackground="black",
                             highlightthickness=1, bg='pink')

        self.frm3.grid(row=0, column=0, sticky="nw")
        self.frm4.grid(row=1, column=0, sticky="se")

        # add treeview to frame frm1
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                             background="silver",
                             foreground="black",
                             fieldbackground="silver")
        self.style.map("Treeview", background=[('selected', 'green')])

        self.my_tree = ttk.Treeview(master=self.frm1, height=26)

        # define our columns
        self.my_tree['columns'] = ("Date & Time", "Type", "Log Message")
        self.my_tree.column("#0", width=0, minwidth=0, stretch=NO)
        self.my_tree.column("Date & Time", anchor=W, width=140, minwidth=140)
        self.my_tree.column("Type", anchor=W, width=70, minwidth=70)
        self.my_tree.column("Log Message", anchor=W, width=685, minwidth=400, stretch=True)

        # create headings
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("Date & Time", text="Date & Time", anchor=W)
        self.my_tree.heading("Type", text="Type", anchor=W)
        self.my_tree.heading("Log Message", text="Log Message", anchor=W)
        self.my_tree.grid(row=0, column=0, sticky="nsew")

        # add scrollbar to treevew widget my_tree
        self.ytree_scroll = ttk.Scrollbar(master=self.my_tree, orient=VERTICAL, command=self.my_tree.yview)
        self.xtree_scroll = ttk.Scrollbar(master=self.my_tree, orient=HORIZONTAL, command=self.my_tree.xview)
        self.ytree_scroll.grid(row=0, column=0, sticky="nse")
        self.xtree_scroll.grid(row=0, column=0, sticky="ews")

        self.my_tree.configure(yscroll=self.ytree_scroll.set, xscroll=self.xtree_scroll.set)

        # add scrollbar to frame widget frm3


#        self.ytree_scroll1 = ttk.Scrollbar(master=self.frm3, orient=VERTICAL)
#        self.xtree_scroll1 = ttk.Scrollbar(master=self.frm3, orient=HORIZONTAL)
#        self.ytree_scroll1.grid(row=0, column=0, sticky="nse")
#        self.xtree_scroll1.grid(row=0, column=0, sticky="ews")
        self.ytree_scroll = ttk.Scrollbar(master=self.frm1, orient=VERTICAL, command=self.my_tree.yview)
        self.xtree_scroll = ttk.Scrollbar(master=self.frm1, orient=HORIZONTAL, command=self.my_tree.xview)
        self.ytree_scroll.grid(row=0, column=1, sticky="nse")
        self.xtree_scroll.grid(row=1, column=0, columnspan=2, sticky="ews")

if __name__ == "__main__":
    window = tk.Tk()
    application = myApp(window)
    window.mainloop()