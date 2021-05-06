from tkinter import *

top = Tk()
songList = []

def addTrack():
    songList.append(E1.get())
    E1.delete(0, END)

def printList():
    print(songList)

def exportLists():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

#label
L1 = Label(top, text="Playlist Generator")
L1.grid(column= 0, row= 1)

#entry
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row = 2)

B1 = Button(text = " + ", bg = "white", command= addTrack)
B1.grid(column = 1, row = 2)

B2 = Button(text = "Playlist", bg = "light blue", command= printList)
B2.grid(column = 1, row = 1)

B3 = Button(text = "Export", bg = "red", command = exportLists)
B3.grid(column = 1, row = 3)

print(E1.get())

top.mainloop()
