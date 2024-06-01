from tkinter import *
from math import factorial

root = Tk()
root.geometry("400x125")


def callback():
    n = int(n_entry.get())
    n2_entry.delete(0, END)
    n2_entry.insert(0, n * 2)


n_label = Label(text="Enter the value of N : ")
n_label.place(x=30, y=20)

n_entry = Entry()
n_entry.place(x=215, y=15, width=170, height=25)

n2_label = Label(text="Here is the double 2*N: ")
n2_label.place(x=30, y=50)

n2_entry = Entry()
n2_entry.place(x=215, y=45, width=170, height=25)

button = Button(text="Validate", command=callback)
button.place(x=215, y=80, width=170, height=30)

mainloop()
