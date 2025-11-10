# BUG: Missing code to append remaining elements
# Should have:
# while i < len(arr1):
#     result.append(arr1[i])
#     i += 1
# while j < len(arr2):
#     result.append(arr2[j])
#     j += 1

def merge_sorted_arrays(arr1, arr2):
    """Merge two sorted arrays into one sorted array"""
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    return result

# Test cases
print("Test 1 (should pass): merge_sorted_arrays([1, 3], [2, 4]) =", merge_sorted_arrays([1, 3], [2, 4]))
print("Expected: [1, 2, 3, 4], Got:", merge_sorted_arrays([1, 3], [2, 4]))
print("✓ PASS" if merge_sorted_arrays([1, 3], [2, 4]) == [1, 2, 3, 4] else "✗ FAIL")

print("\nTest 2 (should fail): merge_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]) =", merge_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]))
print("Expected: [1, 2, 3, 4, 5, 6, 7, 8], Got:", merge_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]))
print("✓ PASS" if merge_sorted_arrays([1, 2, 3], [4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8] else "✗ FAIL")
