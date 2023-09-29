# Write a program that:
# • asks the user for the distance (in metres)
# • asks the user for the time in seconds
# that a journey was completed in
# • calculates and outputs the average
# speed using a function

distance = int(input("Enter distance in metres : "))
time = int(input("Enter time in seconds  : "))

def compute_speed(distance, time):
    speed = distance / time
    return speed
print("Average speed : ", compute_speed(distance, time) , "m/s")




