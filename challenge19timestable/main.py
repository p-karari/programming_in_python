# Write a program that:
# • asks the user to input a number
# • outputs the times table for that
# number
# • starts again every time it finishes

# import math

print(str((5*5)))

# num = 7
while True:
    num = int(input("Enter number : "))
    for x in range(1, 10):
        print(str(x) + " X " + str(num) + " = " + str(x * num))
