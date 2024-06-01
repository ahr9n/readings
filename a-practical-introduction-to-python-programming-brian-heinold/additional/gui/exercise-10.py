from tkinter import *
from math import factorial

root = Tk()
root.geometry("400x150")


def callback():
    name, age = m_entry.get(), eval(n_entry.get())
    if age >= 18:
        output = "Welcome, " + name + ". You are major!"
        result.config(text=output)
    else:
        output = "Welcome, " + name + ". You are minor!"
        result.config(text=output)


m_label = Label(text="Enter your name: ")
m_label.place(x=20, y=20)

m_entry = Entry()
m_entry.place(x=160, y=15, width=170, height=25)

n_label = Label(text="Enter your age: ")
n_label.place(x=20, y=50)

n_entry = Entry()
n_entry.place(x=160, y=45, width=170, height=25)

result = Label()
result.place(x=160, y=75)

button = Button(text="Validate", command=callback)
button.place(x=160, y=100, width=170, height=30)

mainloop()
