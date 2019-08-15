from tkinter import *


class Application(Frame):

    # Constructor
    def __init__(self, parent):
        super(Application, self).__init__(parent)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    # Creating widgets for calculator
    def create_widgets(self):
        # Calculator window
        self.user_input = Entry(self, bg="white", bd=29,
                                insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable=self.UserIn,
                                justify=RIGHT)
        self.user_input.grid(columnspan=4)
        self.user_input.insert(0, "0")

        # Button for 7
        self.button7 = Button(self, bg="cyan", bd=12, text="7", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda:self.buttonClick(7))
        self.button7.grid(row=2, column=0, sticky=W)

        # Button for 8
        self.button8 = Button(self, bg="cyan", bd=12, text="8", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(8))
        self.button8.grid(row=2, column=1, sticky=W)

        # Button for 9
        self.button9 = Button(self, bg="cyan", bd=12, text="9", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(9))
        self.button9.grid(row=2, column=2, sticky=W)

        # Button for 4
        self.button4 = Button(self, bg="cyan", bd=12, text="4", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        # Button for 5
        self.button5 = Button(self, bg="cyan", bd=12, text="5", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        # Button for 6
        self.button6 = Button(self, bg="cyan", bd=12, text="6", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        # Button for 1
        self.button1 = Button(self, bg="cyan", bd=12, text="1", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(1))
        self.button1.grid(row=4, column=0, sticky=W)

        # Button for 2
        self.button2 = Button(self, bg="cyan", bd=12, text="2", padx=35, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(2))
        self.button2.grid(row=4, column=1, sticky=W)

        # Button for 3
        self.button3 = Button(self, bg="cyan", bd=12, text="3", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(3))
        self.button3.grid(row=4, column=2, sticky=W)

        # Button for 0
        self.button0 = Button(self, bg="cyan", bd=12, text="0", padx=33, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        # Button for add
        self.buttonAdd = Button(self, bg="yellow", bd=12, text="+", padx=36, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick("+"))
        self.buttonAdd.grid(row=2, column=3, sticky=W)

        # Button for sub
        self.buttonSub = Button(self, bg="yellow", bd=12, text="-", padx=39, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick("-"))
        self.buttonSub.grid(row=3, column=3, sticky=W)

        # Button for multiplication
        self.buttonMultiple = Button(self, bg="yellow", bd=12, text="*", padx=38, pady=25,
                              font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick("*"))
        self.buttonMultiple.grid(row=4, column=3, sticky=W)

        # Button for division
        self.buttonDivision = Button(self, bg="yellow", bd=12, text="/", padx=38, pady=25,
                                     font=("Helvetica", 20, "bold"),
                                     command=lambda: self.buttonClick("/"))
        self.buttonDivision.grid(row=5, column=3, sticky=W)

        # Button for Equals
        self.buttonEquals = Button(self, bg="yellow", bd=12, text="=", padx=100, pady=25,
                                     font=("Helvetica", 20, "bold"),
                                     command=self.CalculateMath)
        self.buttonEquals.grid(row=5, column=1, sticky=W, columnspan=2)

        # Button for Clear
        self.buttonClear = Button(self, bg="purple", bd=12, text="AC", padx=7, width = 28,
                                   font=("Helvetica", 20, "bold"),
                                   command=self.ClearDisplay)
        self.buttonClear.grid(row=1, columnspan=4, sticky=W)

    # Button Handler
    def buttonClick(self,key):
        self.task = str(self.task)+str(key)
        self.UserIn.set(self.task)

    # Calculating arithmetic
    def CalculateMath(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ""

    # Displaying text on application
    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    # Clearing display field
    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")



calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)
# Not having the window be able to resize
calculator.resizable(width=False, height=False)

calculator.mainloop()

