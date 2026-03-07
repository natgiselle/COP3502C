# write a function remove_all that 
# removes all occurences of a specific valur from a given list.


# go from right to left since the lenght of the list keps changing
def remove_all(my_list, value):
    for i in range(len(my_list) -1, -1, -1): # updated limits
        if my_list[i] == value:
            my_list.pop(i) # removing value at i index

    return my_list

my_list = [5,5,4,8,5,1,5]
print(remove_all(my_list, 5))