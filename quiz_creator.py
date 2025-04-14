# using tkinter create a working gui
import tkinter as tk
from tkinter import messagebox

# window
root = tk.Tk()
root.title("Quiz Creator")
root.geometry("1366x768")
root.resizable(False, False)
root.config(background="pink")

# Elements
# Question box
question_label = tk.Label(
    root,
    text="QUESTION",
    background="pink",
    foreground="black",
    font=("Times New Roman", 20, "bold")
)

question_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="w"
)

question_box = tk.Text(
    root,
    height=25,
    width=80,
    font=("Times New Roman", 15, "bold")
)
question_box.grid(
    row=1,
    column=0,
    padx=10,
    pady=0,
)

# integrate code from reference


# initiate gui
root.mainloop()