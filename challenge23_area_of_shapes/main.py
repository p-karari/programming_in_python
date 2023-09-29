# A gardener needs to buy some turf for a project
# they are working on. The garden is rectangular
# with a circular flower bed in the middle.
# Write a program that:
# • asks the user for the dimensions of the lawn
# and the radius of the circle (in metres)
# • uses a function to calculate and output
# the amount of turf needed

print("-- Enter lawn dimensions below (in metres) --")
width = int(input("Width : "))
length = int(input("Length : "))
radius = int(input("Radius : "))
pi = 22 / 7

def flower_bed(radius):
    flower_area = pi * radius * radius
    return flower_area

def lawn_area(width, length):
    rec_area = width * length
    return rec_area

print("Amount of turf needed  = ", (lawn_area(width, length) - flower_bed(radius)), "Metres squared")
