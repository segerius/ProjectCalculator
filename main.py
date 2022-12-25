import random
from tkinter import *

root = Tk()
colors = ['#CD5C5C', '#F08080', '#FA8072', '#E9967A', '#DC143C']


def bgcolorrandom():
    global colors
    rand = random.randrange(0, len(colors) - 1)
    root.config(bg=colors[int(f'{rand}')])


def bgcolorposledovatelno():
    global colors
    for i in range(0, len(colors) - 1):
        root.config(bg=colors[int(f'{i}')])


def bgcolororiginal():
    root.config(bg='#87CEEB')


root.title('Calculator')
root.geometry('700x400+500+200')
root.config(bg='#87CEEB')
btncolor1 = '#FF00FF'
btncolor2 = '#800080'
btncolorravno1 = 'red'
btncolorravno2 = '#800000'

w = Label(text='Калькулятор',
          font=('Arial', 12, 'bold'),
          bg='#4682B4',
          padx=20,
          pady=20,
          width=15,
          height=2,
          anchor='nw'
          )
e = Entry(bg='pink')
btnrandombg = Button(text='Random Color', command=bgcolorrandom)
btnblackorig = Button(text='Original', command=bgcolororiginal)
btnbgposlefovatelno = Button(text='Color', command=bgcolorposledovatelno)
b1 = Button(text='1', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b2 = Button(text='2', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b3 = Button(text='3', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b4 = Button(text='4', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b5 = Button(text='5', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b6 = Button(text='6', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b7 = Button(text='7', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b8 = Button(text='8', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b9 = Button(text='9', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
b0 = Button(text='0', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}', font=('Arial', 16, 'bold'))
bplus = Button(text='+', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
               font=('Arial', 16, 'bold'))
bminus = Button(text='-', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
                font=('Arial', 16, 'bold'))
bumno = Button(text='x', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
               font=('Arial', 16, 'bold'))
brazdel = Button(text='/', width=4, height=2, bg=f'{btncolor1}', activebackground=f'{btncolor2}',
                 font=('Arial', 16, 'bold'))
bravno = Button(text='=', width=4, height=2, bg=f'{btncolorravno1}', activebackground=f'{btncolorravno2}',
                font=('Arial', 16, 'bold'))
bsteret = Button(text='C', width=4, height=2, bg=f'{btncolorravno1}', activebackground=f'{btncolorravno2}',
                 font=('Arial', 16, 'bold'))
w.grid(row=1, column=1)
e.grid(row=2, column=1)
btnrandombg.grid(row=1, column=6)
btnblackorig.grid(row=1, column=7)
btnbgposlefovatelno.grid(row=1, column=8)
b1.grid(row=4, column=2)
b2.grid(row=4, column=3)
b3.grid(row=4, column=4)
b4.grid(row=3, column=2)
b5.grid(row=3, column=3)
b6.grid(row=3, column=4)
b7.grid(row=2, column=2)
b8.grid(row=2, column=3)
b9.grid(row=2, column=4)
b0.grid(row=5, column=2)
bplus.grid(row=2, column=5)
bminus.grid(row=3, column=5)
bumno.grid(row=4, column=5)
brazdel.grid(row=5, column=5)
bravno.grid(row=5, column=3)
bsteret.grid(row=5, column=4)

root.mainloop()
