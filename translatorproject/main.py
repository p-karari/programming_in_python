 #This is a simple translator project that simply replaces where there is a vowel with the letter 'g'

def translate(phrase):
     translation = ""
     for letter in phrase:
         if letter.lower() in "aeiou":
             translation = translation + "g"
         else:
             translation = translation + letter
     return translation

print(translate(input("Enter a phrase : ")))