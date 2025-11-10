# bug: num % 2 == 1 gives odd numbers

def sum_even_numbers(numbers):
    """Return sum of all even numbers in the list"""
    total = 0
    for num in numbers:
        if num % 2 == 1:
            total += num
    return total

# Test cases
print("Test 1 (should pass): sum_even_numbers([1, 3, 5]) =", sum_even_numbers([1, 3, 5]))
print("Expected: 0, Got:", sum_even_numbers([1, 3, 5]))
print("✓ PASS" if sum_even_numbers([1, 3, 5]) == 0 else "✗ FAIL")

print("\nTest 2 (should fail): sum_even_numbers([2, 4, 6, 8]) =", sum_even_numbers([2, 4, 6, 8]))
print("Expected: 20, Got:", sum_even_numbers([2, 4, 6, 8]))
print("✓ PASS" if sum_even_numbers([2, 4, 6, 8]) == 20 else "✗ FAIL")
