# Write a program that converts between
# centimetres, and inches and vice versa, by:
# • asking the user to input a number
# • asking the user to choose between
# converting from centimetres to inches or from
# inches to centimetres
# • calculating and outputting the result using
# functions

number = float(input("Enter number you wish to convert : "))
print("-- SELECT DESIRED OPERATION --\nOption 1 - centimeters to inches\nOption 2 - inches to centimetres")
option =int(input("Option : "))

def inches_to_cms(number):
    result = number * 2.54
    print(result)
    return result

def cms_to_inches(number):
    result = number * 0.393700787
    print(result)
    return result


if option == 1:
    cms_to_inches(number)

elif option == 2:
    inches_to_cms(number)
else:
    print("-- INVALID INPUT(s) -- \nEnsure you follow the given instructions")



