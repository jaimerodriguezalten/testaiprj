
Aquí tienes un ejemplo de un archivo Python que implementa una calculadora simple, pero contiene un bug:

python
Copiar código
# calculator.py

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def modulo(self, a, b):
        return a % b

    # Bug: This method should return a^b, but it incorrectly uses multiplication instead of exponentiation
    def power(self, a, b):
        return a * b
