from tkinter import *

top = Tk()
songList = []

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
    B2main = Button(text = "Week 2", bg = "#0884d1", command= week2)
    B2main.grid(column = 0, row = 2)
    B3main = Button(text = "Week 3", bg = "#9b08d1", )
    B3main.grid(column = 0, row = 3)

def week1():
    def addTrack():
        songList.append(E1.get())
        E1.delete(0, END)
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


def week2():
    clearWindow()

    L1W2 = Label(top, text="Number of Rolls")
    L1W2.grid(column= 0, row= 1)
    
    L2W2 = Label(top, text="Number of Sides")
    L2W2.grid(column= 2, row= 1)
              
    L3W2= Label(top, text="Dice Roller App")
    L3W2.grid(column= 1, row= 0)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column= 0, row= 2)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column= 2, row= 2)
    
    B1W2 = Button(text= "Roll Dice", bg = "Yellow")
    B1W2.grid(column = 1, row = 4)

if __name__ == "__main__":
    mainMenu()
top.mainloop()
