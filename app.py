import tkinter as tk
from tkinter import ttk #buttons and labels that are themable - i.e. can be adjusted


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk() #creating the main window
# root.geometry('600x400') #make the window with fixed size - px

# ttk.Label(root, text='Hello, World!', padding=(30, 10)).pack() #pack yourself into the parent
user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0)) # LEFT -> TOP -> RIGHT -> BOTTOM
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text='Name: ')
name_label.pack(side='left', padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name) #The width property is not in pixels, but in 'number of characters' that the field should be able to accomodate
name_entry.pack(side='left')
name_entry.focus() #focus is used to start typing straight away

buttons = ttk.Frame(root, padding=(20, 10)) #LEFT and RIGHT
buttons.pack(fill="both")
greet_button = ttk.Button(buttons, text='Greet', command=greet)
greet_button.pack(side='left', fill="x", expand=True) #side='top' by default

quit_button = ttk.Button(buttons, text='Quit', command=root.destroy) #destroy ends the process
quit_button.pack(side='right', fill="x", expand=True)#(side='left', fill='x', expand=True) #fill='y' we take all the vertical space that has been reserved for it (fill: x, y, both)

root.mainloop()