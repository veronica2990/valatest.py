import random


class MathPerson:
    def __init__(self, name):
        self.name = name

    def run_formula(self, a, b):
        pass


class Andy(MathPerson):
    def run_formula(self, a, b):
        return a + b


class Sandy(MathPerson):
    def run_formula(self, a, b):
        return a - b


class Matt(MathPerson):
    def run_formula(self, a, b):
        return a * b


class Danny(MathPerson):
    def run_formula(self, a, b):
        return a / b


class Judge:
    def __init__(self):
        self.a = random.randint(100, 200)
        self.b = random.randint(5, 10)
        self.math_person = random.choice([Andy, Sandy, Matt, Danny])

    def run_math_person(self):
        return self.math_person().run_formula(self.a, self.b)

    def get_a_and_answer(self):
        return self.a, self.run_math_person()


class Jury:
    def __init__(self, a, answer):
        self.a = a
        self.answer = answer

    def guess_b_and_person(self):
        for b in range(5, 11):
            for MathPersonClass in [Andy, Sandy, Matt, Danny]:
                math_person = MathPersonClass()
                if math_person.run_formula(self.a, b) == self.answer:
                    return (b, math_person.name)

    def get_guess(self):
        b, math_person_name = self.guess_b_and_person()
        return b, math_person_name


# Test the code by creating a Judge, running their math person's formula,
# and having the Jury guess what B and math person were used

judge = Judge()
a, answer = judge.get_a_and_answer()
jury = Jury(a, answer)
guessed_b, guessed_person = jury.get_guess()

# Print the results
print("A =", a)
print("Math person =", judge.math_person.__name__)
print("Answer =", answer)
print("Guessed B =", guessed_b)
print("Guessed math person =", guessed_person)

# Check if the guess was correct and print the result
if guessed_b == judge.b and guessed_person == judge.math_person.__name__:
    print("Jury was correct!")
else:
    print("Jury was incorrect.")
