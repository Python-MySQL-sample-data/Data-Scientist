import psycopg2

def create_table():
    conn=psycopg2.connect("lite.db")  # if DB not exist will be created, else connectd to it
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")  # Pass as string
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("lite.db")  # if DB not exist will be created, else connectd to it
    cursor=conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

# insert("Wine Glass",8,10.5)
# insert("Water Glass",10,5.0)
# insert("Coffee cup",15,5.0)

def view():
    conn=psycopg2.connect("lite.db")  # if DB not exist will be created, else connectd to it
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("lite.db")  # if DB not exist will be created, else connectd to it
    cursor=conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("lite.db")  # if DB not exist will be created, else connectd to it
    cursor=conn.cursor()
    cursor.execute("UPDATE store SET quantity=?, price =? WHERE item =?",(quantity,price,item))
    conn.commit()
    conn.close()

# delete("Wine Glass")
update(50, 6,"Water Glass")
print(view())