def calculation_average(nums):
    assert len(nums) > 0, "The list cannot be empty"
    total = sum(nums)
    average = total/len(nums)
    assert average >= 0, "The average cannot be negative"
    return average


# print(calculation_average([1]))

