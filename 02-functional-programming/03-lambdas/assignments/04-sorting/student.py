# orders the Persons by increasing age
def sort_by_age(people):
    return sorted(people, key=lambda person: person.age)
     
#orders the Persons by decreasing age
def sort_by_decreasing_age(people):
    return sorted(people, key = lambda person: -person.age)
    
#orders the Persons by name, alphabetically
def sort_by_name(people):
    return sorted(people, key = lambda person: person.name)

#orders the Persons by name, and in case of equal names, by increasing age
def sort_by_name_then_age(people):
    return sorted(people, key = lambda person: (person.name, person.age))

#orders the Persons by name, and in case of equal names, by decreasing age
def sort_by_name_then_decreasing_age(people):
    return sorted(people, key = lambda person: (person.name, -person.age))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  # Dit zorgt voor een nette output bij print()
        return f"{self.name} ({self.age})"

people = [
        Person('John', 18),
        Person('John', 20),
        Person('Peter', 42),
        Person('Sarah', 19),
        Person('Kim', 17),
        Person('Chris', 35),
    ]

print(sort_by_age(people))
print(sort_by_decreasing_age(people))
print(sort_by_name(people))
print(sort_by_name_then_age(people))
print(sort_by_name_then_decreasing_age(people))
