#=========Tkinter database========#
from tkinter import *
from pymysql import *

a = Tk()
a.geometry('1500x1500')
a.title('Registration Form')


def DATABASE():
    print(id.get(), pw.get(), rb1.get(), cb1.get())
    Lb1 = Listbox(a, bg="pink", font="Castellar", cursor="target")
    Lb1.insert(1, id.get())
    Lb1.insert(2, pw.get())
    Lb1.insert(3, rb1.get())
    Lb1.insert(4, cb1.get())
    Lb1.grid(row=8, column=7)
    c = connect(host='localhost', user='root', passwd='3p8G1u5c', db='test')
    cur = c.cursor()
    cur.execute("insert into details values('{}',{},{});".format(id.get(), pw.get(), rb1.get()))
    c.commit()
    c.close()


Label(a, text='username', bg='skyblue').grid(row=0, column=0)
Label(a, text='password').grid(row=1, column=0)
id = Entry(a)
id.grid(row=0, column=1)
pw = Entry(a, show='*')
pw.grid(row=1, column=1)
##StringVar IntVar
rb1 = IntVar()
Radiobutton(a, text='Male', value=1, variable=rb1).grid(row=2, column=0)
Radiobutton(a, text='Female', value=2, variable=rb1).grid(row=2, column=1)
cb1 = StringVar()
Checkbutton(a, text='AI', onvalue='AI', variable=cb1).grid(row=3, column=0)
Button(a, text='SUBMIT', command=DATABASE).place(x=100, y=150)
a.configure(background='skyblue')




