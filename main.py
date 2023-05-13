
from random import randint

class Math_persons():
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def addition(self):
        return self.A + self.B

    def subtraction(self):
        return self.A - self.B

    def multiplication(self):
        return self.A * self.B

    def division(self):
        return self.A / self.B

def math_problem():
    A = randint(100, 200)
    B = randint(5, 10)
    print(A)
    print(B)
    dummy_list = []
    math_answers = Math_persons(A, B)
    dummy_list.append(math_answers.addition())
    dummy_list.append(math_answers.subtraction())
    dummy_list.append(math_answers.multiplication())
    dummy_list.append(math_answers.division())
    for value in dummy_list:
        if (value + A) >= 100 and (value + A) <= 200 and abs(round(value + A) - (value + A)) < 0.0001:
            print(f"math_person is Add and A is: {A} & B is {(value + A)} and math_answer is:{value}")
        elif (value - A) >= 100 and (value - A) <= 200 and abs(round(value - A) - (value - A)) < 0.0001:
            print(f"math_person is sub and A is: {A} & B is {(value - A)} and math_answer is:{value}")
        elif (value * A) >= 100 and (value * A) <= 200 and abs(round(value * A) - (value * A)) < 0.0001:
            print(f"math_person is mul and A is: {A} & B is {(value * A)} and math_answer is:{value}")
        elif (value / A) >= 5 and (value / A) <= 10 and abs(round(value / A) - (value / A)) < 0.0001:
            print(f"math_person is div and A is: {A} & B is {(value / A)} and math_answer is:{value}")
    math_problem()

math_problem()
