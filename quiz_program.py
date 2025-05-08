# use tkinter to make gui for quiz
import tkinter as tk

# quiz window
root = tk.Tk()
root.title("Quiz Program")
root.geometry("1690x900")
root.resizable(False, False)
root.config(background="pink")

# Elements
# question box
question_label = tk.Label(
    root,
    text="Question Here",
    font=("Times New Roman", 20, "bold"),
    bg="white",
    fg="black",
    wraplength=600,
    justify="center",
    relief="solid",
    width=90,
    height=9
)
question_label.pack(pady=20)

# answer buttons and text areas
answer_frame = tk.Frame(root, bg="pink")
answer_frame.pack()

answer_buttons = {}
for index, letter_key in enumerate(["a", "b", "c", "d"]):
    letter_buttons = tk.Button(
        answer_frame,
        text=f"{letter_key.upper()}",
        font=("Times New Roman", 15, "bold"),
        bg="green",
        fg="black",
        width=5,
        relief="solid"
    )

    letter_buttons.grid(
        row=index,
        column=0,
        padx=10,
        pady=40
    )

    answer_text = tk.Label(
        answer_frame,
        text="Given Here",
        font=("Times New Roman", 15),
        bg="pink",
        fg="black"
    )
    answer_text.grid(
        row=index,
        column=1,
        padx=10,
        pady=5
    )

    answer_buttons[letter_key] = letter_buttons


# randomly take a question from the text file
# have the user answer the question
# check if answer is correct
# if correct pick another question
# loop until user decides to quit

root.mainloop()