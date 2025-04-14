# input questions
while True:
    question = input("Enter a Question/Problem: ").strip()

    # input the possible answers
    letter_choices = {}
    for letter in ["a", "b", "c", "d"]:
        choice = input(f"enter answer for choice {letter.upper()}: ")
        letter_choices[letter] = choice
    break

print(letter_choices)
# determine the correct answer
# format and store into a text file
# make gui (if possible)