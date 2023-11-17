class Grandparent:
    age = 50
    def __init__(self, money):
        self.pension = money
    def pension1(self, day):
        if day == 1:
            return f"Time to become a pension {self.pension}"

class Parent(Grandparent):
    satiety = 100
    def __init__(self, money):
        self.salary = money

    def salary1(self):
        return f"You became a slary {self.salary}"


class Child(Parent):
    height = 130

    def __init__(self, grade):
        self.grades = grade
    def school(self):
        return f"Your grade for this lesson is {self.grades}"


child = Child(12)