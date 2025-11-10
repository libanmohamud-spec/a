# BUG: Should be != for mismatch check
def is_valid_parentheses(s):
    """Check if string has valid/balanced parentheses"""
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if stack.pop() == matching[char]:
                return False

    return len(stack) == 0

# Test cases
print("Test 1 (should pass): is_valid_parentheses('') =", is_valid_parentheses(''))
print("Expected: True, Got:", is_valid_parentheses(''))
print("✓ PASS" if is_valid_parentheses('') == True else "✗ FAIL")

print("\nTest 2 (should fail): is_valid_parentheses('()[]{}') =", is_valid_parentheses('()[]{}'))
print("Expected: True, Got:", is_valid_parentheses('()[]{}'))
print("✓ PASS" if is_valid_parentheses('()[]{}') == True else "✗ FAIL")
