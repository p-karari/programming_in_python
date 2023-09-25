#reading files in python

employee_fle = open("employee.txt", "r") #two parameters - file name and mode eg read -r , write - w,read and write - r+,append - a

#check if its possible to read from the file using the readable() method
print(employee_fle.readable())
#to read contents of the file use read() method
# print(employee_fle.read())
#to read an individual line use the readline() method
# print("\n\n" + employee_fle.readline())
#to read several lines use the readlines() method
# print(employee_fle.readlines()[4]) #sorts the elements in a list and you can print the individual lines by passing in its index)

for employee in employee_fle.readlines():
    print(employee)

employee_fle.close()
