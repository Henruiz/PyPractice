from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime


# Closes window properly
def quit(*args):
    countdown_window.destroy()


def countdown_method():
    # getting the time remaining until an event
    timeLeft = endTime - datetime.datetime.now()

    # removing micro secs
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    txt.set(timeLeft)

    countdown_window.after(1000, countdown_method)


# setting up window
countdown_window = Tk()
countdown_window.attributes("-fullscreen", False)
countdown_window.configure(width=450, height=250, background="black")
countdown_window.bind("x", quit)
countdown_window.after(1000, countdown_method)

endTime = datetime.datetime(2019, 12, 17, 0, 0)

# settings for clock time
fnt = font.Font(family="Courier", size=28, weight="bold")
txt = StringVar()
lbl = ttk.Label(countdown_window, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

countdown_window.mainloop()