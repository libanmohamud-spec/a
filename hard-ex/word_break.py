# BUG: Should be "and" not "or" in last if
def word_break(s, word_dict):
    """Check if string can be segmented into space-separated words from dictionary"""
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] or s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Test cases
print("Test 1 (should pass): word_break('a', ['a']) =", word_break('a', ['a']))
print("Expected: True, Got:", word_break('a', ['a']))
print("✓ PASS" if word_break('a', ['a']) == True else "✗ FAIL")

print("\nTest 2 (should fail): word_break('leetcode', ['le', 'eet', 'code']) =", word_break('leetcode', ['le', 'eet', 'code']))
print("Expected: False, Got:", word_break('leetcode', ['le', 'eet', 'code']))
print("✓ PASS" if word_break('leetcode', ['le', 'eet', 'code']) == False else "✗ FAIL")
