import random

def run_math_person(person, a, b):
    if person == "Andy":
        return a + b
    elif person == "Sandy":
        return a - b
    elif person == "Matt":
        return a * b
    elif person == "Danny":
        return a / b

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
