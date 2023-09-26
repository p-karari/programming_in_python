#multiple choice quiz project

from questions import questions

questions_prompts = [

    "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange \n",
    "What color are bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow \n",
    "What color are Strawberries? \n(a) Yellow \n(b) Red \n(c) Maroon \n"
]

questionns = [
    questions(questions_prompts[0], "a"),
    questions(questions_prompts[1], "c"),
    questions(questions_prompts[2], "b")

]

def run_test(question):

    score = 0
    for question in questionns:

        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1

    print("You got " + str(score) + "/"  + str(len(questionns)) + " correct")

run_test(questionns)
