secret_word = "Giraffe"
guess = " "
guess_count = 1
guess_limit = 3
out_of_guesses = False

while guess.upper() != secret_word.upper() and not(out_of_guesses):
    if guess_count <= guess_limit:
        guess = input("Enter guess : ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess.upper() == secret_word.upper():
    print("You win")
else:
    print("Out of guesses , you loose")

