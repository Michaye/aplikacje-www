from z5 import Calculator


class ScienceCalculator(Calculator):
    def power(self, x, y):
        return pow(x, y)


c = ScienceCalculator()
print(c.power(5, 10))
