import sqlite3

#Query the database and return all records
def show_all():
    conn = sqlite3.connect('customers.db')
    curr = conn.cursor()
    
    curr.execute("SELECT rowid, * FROM customers")
    items = curr.fetchall()
    for item in items:
        print(item)
    
    conn.commit()
    conn.close()

#Add a new record to the table
def add_one(first,last,email):
    conn = sqlite3.connect('customers.db')
    curr = conn.cursor()

    curr.execute("INSERT INTO customers VALUES(?,?,?)", (first,last,email))
    
    conn.commit()
    conn.close()

#Delete a record from table
def delete_one(id):
    conn = sqlite3.connect('customers.db')
    curr = conn.cursor()

    curr.execute("DELETE FROM customers WHERE rowid = (?)", id)
    
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('customers.db')
    curr = conn.cursor()

    curr.executemany("INSERT INTO customers VALUES(?,?,?)", (list))
    
    conn.commit()
    conn.close()

#Lookup with where
def email_lookup(email):
    conn = sqlite3.connect('customers.db')
    curr = conn.cursor()

    curr.execute("SELECT rowid,* FROM customers WHERE email =(?)", (email,))
    
    items = curr.fetchall()
    for item in items:
        print(item)
    
    conn.commit()
    conn.close()







