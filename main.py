import random
from tkinter import *

root = Tk()
colors = ['#CD5C5C', '#F08080', '#FA8072', '#E9967A', '#DC143C']
p1 = PhotoImage(file='info.png')
root.iconphoto(False, p1)
root.resizable(False, True)
root.minsize(200, 350)


def bgcolorrandom():
    global colors
    rand = random.randrange(len(colors))
    root.config(bg=colors[int(f'{rand}')])


def bgcolororiginal():
    root.config(bg='#87CEEB')


def delete_entry():
    e.delete(0, END)


def get_result():
    res = e.get()
    RESULT = Label(text=f'{res}').grid(row=7, column=0, columnspan=4)


root.title('Calculator')
root.geometry('248x400+500+200')
root.config(bg='#87CEEB')
btncolor1 = '#FF00FF'
btncolor2 = '#800080'
btncolorravno1 = 'red'
btncolorravno2 = '#800000'

w = Label(text='Калькулятор',
          font=('Arial', 12, 'bold'),
          bg='#4682B4',
          width=2,
          height=2
          )
e = Entry(bg='pink', justify='right', font=('Arial', 15))
btnrandombg = Button(text='Random Color', padx=0, pady=10, bg='#C0C0C0', activebackground='#808080',
                     font=('Arial', 8, 'bold'), command=bgcolorrandom)
btnblackorig = Button(text='Original', padx=0, pady=10, bg='#C0C0C0', activebackground='#808080',
                      font=('Arial', 8, 'bold'), command=bgcolororiginal)
b1 = Button(text='1', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '1'))
b2 = Button(text='2', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '2'))
b3 = Button(text='3', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '3'))
b4 = Button(text='4', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '4'))
b5 = Button(text='5', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '5'))
b6 = Button(text='6', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '6'))
b7 = Button(text='7', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '7'))
b8 = Button(text='8', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '8'))
b9 = Button(text='9', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '9'))
b0 = Button(text='0', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'),
            command=lambda: e.insert(END, '0'))
bplus = Button(text='+', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
               font=('Arial', 16, 'bold'), command=lambda: e.insert(END, '+'))
bminus = Button(text='-', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
                font=('Arial', 16, 'bold'), command=lambda: e.insert(END, '-'))
bumno = Button(text='x', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
               font=('Arial', 16, 'bold'), command=lambda: e.insert(END, '*'))
brazdel = Button(text='/', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
                 font=('Arial', 16, 'bold'), command=lambda: e.insert(END, '/'))
bravno = Button(text='=', width=4, height=2, bg=f'{btncolorravno1}', activebackground=f'{btncolorravno2}',
                font=('Arial', 16, 'bold'), command=get_result)
bsteret = Button(text='C', width=4, height=2, bg=f'{btncolorravno1}', activebackground=f'{btncolorravno2}',
                 font=('Arial', 16, 'bold'), command=delete_entry)
w.grid(row=0, column=0, columnspan=4, sticky='we')
e.grid(row=1, column=0, columnspan=4, sticky='we')
btnrandombg.grid(row=6, column=0, columnspan=2, sticky='we')
btnblackorig.grid(row=6, column=2, columnspan=2, sticky='we')
b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=0)
bplus.grid(row=2, column=3)
bminus.grid(row=3, column=3)
bumno.grid(row=4, column=3)
brazdel.grid(row=5, column=3)
bravno.grid(row=5, column=1)
bsteret.grid(row=5, column=2)

root.mainloop()
