from tkinter import *
import os
from PIL import ImageTk, Image
import sqlite3
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def login_success():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  screen3.configure(background="#1f3c88")
  screen3.iconbitmap("ICON vp.ico")
  Label(screen3, text = "Login Sucess", bg= "#1f3c88", fg="#fecd1a", font = ("calibri", 12,"bold")).pack()
  Button(screen3, text = "OK",bg="#fecd1a",fg="#1f3c88", command = login).pack()

def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("300x100")
  screen4.configure(background="#1f3c88")
  screen4.iconbitmap("ICON vp.ico")
  Label(screen4, text = "Login, failed, invalid username or password",  bg= "#1f3c88", fg="#fecd1a", font = ("calibri", 12, "bold") ).pack()
  Button(screen4, text = "OK",bg="#fecd1a",fg="#1f3c88", command =delete3).pack()

def register_user():
  print("working")

  username_info = username.get()
  password_info = password.get()
  emailid_info=emailid.get()
  conn = sqlite3.connect('Form.db')
  with conn:
       cursor=conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS Account (Username TEXT,Password TEXT,Emailid TEXT)')
  cursor.execute('INSERT INTO Account (Username,Password,Emailid) VALUES(?,?,?)',(username_info,password_info,emailid_info,))
  conn.commit()


  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,bg= "#1f3c88",font = ("calibri", 11)).pack()

def login_verify():

  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  conn= sqlite3.connect('form.db')
  c=conn.cursor()

  c.execute("SELECT * FROM Account WHERE Username =? AND Password =?",(username1, password1,))
  count=len(c.fetchall())
  if(count==1):
      login_success()
  else:
      password_not_recognised()

  c.close()
  conn.commit()
  conn.close()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Create Account - VIGNAN Healthcare")
  screen1.geometry("300x350")
  screen1.configure(background="#1f3c88")
  screen1.iconbitmap("ICON vp.ico")
  global username
  global password
  global emailid
  global username_entry
  global password_entry
  global emailid_entry
  username = StringVar()
  password = StringVar()
  emailid= StringVar()
  Label(screen1, text = "Please Enter Your Details below", width=300, bg = "#fecd1a",fg="#1f3c88",  font = ("Calibri",14, "bold")).pack()
  Label(screen1, text = "", bg= "#1f3c88", fg="#fecd1a").pack()
  Label(screen1, text = "Username * " , bg= "#1f3c88", fg="#fecd1a",  font = ("Calibri", 15, "bold")).pack()
  username_entry = Entry(screen1, textvariable = username ,  bg = "#d0e8f2",fg="brown",  font = ("Calibri", 15, "bold"))
  username_entry.pack()
  Label(screen1, text = "",  bg= "#1f3c88", fg="#fecd1a").pack()
  Label(screen1, text = "Email-ID * " , bg= "#1f3c88", fg="#fecd1a",  font = ("Calibri", 15, "bold")).pack()
  emailid_entry = Entry(screen1, textvariable = emailid ,  bg = "#d0e8f2",fg="brown",  font = ("Calibri", 15, "bold"))
  emailid_entry.pack()
  Label(screen1, text = "",  bg= "#1f3c88", fg="#fecd1a").pack()
  Label(screen1, text = "Password * " , bg= "#1f3c88", fg="#fecd1a",  font = ("Calibri", 15, "bold") ).pack()
  password_entry =  Entry(screen1, textvariable = password,  bg = "#d0e8f2",fg="brown",  font = ("Calibri", 15, "bold"))
  password_entry.pack()
  Label(screen1, text = "" ,  bg= "#1f3c88", fg="#fecd1a").pack()
  Button(screen1, text = "Register", width = 10, height = 1,bg="#fecd1a",fg="#1f3c88",font=("bold", 15), command = register_user).pack()


def login():

  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login - VIGNAN Healthcare")
  screen2.configure(background="#1f3c88")
  screen2.iconbitmap("ICON vp.ico")
  screen2.geometry("300x250")
  Label(screen2,text = "Please Enter Your Details To Login",width=300, bg = "#fecd1a",fg="#1f3c88",  font = ("Calibri",14, "bold") ).pack()
  Label(screen2, text = "", bg= "#1f3c88", fg="#fecd1a").pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  Label(screen2, text = "Username *", bg= "#1f3c88", fg="#fecd1a",  font = ("Calibri", 15, "bold")).pack()
  username_entry1 = Entry(screen2, textvariable = username_verify,  bg = "#d0e8f2",fg="brown",  font = ("Calibri", 15, "bold"))
  username_entry1.pack()
  Label(screen2, text = "",  bg= "#1f3c88", fg="#fecd1a").pack()
  Label(screen2, text = "Password * ", bg= "#1f3c88", fg="#fecd1a",  font = ("Calibri", 15, "bold")).pack()
  password_entry1 = Entry(screen2, textvariable = password_verify,  bg = "#d0e8f2",fg="brown",  font = ("Calibri", 15, "bold"))
  password_entry1.pack()
  Label(screen2, text = "",  bg= "#1f3c88", fg="#fecd1a").pack()
  Button(screen2, text = "Login", width = 10, height = 1,bg="#fecd1a",fg="#1f3c88",font=("bold", 15),  command = login_verify).pack()


def main_screen():
  global screen
  screen = Tk()
  screen.configure(background="#1f3c88")
  screen.geometry("700x400")
  screen.title("VIGNAN Smart Clinic - Patient Module")
  screen.iconbitmap("ICON vp.ico")
  left_frame = ImageTk.PhotoImage(Image.open("templete/smart.jpg"))
  image_frame = Label(image= left_frame)
  image_frame.place(x=0,y=0,width=700,height=400)
  Label(text = "Welcome to VIGNAN Smart Healthcare - Patient Care", bg = "#fecd1a",fg="#1f3c88", width = "300", height = "2", font = ("Calibri", 20, "bold")).pack()

  Button(screen, text = "Login", bg = "#fecd1a",fg="#1f3c88",height = "3", width = "20", font=("bold", 15),command = login).place(x=250, y=125)

  Button(text = "Register", bg="#fecd1a",fg="#1f3c88",height = "3", width = "20",font=("bold", 15), command = register).place(x=250, y= 275)

  screen.mainloop()

main_screen()
