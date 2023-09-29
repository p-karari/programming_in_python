# write a sign-up program for an after school club; it should ask the user for the
# following details and store them in a file:
# • First Name
# • Last Name
# • Gender
# • Form

first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
gender = input("Enter gender : ")
form = input("Enter form : ")

student_details = open("student_details_file.txt", "a")

student_details.write("\nFirst name: "+first_name+"\nLast name: "+last_name+"\nGender: "+gender+"\nForm: "+form)