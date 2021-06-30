from tkinter import *

def counting():
    c = int(counter.get())
    c += 1
    counter.set(c)
    f = open('save.txt', 'w')
    f.write(str(c))
    f.close()

window = Tk()
window.title("simple clicker game")
window.iconbitmap("titleicon.ico")
window.geometry("300x400")
window.resizable(0, 0)

sf = open('save.txt', 'r')

counter = IntVar()
counter.set(int(sf.read()))
countN = Label(window, textvariable=counter)
countN.pack()
button = Button(window, text="click it!", command=counting)
button.pack()

window.mainloop()
