import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()

def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "Google", variable = vote, value = "Google", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"Google",client_socket)).grid(row = 2,column = 1)
    googleLogo = ImageTk.PhotoImage((Image.open("img/google.png")).resize((90,45),Image.ANTIALIAS))
    googleImg = Label(frame1, image=googleLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Apple", variable = vote, value = "Apple", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"Apple",client_socket)).grid(row = 3,column = 1)
    appleLogo = ImageTk.PhotoImage((Image.open("img/apple.png")).resize((70,35),Image.ANTIALIAS))
    appleImg = Label(frame1, image=appleLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Netflix", variable = vote, value = "Netflix", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"Netflix",client_socket) ).grid(row = 4,column = 1)
    NetflixLogo = ImageTk.PhotoImage((Image.open("img/netflix.png")).resize((70,17),Image.ANTIALIAS))
    NetflixImg = Label(frame1, image=NetflixLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Meta", variable = vote, value = "meta", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"meta",client_socket)).grid(row = 5,column = 1)
    metaLogo = ImageTk.PhotoImage((Image.open("img/meta.png")).resize((70,35),Image.ANTIALIAS))
    metaImg = Label(frame1, image=metaLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNONE", variable = vote, value = "None", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"None",client_socket)).grid(row = 6,column = 1)
    NoneLogo = ImageTk.PhotoImage((Image.open("img/none.png")).resize((30,30),Image.ANTIALIAS))
    NoneImg = Label(frame1, image=NoneLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()

