from tkinter import *
import random

top = Tk(className=" Tkinter Practice")
songList = []
myRolls = []
rollTimes = []
dieType = []
myList = []
unique_list = []


def printList():
    print(songList)

def printListW3():
    print(myList)

def exportLists():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s\n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    top.geometry("400x400")
    top.configure(bg="#87a399")
    
    Lmain = Label(top, text="Block 5 GUI")
    Lmain.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    B1main = Button(text = "Week 1", bg = "#23d108", command= week1)
    B1main.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    B2main = Button(text = "Week 2", bg = "#0884d1", command= week2)
    B2main.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    B3main = Button(text = "Week 3", bg = "#9b08d1", command= week3)
    B3main.place(relx=0.5, rely=0.6, anchor=CENTER)
    

def week1():
    clearWindow()
    def addTrack():
        songList.append(E1.get())
        E1.delete(0, END)
    #label
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row= 1)
    L1.place(relx=0.42, rely=0.3, anchor=CENTER)
    
    #entry
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)
    E1.place(relx=0.4, rely=0.4, anchor=CENTER)

    B1 = Button(text = " + ", bg = "white", command= addTrack)
    B1.grid(column = 1, row = 2)
    B1.place(relx=0.6, rely=0.4, anchor=CENTER)

    B2 = Button(text = "Playlist", bg = "light blue", command= printList)
    B2.grid(column = 1, row = 1)
    B2.place(relx=0.452, rely=0.5, anchor=CENTER)

    B3 = Button(text = "Export", bg = "red", command = exportLists)
    B3.grid(column = 1, row = 3)
    B3.place(relx=0.57, rely=0.5, anchor=CENTER)

    B4 = Button(text = "Main Menu", bg = "blue", command = mainMenu)
    B4.grid(column= 0, row = 3)
    B4.place(relx=0.3, rely=0.5, anchor=CENTER)


def week2():
    def rollDice():
        #update variable data
        rollTimes = E1W2.get()
        dieType = E2W2.get()
        #clear window
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(rollTimes)):
            myRolls.append (random.randint(1, int(dieType)))
        #display the rolls and exit button
        L4W2 = Label(top, text = "Roll Result")
        L4W2.grid(column= 1, row= 0)
        
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column= 1, row= 1)
        
        B2W2 = Button(text = "Main Menu", bg = "blue", command = mainMenu)
        B2W2.grid(column= 1, row= 2)

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
        
        B1W2 = Button(text= "Roll Dice", bg = "Yellow", command = rollDice)
        B1W2.grid(column = 1, row = 4)

def addToListGUI():
    def AddToList():
        myList.append(E1W3.get())
        E1W3.delete(0,END)
    clearWindow()
    L1W3 = Label(top, text= 'Type number here')
    L1W3.grid(column= 0, row= 1)
    
    E1W3 = Entry(top, bd = 5)
    E1W3.grid(column= 0, row= 2)
    
    B2W3 = Button(text= "Add to list", bg= "red", command= AddToList)
    B2W3.grid(column = 1, row= 2)
    B3W3 = Button(text= "Print list", bg= "blue", command= printListW3)
    B3W3.grid(column= 0, row= 3)

def addABunch():
    clearWindow()
    try:
        L2W3 = Label(top, text= "Number of integers")
        L2W3.grid(column= 2, row= 0)
        E2W3 = Entry(top, bd = 5)
        E2W3.grid(column= 2, row= 1)
        L3W3 = Label(top, text= "Bottom range")
        L3W3.grid(column= 0, row= 2)
        E3W3 = Entry(top, bd = 5)
        E3W3.grid(column= 0, row= 3)
        L4W3 = Label(top, text= "Top range")
        L4W3.grid(column= 3, row= 2)
        E4W3 = Entry(top, bd = 5)
        E4W3.grid(column= 3, row= 3)

        """
        for x in range (0, int(numToAdd)):
            myList.append(random.randint(int(numBottomRange), int(numTopRange)))
        print("Your list is now complete.")
        print("Sorting your data...")
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        """
    except:
        week3()
    
def week3():
    
    clearWindow()
    B1W3 = Button(text = "Add to the list", bg = "light blue",command= addToListGUI)
    B1W3.grid(column= 1, row= 2)


    B4W3 = Button(text= "Add a bunch", bg= "blue",command= addABunch)
    B4W3.grid(column= 4, row= 4)
              
        

if __name__ == "__main__":
    mainMenu()
top.mainloop()
