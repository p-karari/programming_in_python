#if statemens in python

is_tall = False
is_male = True


if is_tall and is_male:
    print("You are a tall male")
elif is_tall and not(is_male):
    print("You are tall but not male")
elif not(is_tall) and is_male:
    print("You are a short male")
else :
    print("You are neither tall nor a male")

