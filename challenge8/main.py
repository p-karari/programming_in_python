# Write a program that:
# • asks the user how long on average
# they spend watching TV each day
# • if it is less than 2 hours, outputs ‘That
# shouldn’t rot your brain too much’; if it
# is less than 4 hours per day, outputs
# ‘Aren’t you getting square eyes?’;
# otherwise outputs ‘Fresh air beats
# channel flicking’

watch_hours = float(input("Enter your total tv watching hours per day :"))

if watch_hours <= 2 :
    print("shouldn’t rot your brain too much")
elif watch_hours <= 4 and watch_hours > 2 :
    print("Aren't you getting square eyes")
else:
    print("Fresh air beats channel fleaking")