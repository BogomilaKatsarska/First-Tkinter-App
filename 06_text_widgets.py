import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=8) #  8rows
text.pack()

text.insert("1.0", "Please enter a comment...") #1.0 - the position in which you want to insert the text(1st line, 0 char)
# text["state"] = "disabled" #"normal" is by default

text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()