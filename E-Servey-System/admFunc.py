import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    googleLogo = ImageTk.PhotoImage((Image.open("img/google.png")).resize((90,45),Image.ANTIALIAS))
    googleImg = Label(frame1, image=googleLogo).grid(row = 2,column = 0)

    appleLogo = ImageTk.PhotoImage((Image.open("img/apple.png")).resize((70,35),Image.ANTIALIAS))
    appleImg = Label(frame1, image=appleLogo).grid(row = 3,column = 0)

    NetflixLogo = ImageTk.PhotoImage((Image.open("img/netflix.png")).resize((70,17),Image.ANTIALIAS))
    NetflixImg = Label(frame1, image=NetflixLogo).grid(row = 4,column = 0)

    metaLogo = ImageTk.PhotoImage((Image.open("img/meta.png")).resize((70,35),Image.ANTIALIAS))
    metaImg = Label(frame1, image=metaLogo).grid(row = 5,column = 0)

    NoneLogo = ImageTk.PhotoImage((Image.open("img/none.png")).resize((30,30),Image.ANTIALIAS))
    NoneImg = Label(frame1, image=NoneLogo).grid(row = 6,column = 0)


    Label(frame1, text="Google             :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['Google'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text="Apple               :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['Apple'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text="Netflix               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['Netflix'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text="Meta                 :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['meta'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text="None               :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['None'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()

