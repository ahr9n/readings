# 1. Write a program that asks the user to enter some text and then counts how many articles are
# in the text. Articles are the words 'a', 'an', and 'the'.

text = input("Enter some text: ").split()

articles = ["a", "an", "the"]
cnt = 0
for word in text:
    if word.lower() in articles:
        cnt += 1
print(f"There are {cnt} articles in the text.")
