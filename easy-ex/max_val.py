# bug: 0 is bigger than all negative numbers, needs -float('inf')
def find_max(numbers):
    """Find the maximum value in a list."""
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Test case that works
print(find_max([1, 5, 3, 9, 2]) == 9)  # Expected: 9, Got: 9 ✓

# Test case that fails
print(find_max([-5, -2, -8, -1]) == -1)  # Expected: -1, Got: 0 ✗
