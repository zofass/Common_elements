def common_elements():
    multiples_of_3 = [num for num in range(1, 21) if num % 3 == 0]
    multiples_of_5 = [num for num in range(1, 121) if num % 5 == 0]
    common_set = set(multiples_of_3).intersection(multiples_of_5)
    return common_set


result = common_elements()
expected_result = set(range(3, 21, 3)).intersection(set(range(5, 21, 5)))

assert result == expected_result, f"Expected {expected_result}, but got {result}"
print("ОК")
