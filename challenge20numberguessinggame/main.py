# Write a program that:
# • asks the user to input a number and
# repeats until they guess the number 7
# • congratulate the user with a ‘Well
# Done’ message when they guess
# correctly

secret_num = 7
guess = 0
while guess != secret_num:
    guess = int(input("Enter guess : "))
    if guess == secret_num:
        print("-- Well done! --")
    else:
        print("Incorrect! guess again")
