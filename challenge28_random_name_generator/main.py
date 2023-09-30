# Challenge 28
# Write a random name generator that
# asks for the user to input 5 names, stores
# them in an array and then outputs one
# of them at random.
import random
names = []
for x in range(1, 6):
    name = input("Enter name " + str(x) + " : ")
    names.append(name)

print(random.choice(names), " has been chosen")
# for y in range(0, 5):
#     print(names[y])
