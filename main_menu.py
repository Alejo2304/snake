import tkinter as tk
import ttkbootstrap as ttk

def login():
    pass

def register():
    pass

def guest():
    pass
        
#main window
window = ttk.Window(themename = 'darkly')
window.title('Snake Game')
window.geometry('500x300')

#title
title_label = ttk.Label(
    master = window,
    text = "Welcome to Snake Game!", 
    font = 'Calibri 24 bold')
title_label.pack()

#buttons
buttons_frame = ttk.Frame(master = window)

login_button = ttk.Button(master = buttons_frame, text = "Login", command = login)
login_button.pack()

register_button = ttk.Button(master = buttons_frame, text = 'Register', command = register)
register_button.pack()

guest_button = ttk.Button(master = buttons_frame, text= 'Play as Guest', command = guest)
guest_button.pack()

buttons_frame.pack(pady = 20)

#run
window.mainloop()
