# bug: using the wrong vowel list (missing 'u')

def count_vowels(text):
    """Return the count of vowels in text"""
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in "aeio":
            count += 1
    return count

# Test cases
print("Test 1 (should pass): count_vowels('hello') =", count_vowels('hello'))
print("Expected: 2, Got:", count_vowels('hello'))
print("✓ PASS" if count_vowels('hello') == 2 else "✗ FAIL")

print("\nTest 2 (should fail): count_vowels('education') =", count_vowels('education'))
print("Expected: 5, Got:", count_vowels('education'))
print("✓ PASS" if count_vowels('education') == 5 else "✗ FAIL")
