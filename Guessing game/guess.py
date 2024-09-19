from tkinter import *
import tkinter
import math
import tkinter.messagebox
import random

window = tkinter.Tk()
window.geometry("500x500")

guess = random.randint(1,20)

def message():
    nam = name.get()
    tkinter.messagebox.showinfo("Message Box","You, "+nam+" have to guess between 1-20")

def numberguess():
    value = int(takeguess.get())
    if value > guess:
        tkinter.messagebox.showinfo("Guessing Box","Your guess is too high")
    if value < guess:
        tkinter.messagebox.showinfo("Guessing Box","Your guess is too low")
    elif value == guess:
        tkinter.messagebox.showinfo("Good Guessing Box","You guess the number correctly!")
    



namelbl = Label(window,text = "What's your name?")
takeguesslbl = Label(window,text = " Take a guess:")

guessingame = Label(window,text = "Guessing Game!")

name = Entry(window)
takeguess = Entry(window,width = 7)

namebtn = Button(window,text = "OK",command = message)
takebtn = Button(window,text = "Guess",command = numberguess)


name.place(x = 25, y = 125)
takeguess.place(x = 125, y = 250)

namelbl.place(x = 25, y = 90)
takeguesslbl.place(x = 25,y = 250)

namebtn.place(x = 210,y = 125)
takebtn.place(x = 210, y = 250)

guessingame.place(x = 200, y = 25)

window.mainloop()
