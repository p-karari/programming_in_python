#try except in python
#error handling in python -- for catching errors in python -- user defined
        #General exception handling
try:
    print(int(input("Enter a number : ")))

except:
    print("invalid input")

#         #Exception handling of a specific error
# try:
#     print(str(input("Enter a string : ")))
#
# except ValueError:
#     print("invalid entry")

        #Exception handling of several specific errors as variables

try:
    print(int(input("Enter a number : ")))
    example = 10/0
    print(example)
except ZeroDivisionError as err:
    print(err)
except ValueError as erro:
    print(erro)