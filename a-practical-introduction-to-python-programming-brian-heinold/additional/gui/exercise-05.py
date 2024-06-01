from tkinter import *
from math import factorial, sqrt

root = Tk()
root.geometry("410x150")


def is_perfect_square(n):
    return int(sqrt(n)) ** 2 == n


def callback():
    n = int(entry.get())
    if is_perfect_square(n):
        result.config(
            text="{} is a perfect square {} = {} ^ {}".format(n, n, int(sqrt(n)), 2)
        )
    else:
        result.config(text="{} is not a perfect square".format(n))


label = Label(text="Enter integer N : ")
label.place(x=35, y=20)

entry = Entry()
entry.place(x=175, y=15, width=175, height=25)

button = Button(text="Validate", command=callback)
button.place(x=175, y=60, width=175, height=30)

result = Label()
result.place(x=175, y=100)

mainloop()
