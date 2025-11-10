# bug: "if item in seen:" should be "if item not in seen:"
def remove_duplicates(items):
    """Remove duplicates from list while preserving order"""
    seen = set()
    result = []
    for item in items:
        if item in seen:
            seen.add(item)
            result.append(item)
    return result

# Test cases
print("Test 1 (should pass): remove_duplicates([]) =", remove_duplicates([]))
print("Expected: [], Got:", remove_duplicates([]))
print("✓ PASS" if remove_duplicates([]) == [] else "✗ FAIL")

print("\nTest 2 (should fail): remove_duplicates([1, 2, 2, 3, 1, 4]) =", remove_duplicates([1, 2, 2, 3, 1, 4]))
print("Expected: [1, 2, 3, 4], Got:", remove_duplicates([1, 2, 2, 3, 1, 4]))
print("✓ PASS" if remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4] else "✗ FAIL")
