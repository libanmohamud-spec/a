# BUG: Should be left < right
def is_palindrome(text):
    """Check if text is a palindrome"""
    left = 0
    right = len(text) - 1

    while right < left:
        if text[right] != text[left]:
            return False
        left += 1
        right -= 1

    return True

# Test cases
print("Test 1 (should pass): is_palindrome('racecar') =", is_palindrome('racecar'))
print("Expected: True, Got:", is_palindrome('racecar'))
print("✓ PASS" if is_palindrome('racecar') == True else "✗ FAIL")

print("\nTest 2 (should fail): is_palindrome('foobar') =", is_palindrome('foobar'))
print("Expected: False, Got:", is_palindrome('foobar'))
print("✓ PASS" if is_palindrome('foobar') == False else "✗ FAIL")
