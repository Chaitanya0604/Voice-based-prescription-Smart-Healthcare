import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


conn= sqlite3.connect('form.db')
c=conn.cursor()
c.execute("SELECT * FROM Student ")
r=c.fetchall()


win=Tk()
win.title("Viewing Patients Appointment")
win.geometry=("650 x 650")
win.resizable(False, False)

label= Label(win, text="Patient Records", font= "time 25 bold", bg="blue", fg="white")
label.grid(row=0, column=0, columnspan=20)

p1= Label(win, text="FullName", font= "time 15 bold")
p1.grid(row=1, column=0, padx=10, pady=10)

p2= Label(win, text="Email", font= "time 15 bold")
p2.grid(row=1, column=1, padx=10, pady=10)

p3= Label(win, text="Gender", font= "time 15 bold")
p3.grid(row=1, column=2, padx=10, pady=10)

p4= Label(win, text="Age", font= "time 15 bold")
p4.grid(row=1, column=3, padx=10, pady=10)

p5= Label(win, text="Symptoms", font= "time 15 bold")
p5.grid(row=1, column=4, padx=10, pady=10)

num=2
for i in r:
    name= Label(win, text=i[0], font= "time 12 bold")
    name.grid(row=num, column=0, padx=10, pady=10)

    email= Label(win, text=i[1], font= "time 12 bold")
    email.grid(row=num, column=1, padx=10, pady=10)

    gender= Label(win, text=i[2], font= "time 12 bold")
    gender.grid(row=num, column=2, padx=10, pady=10)

    age= Label(win, text=i[3], font= "time 12 bold")
    age.grid(row=num, column=3, padx=10, pady=10)

    symptoms= Label(win, text=i[4], font= "time 12 bold")
    symptoms.grid(row=num, column=4, padx=10, pady=10)

    num=num+1

    conn= sqlite3.connect('form.db')
    def delete_record():

        c=conn.cursor()
        #query= "DELETE FROM tasks WHERE name= '%s' " % name_entry.get()
        c.execute("DELETE FROM Student WHERE Fullname=ganesh"))

        conn.commit()

    delete_record()

c.close()
conn.commit()
conn.close()

win.mainloop()
