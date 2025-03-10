def children_and_adults(list, condition):
    first_list = []
    second_list = []
    for item in list:
        if condition(item):
            second_list.append(item)
        else:
            first_list.append(item)

    return (second_list, first_list)


def of_age(person):
    return person.age < 18
       