import sqlite3
import sys

def printDB():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address,"
                                   "Salary, HireDate FROM Employees")
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")
    except:
        print("Couldn't Retreive The DataBase")

db_conn = sqlite3.connect('test.db')
print("Database Created")
theCursor = db_conn.cursor()
db_conn.execute("DROP TABLE IF EXISTS Employees")
try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT "
                "NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table Couldn't Be Created")

print("Table Created")
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary,"
                "HireDate) VALUES ('Derek', 'Banas', 41, '123 Main St', 500000, date('now'))")
db_conn.commit()
printDB()
try:
    db_conn.execute("UPDATE Employees SET Address = '121 Main St' WHERE ID=1")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table Couldn't Be Updated")
print()
printDB()
try:
    db_conn.execute("DELETE FROM Employees Where ID=1")
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table Couldn't Be Updated")
print()
printDB()
db_conn.close()
print("Database Closed")