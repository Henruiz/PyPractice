import sqlite3

# this method will connect to the db
# When creating the db we are setting the types of each var
# id, year, isbn = int; title, author = text/string
def connect():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()

# this method will allow us to see the inventory
# returns the rows of the db
def view():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM BOOK")
    rows = cursor.fetchall()
    connection.close()
    return rows

# this method will insert to the db
# parameters to be inserting are title, author, year, isbn
def insert():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO book values (NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()
    view()

# this method will delete from the db
# deleting by id
def delete():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id))
    connection.commit()
    connection.close()

# this method will search through the db
# searching through all parameters
def search():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows = cursor.fetchall()
    connection.close()
    return rows


# this method will update a row in the db
# update whatever is needed
def update():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn))
    connection.commit()
    connection.close()


connect()