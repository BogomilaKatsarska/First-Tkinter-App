import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

label = ttk.Label(root, text="Hello, world!", padding=20)
label.config(font=("Segoe UI", 20))
label.pack()

image = Image.open("Python.svg.png").resize((64, 64))
photo = ImageTk.PhotoImage(image)
label2 = ttk.Label(root, text="Image with text", image=photo, padding=5, compound="right")
label2.pack()

# label["image"] = photo

greeting = tk.StringVar()
label3 = ttk.Label(root, padding=10, textvariable=greeting)
label3.pack()

greeting.set("Hello, John!")
root.mainloop()