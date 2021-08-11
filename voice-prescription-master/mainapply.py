import tkinter as tk


window = tk.Tk()
window.state=("zoomed")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1= tk.Frame(window)
frame2= tk.Frame(window)
frame3=tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()


frame1_title=tk.Label(frame1, text="This is frame 1")
frame1_title.pack(fill='x')

frame1_btn=tk.Button(frame1, text="frame1",command=lambda: show_frame(frame1))
frame1_btn.pack()

frame2_title=tk.Label(frame2, text="This is frame 2")
frame2_title.pack(fill='x')

frame2_btn=tk.Button(frame2, text="grame2",command=lambda: show_frame(frame1))
frame2_btn.pack()

frame3_title=tk.Label(frame3, text="This is frame 3")
frame3_title.pack(fill='x')

frame3_btn=tk.Button(frame3, text="grame3",command=lambda: show_frame(frame1))
frame3_btn.pack()

show_frame(frame1)


window.mainloop()
