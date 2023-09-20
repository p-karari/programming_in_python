# Write a program that:
# • asks the user their name
# • if it is the same as your name, outputs
# 'You’re cool', otherwise outputs 'Nice
# to meet you'

name1 = input("Enter your name : ")
name2 = "Gremlin"


if name1.upper() == name2.upper():
    print("Your'e cool")
else:
    print("Nice to meet you")
