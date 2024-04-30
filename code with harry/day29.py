def count_repeated_elements(tup):
    element_count = {}
    for element in tup:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

# Test the function
tup = ('a', 'b', 'c', 'a', 'b', 'a', 'd', 'e', 'f', 'e')
print(count_repeated_elements(tup))
