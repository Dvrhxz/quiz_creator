# use tkinter to make gui for quiz
import tkinter as tk
import random
import pygame.mixer

# quiz window
root = tk.Tk()
root.title("Quiz Program")
root.geometry("1690x900")
root.resizable(False, False)
root.config(background="pink")
pygame.mixer.init()

# sound effects
correct_sound = pygame.mixer.Sound("correct_answer.mp3")
correct_sound.set_volume(0.8)
wrong_sound = pygame.mixer.Sound("wrong_answer.mp3")
wrong_sound.set_volume(0.8)

def play_correct_sound():
    correct_sound.play()

def play_wrong_sound():
    wrong_sound.play()

# def functions
# randomly take a question from the text file
def get_random_question():
    try:
        with open("questions_for_quiz.txt", "r", encoding="utf-8") as questions_data:
            content_of_text_file = questions_data.read().strip().split("~~~~~\n")

        questions_list = []

        for section in content_of_text_file:
            lines = section.strip().split("\n")
            question_text = lines[0].replace("Question: ", "")
            answer_options = {line[0]: line[3:] for line in lines[1:5]}
            correct_answer = lines[5].replace("Correct Answer: ", "").strip()
            questions_list.append((question_text, answer_options, correct_answer))

        return random.choice(questions_list) if questions_list else None  # picks a random question

    except FileNotFoundError:
        print("no file was found")
        return None

# check if answer is correct
def check_answer(selected_option):
    global current_score

    if selected_option == correct_answer:
        current_score += 1  # Increase score if correct
        play_correct_sound()
    else:
        play_wrong_sound()

    load_new_question() # if correct pick another question

# loads randomly taken question into the gui
def load_new_question():
    global selected_question, correct_answer, total_questions_loaded

    selected_question = get_random_question()
    if selected_question:
        total_questions_loaded += 1
        question_text, answer_options, correct_answer = selected_question
        question_label.config(text=question_text)

        for key, answer_value in answer_options.items():
            answer_labels[key].config(text=answer_value)
            answer_buttons[key].config(command=lambda k=key: check_answer(k))
            score_label.config(text=f"Score: {current_score}/{total_questions_loaded}")

    else:
        question_label.config(text="No questions found.")

# Elements
# score box
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Times New Roman", 20, "bold"),
    bg="black",
    fg="white",
    width=20,
    relief="solid"
)
score_label.pack(pady=20)

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
answer_labels = {}
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
    answer_labels[letter_key] = answer_text

# Initialize quiz variables
current_score = 0
total_questions_loaded = 0
selected_question = None
correct_answer = ""

# randomly take a question from the text file
load_new_question()

# loop until user decides to quit
root.mainloop()