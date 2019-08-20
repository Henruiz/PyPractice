from tkinter import *
# this is just to get familiar with tkinter more
# creating window
window = Tk()

# class that will convert miles to km
def converter():
    print(userInput.get())
    miles = float(userInput.get()) * 1.60934
    # display what the user typed in the 2nd column
    text1.insert(END, miles)



# Displaying a button and placing it on the grid
btn1 = Button(window, text="Convert", command=converter)
btn1.grid(row = 0, column = 0)

# setting user input as a string
userInput = StringVar()

# Creating user entry window and placing it on the grind
entry1 = Entry(window, textvariable = userInput)
entry1.grid(row = 0, column = 1)

# Creating text widget and placing it on the grid
text1 = Text(window, height = 1, width = 20)
text1.grid(row = 0, column = 2)

# Continue running until exit
window.mainloop()
