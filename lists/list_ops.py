# sum() and multiply() functions that operate on the numbers in a list


def sum(list):
    sum = 0
    for element in list:
        if type(element) == int or type(element) == float:
            sum = sum + element
    return sum
    
def multiply(list):
    multiply = 1
    for element in list:
        if type(element) == int or type(element) == float:
            multiply = multiply * element
    return multiply

