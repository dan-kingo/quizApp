import json

with open("files/questions.json") as file:
    contents = file.read()

data = json.loads(contents)
score = 0

for i, question in enumerate(data):
    print(f'#{i + 1}. {question["question_text"]}')

    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}. {alternative}")

    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer

    if user_answer == question["correct_answer"]:
        score += 1

for index, question in enumerate(data):
    response = f"#{index + 1}. Your answer: {question["user_answer"]}, Correct answer: {question['correct_answer']}"
    print(response)

print(f"Your score is {score}/{len(data)}")
percentage = (score / len(data)) * 100
print(f"You have {percentage}% correct answers.")