from tkinter import *

root = Tk()
root.geometry("400x125")


def divisors(n):
    divisors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list


def callback():
    n = int(n_entry.get())
    divisors_list = divisors(n)
    output = "The divisors of {} are ".format(n) + str(divisors_list)
    result.config(text=output)


n_label = Label(text="Enter the value of N : ")
n_label.place(x=30, y=20)

n_entry = Entry()
n_entry.place(x=200, y=15, width=170, height=25)

result = Label()
result.place(x=30, y=50)

button = Button(text="Validate", command=callback)
button.place(x=200, y=80, width=170, height=30)

mainloop()
