def question_loder(path="files/questions.json"):
    with open(path, "r") as file:
        contents = file.read()
    return contents


if __name__ == "__main__":
    print(question_loder())
