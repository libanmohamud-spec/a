# BUG: Should be arr[i + 1] on partition function before return
def quick_sort(arr, low, high):
    """Sort array using quick sort algorithm"""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    """Partition array around pivot"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i]
    return i + 1

def sort_array(arr):
    """Helper function to sort array"""
    if not arr:
        return arr
    return quick_sort(arr[:], 0, len(arr) - 1)

# Test cases
print("Test 1 (should pass): sort_array([5]) =", sort_array([5]))
print("Expected: [5], Got:", sort_array([5]))
print("✓ PASS" if sort_array([5]) == [5] else "✗ FAIL")

print("\nTest 2 (should fail): sort_array([3, 6, 8, 10, 1, 2, 1]) =", sort_array([3, 6, 8, 10, 1, 2, 1]))
print("Expected: [1, 1, 2, 3, 6, 8, 10], Got:", sort_array([3, 6, 8, 10, 1, 2, 1]))
print("✓ PASS" if sort_array([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10] else "✗ FAIL")
