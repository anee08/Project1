# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:07:55 2020

@author: shrabanti
"""

import sqlite3


#BACKEND

def EmployeeData(): 
    con=sqlite3.connect("Employee.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Employee (id INTEGER PRIMARY KEY,Employeeid INTEGER, \
    Firstname TEXT,Lastname TEXT,Mobileno TEXT,Address TEXT, \
                Gender TEXT,BasicPay TEXT,OverTime TEXT,TotalLeave Integer,IssuedLeave Integer)")        
    con.commit()
    con.close()

def addEmployeeData(Employeeid,Firstname,Lastname,Mobileno,Address,Gender,BasicPay,OverTime,TotalLeave,IssuedLeave):
    con=sqlite3.connect("Employee.db")
    cur=con.cursor()
    cur.execute("INSERT INTO Employee VALUES(NULL,?,?,?,?,?,?,?,?,?,?)", \
                (Employeeid,Firstname,Lastname,Mobileno,Address,Gender,BasicPay,OverTime,TotalLeave,IssuedLeave))        
    con.commit()
    con.close()


def viewData():
    con=sqlite3.connect("Employee.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Employee")
    rows =cur.fetchall()
    con.close()
    return rows
    

def searchData(Employeeid="",Firstname="",Lastname="",Mobileno="",Address="",Gender="",BasicPay="",OverTime="",TotalLeave="",IssuedLeave=""):
    con=sqlite3.connect("Employee.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM Employee WHERE Employeeid=? OR Firstname= ? OR Lastname= ? OR Mobileno=? OR Address=? OR Gender=? OR BasicPay=? OR OverTime=? OR TotalLeave=? OR  IssuedLeave=?", (Employeeid,Firstname,Lastname,Mobileno,Address,Gender,BasicPay,OverTime,TotalLeave,IssuedLeave))
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    
    con=sqlite3.connect("Employee.db")
    cur=con.cursor()
    cur.execute("DELETE FROM Employee WHERE id = ?", (id,))
    #cur.execute("DELETE FROM Employee WHERE id = ?", (id,))
    #rows =cur.fetchall()
    con.commit()
    #con.close()
    
    #return rows



def DataUpdate(Employeeid="",Firstname="",Lastname="",Mobileno="",Address="",Gender="",BasicPay="",OverTime="",TotalLeave="",IssuedLeave=""):     
    con=sqlite3.connect("Employee.db")
    cur=con.cursor()
    cur.execute("Update Employee set Employeeid=? , Firstname= ? , Lastname= ? , Mobileno=? , Address=? , Gender=? , BasicPay=? , OverTime=? , TotalLeave=? , IssuedLeave=?", (Employeeid,Firstname,Lastname,Mobileno,Address,Gender,BasicPay,OverTime,TotalLeave,IssuedLeave,id))
    con.commit()
    con.close()

EmployeeData()

    
