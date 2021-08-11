from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3
import sqlite3
import tkinter as tk
from tkinter import messagebox


root = Tk()
root.geometry('1200x550')
root.title("Patient Appointment Form")
root.configure(background="#1f3c88")
root.iconbitmap("ICON vp.ico")

Fullname=StringVar()
Email=StringVar()
Gender = StringVar()
Age=StringVar()
Symptoms= StringVar()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()

left_frame = ImageTk.PhotoImage(Image.open("templete/patient-12.jpg"))
image_frame = Label(image= left_frame)
image_frame.place(x=0,y=0,width=350,height=550)

def database():
    messagebox.showinfo('Online consultation','Consultation with doctor is successful')

    name1=Fullname.get()
    email=Email.get()
    gender=Gender.get()
    age=Age.get()
    symptoms=Symptoms.get()
    conn = sqlite3.connect('Form.db')
    with conn:
         cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Patient (Fullname TEXT,Email TEXT,Gender TEXT,Age TEXT,Symptoms TEXT)')
    cursor.execute('INSERT INTO Patient (FullName,Email,Gender,Age,Symptoms) VALUES(?,?,?,?,?)',(name1,email,gender,age,symptoms,))
    conn.commit()

    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()

label_0 = Label(root, text="Online Consultation",width=20,font=("bold", 20))
label_0.place(x=410,y=53)

def name():
        with sr.Microphone() as source:

                speak("patient\'s name")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        entry_1.insert(0,t1)
                        pr.name(name_entry.get())
                except:
                        speak(' could not recognize ')
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=380,y=130)

entry_1 = Entry(root, width=50, textvar=Fullname)
entry_1.place(x=620,y=130)
Button(root, text='Name',width=15,bg='lightgreen',fg='brown',command=name).place(x=950,y=125)

def email():
        with sr.Microphone() as source:

                speak("Please say your e-mail id")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        entry_2.insert(0,t1)
                        pr.name(name_entry.get())
                except:
                        speak(' could not recognize ')


label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=380,y=180)

entry_2 = Entry(root, width=50, textvar=Email)
entry_2.place(x=620,y=180)
Button(root, text='Email-id',width=15,bg='lightgreen',fg='brown', command=email).place(x=950,y=175)

def gender():
        with sr.Microphone() as source:

                speak("Your Gender")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        entry_3.insert(0,t1)
                        pr.name(name_entry.get())
                except:
                        speak(' could not recognize ')

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=380,y=230)
entry_3 = Entry(root, width=50, textvar=Gender)
entry_3.place(x=620,y=230)
Button(root, text='Gender',width=15,bg='lightgreen',fg='brown', command=gender).place(x=950,y=225)

def age():
        with sr.Microphone() as source:

                speak("Please mention your age")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        entry_4.insert(0,t1)
                        pr.name(name_entry.get())
                except:
                        speak(' could not recognize ')

label_4 = Label(root, text="Age",width=20,font=("bold", 10))
label_4.place(x=380,y=280)

entry_4 =Entry(root, width=50, textvar=Age)
entry_4.place(x=620,y=280)
Button(root, text='Age',width=15,bg='lightgreen',fg='brown',command=age).place(x=950,y=275)

def symptoms():
        with sr.Microphone() as source:

                speak("Please mention your age")
                try:
                        r.adjust_for_ambient_noise(source,duration=0.7)
                        audio= r.listen(source)
                        t1 = r.recognize_google(audio)
                        entry_5.insert(0,t1)
                        pr.name(name_entry.get())
                except:
                        speak(' could not recognize ')
label_5 = Label(root, text="Symptoms",width=20,font=("bold", 10))
label_5.place(x=380,y=330)

entry_5 =Entry(root, width= 50, textvar=Symptoms)
entry_5.place(x=620,y=330)
Button(root, text='Symptoms',width=15,bg='lightgreen',fg='brown',command=symptoms).place(x=950,y=325)

Button(root, text='Submit',width=20,bg='brown',fg='white', command=database).place(x=680,y=380)


root.mainloop()
