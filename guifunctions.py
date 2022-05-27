''''
#for displaying windows
import tkinter
t=tkinter.Tk()# main window
t.title("Editor")
t.geometry("500x500")
t.mainloop()
'''




'''
# for messagebox and title
import tkinter
from tkinter import messagebox
t=tkinter.Tk()
t.title("VideoEditor")
t.geometry("500x500")
t.configure(bg='blue')
t.withdraw()# for not displaying the main window
messagebox.showerror("Error","Invalid syntax")
messagebox.showwarning("Warning","There is no space in the drive")
messagebox.showinfo("Information","Successfully installed")
messagebox.askquestion('message','do u wish to contnuine')
messagebox.askyesnocancel('message','do u wish to contnuine')
b=messagebox.askretrycancel('message','do u wish to contnuine')
print(b)
'''
'''
#example for msgbox:
import tkinter as tk
from tkinter import messagebox
r = tk.Tk()
r.title('Counting Seconds')
r.geometry('500x500')
def show():
    messagebox.askquestion('message','do u wish to contnuine')

button = tk.Button(r, text='Stop',font=("Times New Roman",20),bg="red",fg="white", command=show)

button.grid(column=0,row=0)# column and row
button.pack()#middle of ur page it will place
r.mainloop()
'''
'''

#widgets-1--labelbox
import tkinter
t=tkinter.Tk()
t.title("VideoEditor")
t.geometry("500x500")
l=tkinter.Label(t,text="Welcome",font=("Times New Roman Bold",20))
l.pack() #for display in window withoout grid method
l.place(x=50,y=50)
l1=tkinter.Label(t,text="",width="500",height="4",bg="red")
l2=tkinter.Label(t,text="",width="500",height="4",bg="orange")
l3=tkinter.Label(t,text="",width="500",height="4",bg="yellow")
l4=tkinter.Label(t,text="",width="500",height="4",bg="green")
l5=tkinter.Label(t,text="",width="500",height="4",bg="blue")
l6=tkinter.Label(t,text="",width="500",height="4",bg="grey")
l7=tkinter.Label(t,text="",width="500",height="4",bg="purple")
l1.grid(column=0,row=0)
l2.grid(column=0,row=1)
l3.grid(column=0,row=2)
l4.grid(column=0,row=3)
l5.grid(column=0,row=4)
l6.grid(column=0,row=5)
l7.grid(column=0,row=6)
t.mainloop()
'''

'''
#2-button
import tkinter
from tkinter import messagebox
t=tkinter.Tk()
t.title("VideoEditor")
t.geometry("500x500")
l=tkinter.Label(t,text="Welcome to GUI")
def shows():
    messagebox.showinfo("message","Button is Pressed")
b=tkinter.Button(t,text="Click Me",command=shows,bg="red",fg="black")
l.grid(column=0,row=0)
b.grid(column=0,row=1)
t.mainloop()


#3-Textbox
from tkinter import *
t=Tk()
t.title("VideoEditor")
t.geometry("500x500")
l=Label(t,text="Welcome to GUI")
def shows():
    msg=a.get()
    l.configure(text=msg)
b=Button(t,text="Click Me",command=shows,bg="red",fg="black")
l.grid(column=0,row=0)
a=Entry(t,width=10)
a.grid(column=1,row=0)
b.grid(column=0,row=1)
t.mainloop()


#4-checkbutton
from tkinter import *
t=Tk()
t.title("VideoEditor")
t.geometry("500x500")
state=BooleanVar()
c1=Checkbutton(t,text='one',var=state)
c2=Checkbutton(t,text='two',var=state)
state.set(True)
c1.grid(column=1,row=0)
c2.grid(column=0,row=1)
t.mainloop()

#5-Radiobutton
from tkinter import *
t=Tk()
t.title("VideoEditor")
t.geometry("500x500")
c1=Radiobutton(t,text='one',value=1)
c2=Radiobutton(t,text='two',value=2)
c1.grid(column=0,row=0)
c2.grid(column=1,row=0)
t.mainloop()

'''





















