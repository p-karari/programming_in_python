# challenge 29
# Write a program that allows the user to
# create and store a checklist for a holiday.
# It should start by asking them the
# destination of the holiday, how many
# things they need to pack and how many
# tasks they need to complete to prepare.
# The user should then be able to enter
# each item they need to pack and each
# task they need to complete.

holiday_checklist = open("Holiday_Checklist.txt", "a")


destination = input("Enter your desired destination : ")

holiday_checklist.write("\n-- DESTINATION -- \n" + destination)

pack = int(input("Enter number of items you need to pack : "))
print("-- ITEMS LIST --")
holiday_checklist.write("\n-- ITEMS LIST -- \n")
for item in range(0, pack):
    pack_list = []
    pack_list_items = input("Item " + str((item + 1)) + " : ")
    holiday_checklist.write(("\n") + str(pack_list_items) + "\n")
    pack_list.append(pack_list_items)

tasks = int(input("Enter number of tasks you need to complete : "))
print("-- TASKS LIST --")
holiday_checklist.write("\n-- TASK LIST --  \n")

for task in range(0, tasks):
    tasks_list = []
    task_list_items = input("Task " + str((task + 1)) + " : ")
    holiday_checklist.write("\n" + str(task_list_items) + "\n")
    tasks_list.append(task_list_items)


holiday_checklist.close()

print("Your list has been saved")