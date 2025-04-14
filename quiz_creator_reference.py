# open text file
questions_file = open("questions_for_quiz.txt", "a")

# input questions
while True:
    question = input("Enter a Question/Problem: ").strip().capitalize()

    # input the possible answers
    letter_choices = {}
    for letter in ["a", "b", "c", "d"]:
        choice = input(f"enter answer for choice {letter.upper()}: ")
        letter_choices[letter] = choice

# determine the correct answer
    while True:
        correct_answer = input("Enter the correct answer from a-d: ").strip().lower()
        if correct_answer in letter_choices:
            break
        else:
            print("Input not in valid choices, please choose from (a/b/c/d): ")

    # format and store into a text file
    questions_file.write(f"Question: {question}\n")
    for key in ["a", "b", "c", "d"]:
        questions_file.write(f"{key}.) {letter_choices[key]}\n")
    questions_file.write(f"Correct Answer: {correct_answer}\n")
    questions_file.write(f"~~~~~\n")
    print("\nquestion and answers stored successfully")

    # ask if you want to input another question
    retry = input("Do you want to input another problem? (y/n): ").strip().lower()
    if retry != "y":
        print("The program is closing.....")
        break

# close text file after exiting
questions_file.close()

# make gui (if possible)