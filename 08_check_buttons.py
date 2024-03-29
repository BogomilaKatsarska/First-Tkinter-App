import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

# check_button = ttk.Checkbutton(root, text='Check me!')
# check_button.pack()
#
# check_button['state'] = "disabled"

selected_option = tk.StringVar()


def print_current_option():
    print(selected_option.get())


check = ttk.Checkbutton(
    root,
    text="Check Exampe",
    variable=selected_option,
    command=print_current_option,
    onvalue='On',
    offvalue='Off'
)

check.pack()
root.mainloop()