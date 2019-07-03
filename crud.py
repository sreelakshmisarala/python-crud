#!/usr/bin/env python
# Import MySQLdb
import MySQLdb as mdb
import sys

# CREATE A NEW TABLE and INSERT SOME VALUES
def createTable(con):
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS TableTest")
        cur.execute("CREATE TABLE TableTest(Id INT PRIMARY KEY AUTO_INCREMENT, \
            Name VARCHAR(25))")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Midhun')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Sreelakshmi')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Manu')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Shadow')")
        cur.execute("INSERT INTO TableTest(Name) VALUES('Lucifer')")

# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM TableTest")
        rows = cur.fetchall()
        for row in rows:
            print row["Id"], row["Name"]

# UPDATE ROW
def updateRow(con):
    with con:
        cur = con.cursor()
        cur.execute("UPDATE TableTest SET Name = %s WHERE Id = %s",
            ("Malu", "4"))
        print "Number of rows updated:",  cur.rowcount

# DELETE ROW
def deleteRow(con):
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM TableTest WHERE Id = %s", "2")
        print "Number of rows deleted:", cur.rowcount

# SET UP THE CONNECTION
try:
    con = mdb.connect('localhost', 'root', 'password', 'pycrud');
    cur = con.cursor()

    # CRUD OPERATIONS
    createTable(con)
    updateRow(con)
    deleteRow(con)
    retrieveTable(con)
    

except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()