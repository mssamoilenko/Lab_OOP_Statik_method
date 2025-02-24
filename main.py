#task1
class Human:
    count = 0
    def __init__(self, name, age, eye_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        Human.count += 1

    def getInfo(self):
        return (f"\nname - {self.name};"
                f"\nage - {self.age};"
                f"\neye color - {self.eye_color}")
    @staticmethod
    def countHuman():
        return Human.count

firstPerson = Human("Alla", 25, "chameleon")
secondPerson = Human("Kolya", 20, "brown")
print(firstPerson.getInfo())
print(secondPerson.getInfo())
print(f"\nTotal number of Human objects created: {Human.countHuman()}")

#task2
class AreaCalculator:
    count = 0

    @staticmethod
    def triangle_area(base, height):
        AreaCalculator.count += 1
        return 0.5 * base * height

    @staticmethod
    def rectangle_area(length, width):
        AreaCalculator.count += 1
        return length * width

    @staticmethod
    def square_area(side):
        AreaCalculator.count += 1
        return side ** 2

    @staticmethod
    def rhombus_area(diagonal1, diagonal2):
        AreaCalculator.count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return AreaCalculator.count

area_calculator = AreaCalculator()
print("Triangle area (base=5, height=10):", area_calculator.triangle_area(5, 10))
print("Rectangle area (length=4, width=6):", area_calculator.rectangle_area(4, 6))
print("Square area (side=3):", area_calculator.square_area(3))
print("Rhombus area (diagonal1=4, diagonal2=6):", area_calculator.rhombus_area(4, 6))
print("Total area calculations:", AreaCalculator.get_calculation_count())

#task3
class Statistics:

    @staticmethod
    def maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def minimum(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n < 0:
            return "Factorial is not defined for negative numbers."
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print("Maximum of (3, 5, 2, 8):", Statistics.maximum(3, 5, 2, 8))
print("Minimum of (3, 5, 2, 8):", Statistics.minimum(3, 5, 2, 8))
print("Average of (3, 5, 2, 8):", Statistics.average(3, 5, 2, 8))
print("Factorial of 5:", Statistics.factorial(5))