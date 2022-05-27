# # # import turtle
# # #
# # # t = turtle.Turtle()
# # # t.speed(0)
# # #
# # # #for j jn range(29):
# # # # t.forward(100)
# # # # t.left(90)
# # # # t.forward(10)
# # # # t.left(96)
# # # # t.forward(100)
# # # #experjmental cjrcle gen
# # # for i in range(10):
# # #     j= 180
# # #     t.penup()
# # #     t.forward(100)
# # #     t.left(j)
# # #     t.pendown()
# # #     t.forward(j)
# # #     t.left(j)
# # #     t.pendown()
# # #     t.forward(100)
# # #     t.left(j)
# # #     t.penup()
# # #     t.forward(j)
# # #     t.left(j)
# # #
# # #
# # # turtle.exitonclick()
# # from tkinter import *
# # from tkinter import ttk
# #
# # def cell(event):
# #     '''Identify cell from mouse position'''
# #     row, col = tree.identify_row(event.y), tree.identify_column(event.x)
# #     pos = tree.bbox(row, col)       # Calculate positon of entry
# #     return row, col, pos
# #
# # def single(event=None):
# #     '''Single click to select row and column'''
# #     global row, col, pos
# #     row, col, pos = cell(event)
# #     print('Select', row, col)
# #
# # def ok(event=None):
# #     '''Validate entry as at loses focus'''
# #     tree.set(*item, typed.get())    # Set tree cell text
# #     entry.place_forget()            # Remove entry without deleting it
# #
# # def double(event=None):
# #     '''Double click to edit cell'''
# #     global row, col, pos, item
# #     row, col, pos = cell(event)
# #     print('Edit', row, col)
# #     item = row, col                 # Remember which item you are editing
# #     typed.set(tree.set(row, col))   # Set entry text
# #     x, y, w, h = pos                # Place entry on tree
# #     entry.place(x=x, y=y, width=w, height=h, anchor='nw')
# #     entry.focus_set()               # Set focus in entry
# #
# # def deleterow(event):
# #     '''Delete selected row'''
# #     print('delete', len(tree.selection()))
# #     if len(tree.selection()) != 0:
# #         row = tree.selection()[0]
# #     try:
# #         print('deleterow', row)
# #         tree.delete(row)
# #     except:
# #         print('no row selected')
# #
# #
# # myApp = Tk()
# # myApp.title(" Program ")
# # myApp.geometry("600x600+800+50")
# #
# # tree = ttk.Treeview(myApp, height=20)
# # tree['show'] = 'headings'
# # sb = ttk.Scrollbar(myApp, orient="vertical", command=tree.yview)
# # sb.grid(row=1,column=12,sticky="NS")
# # tree.configure(yscrollcommand=sb.set)
# # tree["columns"]=("1","2")
# # tree.column("1", width=150)
# # tree.column("2", width=150)
# # tree.grid(row=1 ,column=0,pady=5)
# #
# # tree.heading("1", text="Project Name")
# # tree.heading("2", text="Size [m2]")
# #
# # item = tree.insert("", "end", values=("Project Alice","500 GB"))
# # tree.item(item, tags=item)
# #
# # # Mouse & keyboard bindings
# # tree.bind('<1>', single)
# # tree.bind('<Double-Button-1>', double)
# # tree.bind("<Delete>", deleterow)
# #
# # # Create entry in global scope
# # typed = StringVar()
# # entry = ttk.Entry(tree, textvariable=typed)
# # entry.bind('<FocusOut>', ok)
# #
# # # myApp.mainloop()
#
# import turtle
# import turtle as tut
#
#
# pen = turtle.Turtle()
# t = turtle.Turtle()
# t.color("red")
# pen.color("black")
# t.begin_fill()
# t.pensize(6)
# t.left(50)
# t.forward(133)
# t.circle(50,200)
# t.right(140)
# t.circle(50,200)
# t.forward(133)
# pen.write("       LO  E YOU", align='center',font=("Calibri",80 , "bold"))
# t.end_fill()
# tut.Screen().exitonclick()
#

from tkinter import *

# from tkinter import messagebox
#
# top = Tk()
#
# top.geometry("100x100")
# a = "ANuroop"
# b = "SDFGHJKUYANUROOPKJHG"
# c = "You have selected \nCustomer:"+a+"\nwith \ncustomer reference number:"+b
#
# messagebox.showinfo("Selected OPtions",c)
#
# top.mainloop()


