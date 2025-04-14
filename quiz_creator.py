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

# Answers box
answer_boxes = {}
y = 130
letters = ["a", "b", "c", "d"]
for index, letter in enumerate(letters): # makes a label and corresponding text box for letters a-d
    letter_label = tk.Label(
        root,
        text=f"Answer {letter}.)",
        background="white",
        foreground="black",
        relief= "solid",
        width=40
    )

    letter_label.grid(
        row=index,
        column=1,
        padx=10,
        pady=5,
        sticky="w"
    )

    letter_text_box = tk.Text(root, width= 20, height= 2)
    letter_text_box.grid(
        row=index,
        column=2,
        padx=10,
        pady=5,
        sticky="w"
    )

    answer_boxes[letter] = letter_text_box #determine which typed answer in box corresponds with what letter


# integrate code from reference


# initiate gui
root.mainloop()