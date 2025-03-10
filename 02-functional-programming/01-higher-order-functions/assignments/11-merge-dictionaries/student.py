def sum(item1, item2):
    return item1 + item2


def merge_dictionaries(d1, d2, merge_function):
    result = d1.copy()
    
    for k in d2.keys():
        if k in result.keys():
            result[k] = merge_function(result[k], d2[k])
        else:
            result[k] = d2[k]

    return result

order1 = {'banana': 4, 'coke': 12, 'chocolate': 3}
order2 = {'mustard': 1, 'chocolate': 7}
combined = merge_dictionaries(order1, order2, sum)
print(combined)

