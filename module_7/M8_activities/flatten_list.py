def flatten(og_list):
    flat_list = []
    for item in og_list:
        if type(item) == list:
            flat_list.extend(flatten(item)) # puts the results in the element list ONE BY ONE
        else:
            flat_list.append(item)
    return flat_list

print(flatten([1,[2,3]]))



# other flatten list method
'''
def flatten(values):
    if type(values) != list:
        return [values]
    if len(values) == 0:
        return []
    return flatten(values[0]) + flatten(values[1:])
'''