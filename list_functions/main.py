lucky_numbers = [5, 7, 90, 852, 852, 23, 54, 88]

characters_list = ["Tommy", "Tariq", "Sax", "Ghost", "Angela"]
#characters_list.extend(lucky_numbers) #extend function is for adding another list to an existing one
lucky_numbers.append(312) #append function is for adding other list elements to an existing list
characters_list.insert(6, "Tasha") #insert function inserts an element at a specified index in a list
lucky_numbers.remove(90) #removing a specific element from a list
lucky_numbers.pop() #pops the last elements out of a list
characters_list.sort() #sorts the elements of a list
lucky_numbers.reverse() #reverses the order of elements inside of a list

lucky_numbers2 = lucky_numbers.copy() #duplicating elements of a list

print(lucky_numbers.count(852)) #counts the number of times an element appears in a list
print(lucky_numbers.index(852)) #.index() method is used to check the index of a specific element of a list
print(characters_list)
print(lucky_numbers)
