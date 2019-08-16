from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

# Closes window properly
def quit(*args):
    clock_window.destroy()

def clock_time():
    # Getting the time remaining until an event
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
    txt.set(time)

    clock_window.after(1000, clock_time)


# setting up window
clock_window = Tk()
clock_window.attributes("-fullscreen", False)
clock_window.configure(width=250, height=250, background="purple")
clock_window.bind("x", quit)
clock_window.after(1000, clock_time)

# settings for clock time
fnt = font.Font(family="Courier", size=28, weight="bold")
txt = StringVar()
lbl = ttk.Label(clock_window, textvariable=txt, font=fnt, foreground="red", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

clock_window.mainloop()
