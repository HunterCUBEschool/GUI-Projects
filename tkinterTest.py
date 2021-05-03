from tkinter import *

top = Tk()

L1 = Label(top, text="Hello, world!")

L1.grid(column= 0, row= 1)

E1 = Entry(top, bd = 5)

E1.grid(column= 0, row = 2)

#next class put this line to use
print(E1.get())

top.mainloop()
