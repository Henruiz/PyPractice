from tkinter import *
# import other python file bugged
from backend import *

# Getting all of the rows
def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])

# Inserting rows to the list
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)


# calling search query call from backend
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

#  calling insert query call from backend
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

# calling delete query call from backend
def delete_command():
    backend.delete(selected_tuple[0])

# calling update query call from backend
def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()
window.configure(background="maroon")
window.wm_title("Online BookStore")

# setting all the labels with their respective titles
label1 = Label(window, text="Title", background="gold", foreground="maroon", font="Helvetica 12 bold")
label1.grid(row=0, column=0)

label2 = Label(window, text="Author", background="gold", foreground="maroon", font="Helvetica 12 bold")
label2.grid(row=0, column=2)

label3=Label(window, text="Year", background="gold", foreground="maroon", font="Helvetica 12 bold")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN", background="gold", foreground="maroon", font="Helvetica 12 bold")
label4.grid(row=1, column=2)

# setting all the entries with respective parameters
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)
 
list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# setting all the buttons with respective titles
btn1 = Button(window, text="View all", width=12, command=view_command, highlightbackground="gold", foreground="maroon", font="Helvetica 12 bold")
btn1.grid(row=2, column=3)

btn2 = Button(window, text="Search entry", width=12, command=search_command, highlightbackground="gold", foreground="maroon", font="Helvetica 12 bold")
btn2.grid(row=3, column=3)

btn3 = Button(window, text="Add entry", width=12, command=add_command, highlightbackground="gold", foreground="maroon", font="Helvetica 12 bold")
btn3.grid(row=4, column=3)

btn4 = Button(window, text="Update selected", width=12, command=update_command, highlightbackground="gold", foreground="maroon", font="Helvetica 12 bold")
btn4.grid(row=5, column=3)

btn5 = Button(window, text="Delete selected", width=12, command=delete_command, highlightbackground="gold", foreground="maroon", font="Helvetica 12 bold")
btn5.grid(row=6, column=3)

btn6 = Button(window, text="Close", width=12, command=window.destroy, highlightbackground="gold", foreground="maroon", font="Helvetica 12 bold")
btn6.grid(row=7, column=3)

window.mainloop()
