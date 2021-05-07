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

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    
    Lmain = Label(top, text="Block 5 GUI")
    Lmain.grid(column= 0, row= 0)

    B1main = Button(text = "Week 1", bg = "#23d108", command= week1)
    B1main.grid(column = 0, row = 1)
    B2main = Button(text = "Week 2", bg = "#0884d1", )
    B2main.grid(column = 0, row = 2)
    B3main = Button(text = "Week 3", bg = "#9b08d1", )
    B3main.grid(column = 0, row = 3)

def week1():
    clearWindow()
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

if __name__ == "__main__":
    mainMenu()
top.mainloop()
