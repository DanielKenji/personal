# on_all function that applies a function to all elements of a list.
# returns a new list
# A poor man's map() function


def on_all(func, list):
    newlist = []
    for element in list:
        newlist.append(func(element))
    return newlist
