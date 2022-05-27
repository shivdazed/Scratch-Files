from tkinter import*
import tkinter as tk

class MainWindow():
    def __init__(self,master):
        self.master = master

        self.frame= tk.Frame(self.master,width=600,height=600)
        self.frame.pack()



root = tk.Tk()
window = MainWindow(root)
root.eval('tk::PlaceWindow . center')
root.mainloop()