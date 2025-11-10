def two_sum(numbers, target):
    """Return indices of two numbers that add up to target"""
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i + 1  # BUG: Should be just i
    return None

# Test cases
print("\nTest (should fail): two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9))
print("Expected: [0, 1], Got:", two_sum([2, 7, 11, 15], 9))
print("✓ PASS" if two_sum([2, 7, 11, 15], 9) == [0, 1] else "✗ FAIL")
