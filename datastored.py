import sqlite3
#create a database
conn = sqlite3.connect('customers.db')
#create a cursor
curr = conn.cursor()
#adding data
#many_customer = [
 #                 ('Silq','tech','silq@gmail.com'),
  #               ('Java','old','old@yahoo.com'),
   #             ('Rust','new','enw@protonmail.com')
#]


#curr.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)


#create a table
#curr.execute("""CREATE TABLE customers(
 #   first_name text,
  #  last_name text,
   # email text
    #) 
#""")

#curr.execute("CREATE TABLE customers( first_name DATATYPE, last_name DATATYPE, email DATATYPE )") U HAVE TO WRITE IN ONE LINE

#query the database
#curr.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")

#print(curr.fetchone()[0])
#curr.fetchmany(3)
#print(curr.fetchall())#in order to print we need to wrap it

#print("NAME"+"\tEMAIL")
#print("-----"+"\t------")

#print("Command exectued successfully.....")

#updating databaes
#curr.execute("""UPDATE customers SET first_name = 'pink'
 #               WHERE rowid = 1
#""")


#deleting databases
#curr.execute("DELETE from customers WHERE rowid = 2")

#query database-ORDER BY
#curr.execute("SELECT rowid, * FROM customers ORDER BY last_name")
#query database-AND/OR
#curr.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'ne%' OR email LIKE '%gmail.com'")
#query database-LIMIT
#curr.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

#drop a table
#curr.execute("DROP TABLE customers")



conn.commit()

curr.execute("SELECT rowid, * FROM customers")
items = curr.fetchall()
for item in items:
    print(item)



#commit our command
conn.commit()
#close the connection

conn.close()

