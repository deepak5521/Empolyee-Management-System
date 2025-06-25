#!/usr/bin/env python
# coding: utf-8

# # GUI

# In[28]:


#import mysql.connector
#conn=mysql.connector.connect(user='root',password='root',host='localhost')
#qur='create database emp_db'
#mycur=conn.cursor()
#mycur.execute(qur)
#mycur.close()
#conn.close()


# In[30]:


import mysql.connector
conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
qur='create table emp_table(name varchar(40),mobno varchar(40),dept varchar(40),salary varchar(40))'
mycur=conn.cursor()
mycur.execute(qur)
mycur.close()
conn.close()


# In[1]:


import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
win=Tk()

win.title('EMPLOYEE MANAGEMENT SYSTEM')
win.geometry('800x600')
win.configure(bg='skyblue')

def show():
    conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
    qur='select * from emp_table'
    mycur=conn.cursor()
    mycur.execute(qur)
    list1=mycur.fetchall()
    for i in list1:
        treev.insert('',0,values=(i[0],i[1],i[2],i[3]))
    mycur.close()
    conn.close()
    


def add():
    name=n1.get()
    mobno=m1.get()
    dept=d1.get()
    salary=s1.get()
    if name==''or mobno==''or dept=='' or salary=='':
        messagebox.showinfo('info','All field are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
        qur=f'insert into emp_table values("{name}","{mobno}","{dept}","{salary}")'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is added successfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')






def salary():
    root=Tk()
    root.title('Salary management')
    root.configure(bg='cyan')
    root.geometry('600x400')
    def disp():
        x=e9.get()
        conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
        qur=f'select salary from emp_table where name="{x}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        mycur.fetchone()
        l10.config(text=salary[0]+'RS')
        mycur.close()
        conn.close()


    l1=Label(root,text='Name of Employee')
    l1.place(x=100,y=40)
    var3=StringVar()
    e9=Entry(root,textvariable=var3)
    e9.place(x=220,y=40)
    b9=Button(root,text='show salary',width=15,command=disp)
    b9.place(x=220,y=80)
    
    l10=Label(root,text='salary is here',height=5,width=20)
    l10.place(x=100,y=100)

    root.mainloop()

def delete():
    name=var1.get()
    if name=='':
        messagebox.showinfo('info','All field are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
        qur=f'delete from emp_table where name="{name}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is deleted successfully')
        var1.set('')
        
def select():
    name=var2.get()
    if name=='':
        messagebox.showinfo('info','All field are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
        qur=f'select * from emp_table where name="{name}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        result=mycur.fetchone()
        e1.insert(0,result[0])
        e2.insert(0,result[1])
        e3.insert(0,result[2])
        e4.insert(0,result[3])
        mycur.close()
        conn.close()
        
def update():
    name=n1.get()
    mobno=m1.get()
    dept=d1.get()
    salary=s1.get()
    if name==''or mobno==''or dept=='' or salary=='':
        messagebox.showinfo('info','All field are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='root',host='localhost',database='emp_db')
        qur=f'update emp_table set mobno="{mobno}",dept="{dept}",salary="{salary}"where name="{name}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is updated successfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
    

def clear():
    treev.delete(*treev.get_children())
    
    
    
# main label

l0=Label(win,text='EMPLOYEE MANAGEMENT SYSTEM',bg='white',fg='black',bd=5,width=40,relief='ridge',
         font=('times new roman',18,'bold'))
l0.place(x=300,y=40)

# name label and entry

l1=Label(win,text='EMPLOYEE NAME',bg='white',fg='black',bd=5,relief='ridge',width=25,font=('times new roman',12,'bold'))
l1.place(x=100,y=120)

n1=StringVar()
e1=Entry(win,textvariable=n1,bg='white',fg='black',bd=5,relief='ridge',width=40,font=('times new roman',12,'bold'))
e1.place(x=360,y=120)

# mobile no Label and entry

l2=Label(win,text='MOBILE NO',bg='white',fg='black',bd=5,relief='ridge',width=25,font=('times new roman',12,'bold'))
l2.place(x=100,y=160)

m1=StringVar()
e2=Entry(win,textvariable=m1,bg='white',fg='black',bd=5,relief='ridge',width=40,font=('times new roman',12,'bold'))
e2.place(x=360,y=160)

# department and entry 

l3=Label(win,text='DEPARTMENT',bg='white',fg='black',bd=5,relief='ridge',width=25,font=('times new roman',12,'bold'))
l3.place(x=100,y=200)

d1=StringVar()
e3=Entry(win,textvariable=d1,bg='white',fg='black',bd=5,relief='ridge',width=40,font=('times new roman',12,'bold'))
e3.place(x=360,y=200)

# salary label and entry


l4=Label(win,text='SALARY',bg='white',fg='black',bd=5,relief='ridge',width=25,font=('times new roman',12,'bold'))
l4.place(x=100,y=240)

s1=StringVar()
e4=Entry(win,textvariable=s1,bg='white',fg='black',bd=5,relief='ridge',width=40,font=('times new roman',12,'bold'))
e4.place(x=360,y=240)

# four buttons
# add,exit,show,salary


b1=Button(win,text='SHOW',width=20,command=show)
b1.place(x=180,y=320)


b2=Button(win,text='ADD',width=20,command=add)
b2.place(x=420,y=320)


b3=Button(win,text='EXIT',width=20,command=win.destroy)
b3.place(x=180,y=360)


b4=Button(win,text='SALARY',width=20,command=salary)
b4.place(x=420,y=360)

# delete
#  label entry button

l5=Label(win,text='ENTER NAME>>',bg='white',fg='black',bd=5,relief='ridge',width=25,font=('times new roman',12,'bold'))
l5.place(x=100,y=440)

var1=StringVar()
e5=Entry(win,textvariable=var1,bg='white',fg='black',bd=5,relief='ridge',width=40,font=('times new roman',12,'bold'))
e5.place(x=360,y=440)

b5=Button(win,text='DELETE',width=20,command=delete)
b5.place(x=360,y=480)

# update
# label entry select update

l6=Label(win,text='ENTER NAME>>',bg='white',fg='black',bd=5,relief='ridge',width=25,font=('times new roman',12,'bold'))
l6.place(x=100,y=520)

var2=StringVar()
e6=Entry(win,textvariable=var2,bg='white',fg='black',bd=5,relief='ridge',width=40,font=('times new roman',12,'bold'))
e6.place(x=360,y=520)

b6=Button(win,text='SELECT',width=20,command=select)
b6.place(x=250,y=560)

b7=Button(win,text='UPDATE',width=20,command=update)
b7.place(x=400,y=560)

# Tree view

treev=ttk.Treeview(win,height=23)
treev.place(x=800,y=100,width=530)

treev["columns"]=("1","2","3","4")
treev['show']='headings'

treev.column("1",width=90,anchor='c')
treev.column("2",width=90,anchor='se')
treev.column("3",width=90,anchor='se')
treev.column("4",width=90,anchor='se')

treev.heading("1",text="NAME")
treev.heading("2",text="MOBILE NO")
treev.heading("3",text="DEPT")
treev.heading("4",text="SALARY")


b8=Button(win,text='CLEAR',width=20,command=clear)
b8.place(x=1000,y=590)

win.mainloop()


# In[ ]:





# In[ ]:




