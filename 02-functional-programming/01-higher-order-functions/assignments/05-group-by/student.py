def group_by(xs, key_function):
    bib = {}
    for value in xs:
        if key_function(value) not in bib:
            bib[key_function(value)] = [value]
        else:
            bib[key_function(value)].append(value)
        
    return bib


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  # Zorgt ervoor dat print() nuttige info toont
        return f"Person(name='{self.name}', age={self.age})"



class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        return f"Card(value={self.value}, suit='{self.suit}')"

def age(person):
    return person.age

def card_suit(card):
    return card.suit

print(group_by([
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
], age))

print(group_by([
    Card(value=2, suit='hearts'),
    Card(value=5, suit='clubs'),
    Card(value=4, suit='hearts'),
    Card(value=10, suit='hearts'),
], card_suit))


