import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO books VALUES(NULL, ?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()



# testing before connecting to frontend
connect()
# insert("time machine","Wells",1890,1234567890)
# update(1,"Moby Dick", "Melvile", 1930,1234567788)
# print(view())