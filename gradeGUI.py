from tkinter import *
from tkinter import ttk

root = Tk()

def mainWindows():
    global root
    root.title("Calculate Grade")
    return root

def drawMenu():
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit",command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    return menubar

def drawBox():
    Label(root, text="subject").grid(row=0,column=1)
    Label(root,text="", width=5).grid(row=0,column=2)
    Label(root, text="credit").grid(row=0,column=3)
    Label(root,text="", width=5).grid(row=0,column=4)
    Label(root, text="grade").grid(row=0,column=5)
    Label(root,text="", width=5).grid(row=0,column=6)
    Label(root, text="total").grid(row=0,column=7)

    ######## Subject #########
    S1 = Entry(root, bd=3)
    S1.grid(row=1,column=1)
    S2 = Entry(root, bd=3)
    S2.grid(row=2,column=1)
    S3 = Entry(root, bd=3)
    S3.grid(row=3,column=1)

    ######## Credit #########
    global C1,C2,C3,G1,G2,G3
    C1 = Entry(root, bd=3)
    C1.grid(row=1, column=3)
    C2 = Entry(root, bd=3)
    C2.grid(row=2, column=3)
    C3 = Entry(root, bd=3)
    C3.grid(row=3, column=3)

    ######## Grade ##########
    G1 = Entry(root, bd=3)
    G1.grid(row=1, column=5)
    G2 = Entry(root, bd=3)
    G2.grid(row=2, column=5)
    G3 = Entry(root, bd=3)
    G3.grid(row=3, column=5)
    ######## Total #########

def mainPrograme():
    root = mainWindows()
    drawMenu()
    drawBox()
    Button(root, text='calculate').grid(row=4,column=7)
    root.mainloop()

mainPrograme()
