def find(list, condition):
    for item in list:
        if condition(item):
            return item
    return None

def has_consecutive_characters(string):
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            return True
            
print(find(["monkey", "banana", "computer", "yellow", "oddish"], has_consecutive_characters))