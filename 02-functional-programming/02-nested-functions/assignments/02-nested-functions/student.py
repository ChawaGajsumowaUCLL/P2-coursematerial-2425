
def count(xs, predicate):
    return len([x for x in xs if predicate(x)])


def indices_of(xs, condition):
    return [index for index in range(len(xs)) if condition(xs[index])]


#counts the number of people who are older than min_age
def count_older_than(people, min_age):
    def is_older_than(person):
        return person.age >= min_age
    return count(people, is_older_than)



#returns the indices of all the Cards whose suit equals suit
def indices_of_cards_with_suit(cards, suit):
    def is_with_suit(card):
        return card.suit == suit
    return indices_of(cards, is_with_suit)