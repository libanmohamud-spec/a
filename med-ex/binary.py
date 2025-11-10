# bug: if the target is bigger than the middle, left should be mid + 1
def binary_search(arr, target):
    """Return index of target in sorted array, or -1 if not found"""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid
        else:
            right = mid - 1

    return -1

# Test cases
print("Test 1 (should pass): binary_search([1, 2, 3, 4, 5], 1) =", binary_search([1, 2, 3, 4, 5], 1))
print("Expected: 0, Got:", binary_search([1, 2, 3, 4, 5], 1))
print("✓ PASS" if binary_search([1, 2, 3, 4, 5], 1) == 0 else "✗ FAIL")

print("\nTest 2 (may cause infinite loop or wrong result): binary_search([1, 2, 3, 4, 5], 5)")
try:
    result = binary_search([1, 2, 3, 4, 5], 5)
    print("Expected: 4, Got:", result)
    print("✓ PASS" if result == 4 else "✗ FAIL")
except:
    print("✗ FAIL - Function caused an error or infinite loop")
