class Calculator:
    def add(self, x, y):
        return x + y

    def difference(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


class ScienceCalculator(Calculator):
    def power(self, x, y):
        return pow(x, y)


c = ScienceCalculator()
print(c.power(5, 10))
