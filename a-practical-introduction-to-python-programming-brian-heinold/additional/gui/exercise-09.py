from tkinter import *
from tkinter import ttk
from math import gcd
from numpy import lcm

root = Tk()
root.geometry('350x150')


def callback(event):
    n, m = int(n_entry.get()), int(m_entry.get())
    choice = combobox.get()
    if choice == 'GCD':
        output = 'GCD(m, n) = ' + str(gcd(n, m))
        result.config(text=output)
    elif choice == 'LCM':
        output = 'LCM(m, n) = ' + str(lcm(n, m))
        result.config(text=output)


m_label = Label(text='Enter value of m: ')
m_label.place(x=15, y=20)

m_entry = Entry()
m_entry.place(x=150, y=15, width=175, height=25)

n_label = Label(text='Enter value of n: ')
n_label.place(x=15, y=50)

n_entry = Entry()
n_entry.place(x=150, y=45, width=175, height=25)

choose = Label(text='Choose function: ')
choose.place(x=15, y=80)

combobox = ttk.Combobox(root, state='readonly')
combobox.set('Select the operation')
combobox.place(x=150, y=75, width=175, height=25)
combobox.bind("<<ComboboxSelected>>", callback)
combobox['values'] = ('GCD', 'LCM')

result = Label()
result.place(x=155, y=110)

mainloop()
