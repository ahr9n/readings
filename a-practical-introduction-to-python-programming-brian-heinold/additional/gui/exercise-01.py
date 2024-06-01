from tkinter import *

root = Tk()
root.geometry("400x150")


def callback():
    word = entry.get()
    reversed_word = word[::-1]
    result.config(text=reversed_word)


label = Label(text="Enter a word : ")
label.place(x=20, y=20)

entry = Entry()
entry.place(x=150, y=20, width=225, height=25)

result = Label()
result.place(x=150, y=60)

button = Button(text="Validate", command=callback)
button.place(x=150, y=100, width=225, height=30)

mainloop()
