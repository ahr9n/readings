# 9. Write a simple quiz game that has a list of ten questions and a list of answers to those ques-
# tions. The game should give the player four randomly selected questions to answer. It should
# ask the questions one-by-one, and tell the player whether they got the question right or
# wrong. At the end it should print out how many out of four they got right.

import random

questions = ["What is the capital of France?", "What is the capital of Germany?", "What is the capital of Italy?", "What is the capital of Spain?", "What is the capital of Portugal?", "What is the capital of Belgium?", "What is the capital of Denmark?", "What is the capital of Sweden?", "What is the capital of Norway?", "What is the capital of Finland?"]
answers = ["Paris", "Berlin", "Rome", "Madrid", "Lisbon", "Brussels", "Copenhagen", "Stockholm", "Oslo", "Helsinki"]

cnt = 0
for i in range(4):
    print(random.choice(questions))
    answer = input("Your answer: ")
    if answer.lower() == answers[i].lower():
        cnt += 1

print("You got", cnt, "out of 4 correct.")
