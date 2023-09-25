#writing and appending to files in python

# appending

employees2 = open("emplyeees2", "a")

employees2.write("\nHayley - New security personnel") #appends it contentents onto the end of the list


#writing to files and writing new files

employees3 = open("emplyees3", "w")
employees3.write("I am a new list")
employees3.write("\nNew employee list")#Overrides the contents previously contained on the list

writingnewfilesdemo = open("index.html", "w")
writingnewfilesdemo.write("<h2> Sample html code </h2>")

writingnewfilesdemo2 = open("styles.css", "w")
writingnewfilesdemo2.write("body {color:red}")

employees2.close()
