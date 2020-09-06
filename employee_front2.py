
from tkinter import *
#from tkinter import ttk
#import random
import tkinter.messagebox
#import datetime
#import time
#import tempfile,os
import EmployeeDatabase



class Employee:
    
    def __init__(self,root):
        
        self.root = root
        self.root.title("HR Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(bg="gainsboro")
       
        TopFrame1 =Frame(self.root, bd =7, width=1340,height=50,relief=RIDGE)
        TopFrame1.grid(row=2,column=0)
        
        TopFrame2 =Frame(self.root, bd =7, width=1340,height=100,relief=RIDGE)
        TopFrame2.grid(row=1,column=0)
        
        TopFrame3 =Frame(self.root, bd =7, width=1340,height=500,relief=RIDGE)
        TopFrame3.grid(row=0,column=0)
        
        LeftFrame = Frame(TopFrame3,bd=5 ,width=1340, height=400, padx=2 ,bg="gainsboro",relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame,bd=5 ,width=600, height=180, padx=2, pady=4 ,bg="gainsboro",relief=RIDGE)
        LeftFrame1.pack(side=TOP)
        
        LeftFrame2 = Frame(LeftFrame, bd=5 ,width=600, height=180, padx=2 ,bg="gainsboro",relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        LeftFrame2Left = Frame(LeftFrame2,bd=5 ,width=300, height=170, padx=2,bg="gainsboro",relief=RIDGE)
        LeftFrame2Left.pack(side=LEFT)
        
        
        LeftFrame2Right= Frame(LeftFrame2,bd=5 ,width=300, height=170, padx=2,bg="gainsboro",relief=RIDGE)
        LeftFrame2Right.pack(side=RIGHT)
        
       

        
        #=================================functions===================================================================

        def addData():
            if(len(Employeeid.get())!=0):
                EmployeeDatabase.addEmployeeData(Employeeid.get(),Firstname.get(),Lastname.get(),Mobileno.get(),Address.get(),Gender.get(),BasicPay.get(),OverTime.get(),TotalLeave.get(),IssuedLeave.get())
                lstEmployee.delete(0,END)
                lstEmployee.insert(END,Employeeid.get(),Firstname.get(),Lastname.get(),Mobileno.get(),Address.get(),Gender.get(),BasicPay.get(),OverTime.get(),TotalLeave.get(),IssuedLeave.get())
                Reset()
                
        
        def DisplayData():     #working.....
            lstEmployee.delete(0,END)
            for row in EmployeeDatabase.viewData():
                lstEmployee.insert(END,row,str(""))



        def EmployeeRec(event):                                                                                                                                                                                                                                                                                                                                                                                                             

            global Ed
            searchEd= lstEmployee.curselection()[0]
            Ed=lstEmployee.get(searchEd)

            self.txtEmployeeid.delete(0,END)
            self.txtEmployeeid.insert(END,Ed[1])                                 
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,Ed[2])                                 
            self.txtLastname.delete(0,END)
            self.txtLastname.insert(END,Ed[3])                                 
            self.txtMobileno.delete(0,END)
            self.txtMobileno.insert(END,Ed[4])                                 
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,Ed[5])                                 
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,Ed[6])
            self.txtBasicPay.delete(0,END)
            self.txtBasicPay.insert(END,Ed[7])
            self.txtOverTime.delete(0,END)
            self.txtOverTime.insert(END,Ed[8])
            self.txtTotalLeave.delete(0,END)
            self.txtTotalLeave.insert(END,Ed[9])
            self.txtIssuedLeave.delete(0,END)
            self.txtIssuedLeave.insert(END,Ed[10])
             

        def DeleteData():
            #global Ed
           
            #deleting from list box      working...
            searchEd= lstEmployee.curselection()[0]
           # print(searchEd)
            #lstEmployee.delete(searchEd[0])
            #deleting from database     not working...
            v=lstEmployee.get(searchEd)
            EmployeeDatabase.deleteRec(v[0])
            #Reset()
            DisplayData()

        def update():
            if(len(Employeeid.get())!=0):
                EmployeeDatabase.deleteRec(Ed[0])
            if(len(Employeeid.get())!=0):
                EmployeeDatabase.addEmployeeData(Employeeid.get(),Firstname.get(),Lastname.get(),Mobileno.get(),Address.get(),Gender.get(),BasicPay.get(),OverTime.get(),TotalLeave.get(),IssuedLeave.get())
                lstEmployee.delete(0,END)
                lstEmployee.insert(END,Employeeid.get(),Firstname.get(),Lastname.get(),Mobileno.get(),Address.get(),Gender.get(),BasicPay.get(),OverTime.get(),TotalLeave.get(),IssuedLeave.get())

        def  Reset():     #working.....
            Firstname.set("")
            Lastname.set("")
            Employeeid.set("")
            Mobileno.set("")
            Address.set("")
            Gender.set("")
            BasicPay.set("")
            OverTime.set("")
            GrossPay.set("")
            NetPay.set("")
            PayDay.set("")
            TotalLeave.set("")
            IssuedLeave.set("")
            RemainingLeave.set("")
            GenerateLeave.set("")
            lstEmployee.delete(0,END)
            BasicPay.set("0.00")
            TotalLeave.set("0.00")
            self.txtReceipt.delete("1.0",END)


        def Quit():       #working.....
            Quit = tkinter.messagebox.askyesno("HR MANAGEMENT SYSTEM","confirm if you want exit")
            if Quit > 0:
                root.destroy()
                return

       
        def Generateleave():
            global Ed
            searchEd= lstEmployee.curselection()
            lstEmployee.viewleave(searchEd[0])
            if (RemainingLeave!=0):
                Il=IssuedLeave.get()
                Il+=1
                RemainingLeave.set(24-Il)

         #=================================variables==========================================================
        global Ed
        Firstname = StringVar()
        Lastname = StringVar()
        Employeeid = StringVar()
        Mobileno = StringVar()
        Address = StringVar()
        Gender = StringVar()
        BasicPay = IntVar()
        OverTime = StringVar()
        GrossPay = StringVar()
        NetPay = StringVar()
        PayDay = StringVar()
        TotalLeave = IntVar()
        IssuedLeave=IntVar()
        RemainingLeave = IntVar()
        GenerateLeave = IntVar()
        Add= StringVar()
        
        
        BasicPay.set("0.00")
        TotalLeave.set("24.00")
        
        
        #====================================================================================================
        self.lblLabel = Label(TopFrame2, font=('arial',10,'bold'),padx=6,pady=2,text = "Employeeid\tFirstName\tSurName\tAddress\t\tGender\t\tMobileNo\t\tBasicPay\tOvertime\tNetPay")
        self.lblLabel.grid(row=0, column=0,columnspan=17)
        
        
        #===============================================listbox and scrollbar=====================================================
        
        scrollbar = Scrollbar(TopFrame2)
        scrollbar.grid(row=1, column=1, sticky='ns')
        
        lstEmployee = Listbox(TopFrame2,width=145,height=5,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        lstEmployee.bind('<<listboxselect>>',EmployeeRec)
        lstEmployee.grid(row=1,column=0,padx=1,sticky='nsew')
        scrollbar.config(command = lstEmployee.yview)
        #========================================widget========================================
        
        self.lblEmployeeid = Label(LeftFrame1,font=('arial',12,'bold'),text = 'Employeeid',bd=7,bg='gainsboro',anchor='w')
        self.lblEmployeeid.grid(row=0,column=0,sticky='w',padx=5)
        self.txtEmployeeid = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Employeeid)
        self.txtEmployeeid.grid(row=0,column=1)
        
        self.lblFirstname = Label(LeftFrame1,font=('arial',12,'bold'),text = 'Firstname',bd=7,bg='gainsboro',anchor='w')
        self.lblFirstname.grid(row=1,column=0,sticky='w',padx=5)
        self.txtFirstname = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)
        
        self.lblLastname = Label(LeftFrame1,font=('arial',12,'bold'),text = 'Lastname',bd=7,bg='gainsboro',anchor='w')
        self.lblLastname.grid(row=2,column=0,sticky='w',padx=5)
        self.txtLastname = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Lastname)
        self.txtLastname.grid(row=2,column=1)
        
        self.lblAddress = Label(LeftFrame1,font=('arial',12,'bold'),text = 'Address',bd=7,bg='gainsboro',anchor='w')
        self.lblAddress.grid(row=3,column=0,sticky='w',padx=5)
        self.txtAddress = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Address)
        self.txtAddress.grid(row=3,column=1)
        
        self.lblGender = Label(LeftFrame1,font=('arial',12,'bold'),text = 'Gender',bd=7,bg='gainsboro',anchor='w')
        self.lblGender.grid(row=4,column=0,sticky='w',padx=5)
        self.txtGender = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Gender)
        self.txtGender.grid(row=4,column=1)
        
        
        self.lblMobileno = Label(LeftFrame1,font=('arial',12,'bold'),text = 'Mobileno',bd=7,bg='gainsboro',anchor='w')
        self.lblMobileno.grid(row=5,column=0,sticky='w',padx=5)
        self.txtMobileno = Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=60, justify='left',textvariable=Mobileno)
        self.txtMobileno.grid(row=5,column=1)
        #===========================================================================================================================
        
        self.lblBasicPay = Label(LeftFrame2Left,font=('arial',12,'bold'),text = 'BasicPay',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblBasicPay.grid(row=0,column=0,sticky='w')
        self.txtBasicPay = Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=BasicPay)
        self.txtBasicPay.grid(row=0,column=1)
        
        self.lblOverTime = Label(LeftFrame2Left,font=('arial',12,'bold'),text = 'OverTime',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblOverTime.grid(row=1,column=0,sticky='w')
        self.txtOverTime = Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=OverTime)
        self.txtOverTime.grid(row=1,column=1)
        
        self.lblNetPay = Label(LeftFrame2Left,font=('arial',12,'bold'),text = 'NetPay',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblNetPay.grid(row=2,column=0,sticky='w')
        self.txtNetPay = Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=NetPay)
        self.txtNetPay.grid(row=2,column=1) 
        
        self.lblPayDay = Label(LeftFrame2Left,font=('arial',12,'bold'),text = 'PayDay',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblPayDay.grid(row=3,column=0,sticky='w')
        self.txtPayDay = Entry(LeftFrame2Left,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=PayDay)
        self.txtPayDay.grid(row=3,column=1) 
        #=======================================================================================================
        self.lblTotalLeave = Label(LeftFrame2Right,font=('arial',12,'bold'),text = 'TotalLeave',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblTotalLeave.grid(row=0,column=0,sticky='w')
        self.txtTotalLeave = Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=TotalLeave)
        self.txtTotalLeave.grid(row=0,column=1)
        
        self.lblIssuedLeave = Label(LeftFrame2Right,font=('arial',12,'bold'),text = 'IssuedLeave',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblIssuedLeave.grid(row=1,column=0,sticky='w')
        self.txtIssuedLeave = Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=IssuedLeave)
        self.txtIssuedLeave.grid(row=1,column=1)
        
        self.lblRemainingLeave = Label(LeftFrame2Right,font=('arial',12,'bold'),text = 'RemainingLeave',bd=7,bg='gainsboro',anchor='w',justify='left')
        self.lblRemainingLeave.grid(row=2,column=0,sticky='w')
        self.txtRemainingLeave = Entry(LeftFrame2Right,font=('arial',12,'bold'),bd=5,width=20, justify='left',textvariable=RemainingLeave)
        self.txtRemainingLeave.grid(row=2,column=1)
        
        self.btnGenerateLeave = Button(LeftFrame2Right,pady=1, bd=3, fg='black', font=('arial',16,'bold'),padx=24, width=8,text='GenerateLeave',command=Generateleave).grid(row=1, column=4, padx=1)
        
        
        #==================================================================================================================================
        self.btnAdd = Button(TopFrame1,pady=1, bd=3, fg='black', font=('arial',16,'bold'),padx=24, width=3,text='Add',command=addData).grid(row=0, column=0, padx=1)
        
        self.btnDisplay = Button(TopFrame1,pady=1, bd=3, fg='black', font=('arial',16,'bold'),padx=24, width=3,text='Display',command=DisplayData).grid(row=0, column=1, padx=1)
        
        #self.btnUpdate = Button(TopFrame1,pady=1, bd=4, fg='black', font=('arial',16,'bold'),padx=24, width=3,text='Update',command=update).grid(row=0, column=2, padx=1)
        
        self.btnDelete = Button(TopFrame1,pady=1, bd=4, fg='black', font=('arial',16,'bold'),padx=24, width=3,text='Delete',command=DeleteData).grid(row=0, column=3, padx=1)
        
            
        self.btnReset = Button(TopFrame1,pady=1, bd=4, fg='black', font=('arial',16,'bold'),padx=24, width=3,text='Reset',command=Reset).grid(row=0, column=5, padx=1)
        
        self.btnExit = Button(TopFrame1,pady=1, bd=4, fg='black', font=('arial',16,'bold'),padx=24, width=3,text='Exit',command=Quit).grid(row=0, column=6, padx=1)
        
       # self.btnsearch = Button(TopFrame1,pady=1, bd=4, fg='black', font=('arial',16,'bold'),padx=24, width=10,text='Search Employee',command=EmployeeRec).grid(row=0, column=7, padx=1)

        
        
        
        
      
if __name__=='__main__':
    root = Tk()
    application = Employee(root)
    root.mainloop()        
       
