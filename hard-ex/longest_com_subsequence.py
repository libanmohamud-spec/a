# BUG: Should be dp[i][j-1]

def longest_common_subsequence(text1, text2):
    """Return length of longest common subsequence between two strings"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
    return dp[m][n]

# Test cases
print("Test 1 (should pass): longest_common_subsequence('a', 'a') =", longest_common_subsequence('a', 'a'))
print("Expected: 1, Got:", longest_common_subsequence('a', 'a'))
print("✓ PASS" if longest_common_subsequence('a', 'a') == 1 else "✗ FAIL")

print("\nTest 2 (should fail): longest_common_subsequence('afloof', 'flooferfoof') =", longest_common_subsequence('afloof', 'flooferfoof'))
print("Expected: 5, Got:", longest_common_subsequence('afloof', 'flooferfoof'))
print("✓ PASS" if longest_common_subsequence('afloof', 'flooferfoof') == 5 else "✗ FAIL")
