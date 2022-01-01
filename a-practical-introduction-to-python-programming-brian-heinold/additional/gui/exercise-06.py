from tkinter import *

root = Tk()
root.geometry('375x125')


def callback():
    name = entry.get()
    result.config(text=f'Welcome {name} !')


label = Label(text='Enter your name : ')
label.place(x=35, y=20)

entry = Entry()
entry.place(x=175, y=15, width=175, height=25)

button = Button(text='Validate', command=callback)
button.place(x=175, y=45, width=175, height=30)

result = Label()
result.place(x=175, y=90)

mainloop()
