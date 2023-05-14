import random
def __init__(self,a,b):
    def math_person(person,a,b):
            if person == "Andy" :
                return a+b
            if person == "Sandy" :
                return a-b
            if person == "Matt" :
                return a*b
            if person == "Danny" :
                return a/b
math_person = random.choice(["Andy", "Sandy", "Matt", "Danny"])
a = random.randint(100,200)
b = random.randint(5,10)
def __init__(self,a,b):
    math_person = math_answers(a,b)
    empty.dictionary = math_answers.addition
    empty.dictionary = math_answers.subtraction
    empty.dictionary = math_answers.multiplication
    empty.dictionary = math_asnwers.division
    def empty_list():
        empty_list().append = math_answers.addition
        empty_list().append = math_answers.subtraction
        empty_list().append = math_answers.mutiplication
        empty_list().append = math_answers.division

    def guess_b_and_person(a, answer):
        for b in range(5, 11):
            for person in ["Andy", "Sandy", "Matt", "Danny"]:
                if run_math_person(person, a, b) == answer:
                    return (b, person)

    # Generate random numbers for A and B
    a = random.randint(100, 200)
    b = random.randint(5, 10)

    # Choose a random math person to run the formula
    math_person = random.choice(["Andy", "Sandy", "Matt", "Danny"])

    # Run the formula and get the answer
    answer = run_math_person(math_person, a, b)

    # Guess B and the math person
    guessed_b, guessed_person = guess_b_and_person(a, answer)

    # Print the results
    print("A =", a)
    print("Math person =", math_person)
    print("Answer =", answer)
    print("Guessed B =", guessed_b)
    print("Guessed math person =", guessed_person)

    # Check if the guess was correct and print the result
    if guessed_b == b and guessed_person == math_person:
        print("Jury was correct!")
    else:
        print("Jury was incorrect.")
