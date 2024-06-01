from tkinter import *
from math import factorial

root = Tk()
root.geometry("450x150")


def callback():
    n = int(entry.get())
    result.config(text="The factorial of {} is {}! = {}".format(n, n, factorial(n)))


label = Label(text="Enter value of integer N : ")
label.place(x=20, y=20)

entry = Entry()
entry.place(x=190, y=20, width=225, height=25)

result = Label()
result.place(x=190, y=60)

button = Button(text="Validate", command=callback)
button.place(x=190, y=100, width=225, height=30)

mainloop()
