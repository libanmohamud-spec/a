# bug: division by 0 when the list of numbers is empty
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

print(calculate_average([2, 4, 6]))  # Expected: 4.0, Got: 4.0 ✓

# Test case that fails
print(calculate_average([]))  # Expected: 0 or None, Got: ZeroDivisionError ✗
