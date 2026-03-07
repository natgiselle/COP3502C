# the functoin double_odd_elements takes a 
# parameter number_list( a non-empty list of integers)
# but doubled in value

# example: for input [1,2,3,4,5] the function should return [2,6,10]

def double_odd_elements(number_list):
    result = []
    for i in range(0, len(number_list)):
        if number_list[i] % 2 != 0:
            result.append(i)
            result[i] * 3
            