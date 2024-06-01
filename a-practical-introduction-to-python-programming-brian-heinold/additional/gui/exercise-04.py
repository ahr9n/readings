from tkinter import *
from math import factorial

root = Tk()
root.geometry("400x150")


def callback():
    m, n = int(m_entry.get()), int(n_entry.get())
    result.config(text="The Sum is : {} + {} = {}".format(m, n, m + n))


m_label = Label(text="Enter the value of M : ")
m_label.place(x=50, y=20)

m_entry = Entry()
m_entry.place(x=200, y=15, width=170, height=25)

n_label = Label(text="Enter the value of N : ")
n_label.place(x=50, y=50)

n_entry = Entry()
n_entry.place(x=200, y=45, width=170, height=25)

result = Label()
result.place(x=200, y=75)

button = Button(text="Validate", command=callback)
button.place(x=200, y=100, width=170, height=30)

mainloop()
