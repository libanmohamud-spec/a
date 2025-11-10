# bug: iteration should be in range(n - 1)
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    curr = 1
    ith = curr
    for i in range(n - 2):
        ith = curr + prev
        prev = curr
        curr = ith
    return ith

# Test cases
print("Test 1 (should pass): fibonacci(2) =", fibonacci(2))
print("Expected: 1, Got:", fibonacci(2))
print("✓ PASS" if fibonacci(2) == 1 else "✗ FAIL")

print("\nTest 2 (should fail): fibonacci(5) =", fibonacci(5))
print("Expected: 5, Got:", fibonacci(5))
print("✓ PASS" if fibonacci(5) == 5 else "✗ FAIL")
