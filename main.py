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

