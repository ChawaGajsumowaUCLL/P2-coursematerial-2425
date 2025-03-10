def is_negative(x):
    return x < 0


def take_while(list, condition):
    list_one = []
    i = 0
    while i <= len(list)-1 and condition(list[i]):
        list_one.append(list[i])
        i += 1
    list_two = list[i::]
    return (list_one, list_two)




print(take_while([-4, -2, 0, -1, 4, 6],is_negative))
