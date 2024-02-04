import json
import utils

"""
sample CLI based Quiz App
developed by @dan-kingo

you can get the project file at https://www.github.com/dan-kingo/quizApp/tree/master
"""

contents = utils.question_loder()

data = json.loads(contents)
score = 0

for i, question in enumerate(data):
    try:
        print("\n" + f'#{i + 1}. {question["question_text"]}')

        for index, alternative in enumerate(question["alternatives"]):
            print(f"{index + 1}. {alternative}")

        user_answer = int(input("Enter your answer: "))

        question["user_answer"] = user_answer

        if user_answer == question["correct_answer"]:
            score += 1
    except ValueError:
        print("Invalid input only numbers{1-4} are allowed!")

print("Result: ")
for index, question in enumerate(data):
    try:
        response = f"#{index + 1}. Your answer: {question['user_answer']}, Correct answer: {question['correct_answer']}"
        print(response)
    except KeyError:
        print(f"#{index + 1}. please enter a number!")
print(f"Your score is {score}/{len(data)}")

percentage = (score / len(data)) * 100
percentage = float(f"{percentage:.2f}")

if percentage >= 90:
    print("You got grade 'A+'")
elif percentage >= 85:
    print("You got grade 'A' ")
elif percentage >= 80:
    print("You got grade 'A-' ")
elif percentage >= 75:
    print("You got grade 'B+' ")
elif percentage >= 70:
    print("You got grade 'B' ")
elif percentage <= 65:
    print("You got grade 'F' ")
print(f"You have {percentage}% correct answers.")
