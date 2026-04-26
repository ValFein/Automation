class Calculator:

    def __init__(self, name='basicCalculator'):
        self.name = name


    def add(self, num1, num2):
        print(f'first number is{num1}, secode number is {num2}')
        return num1 + num2

    def minus(self, num1, num2):
        print(f'first number is{num1}, second number is {num2}')
        return num1 - num2

    def divide(self, num1, num2):
        print(f'first number is{num1}, second number is {num2}')
        return num1 / num2
