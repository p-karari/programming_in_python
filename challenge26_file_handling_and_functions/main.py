# Write a maths quiz with three questions.
# It must ask the user to input their name at
# the start.
# At the end it should display a message
# informing the user of their score.
# Write a function that saves the user’s
# name and quiz result in a text file.

name = input("Enter Name : ")
qn1 = int(input("Question 1\n 5 X 3 = "))
qn2 = int(input("Question 2\n 8 X 12 = "))
qn3 = int(input("Question 2\n 22 X 17 = "))

score = 0
if qn1 == 15:
    score += 1
if qn2 == 8*12:
    score += 1
if qn3 == 22 * 17:
    score += 1

print("Your score is " + str(score))

quiz_info = open("Test_results.txt", "a")

def save_score(name, score):
    quiz_info.write("\nName : " + name)
    quiz_info.write("\nScore : " + str(score) + "\n")
    quiz_info.close()
    return

save_score(name, score)

