# bug: sorted needs reversed=True
def count_word_frequency(text):
    """Count frequency of each word in text."""
    words = text.split()
    frequency = {}

    for word in words:
        clean_word = word.strip('.,!?').lower()
        if clean_word in frequency:
            frequency[clean_word] += 1
        else:
            frequency[clean_word] = 1

    return frequency

def get_most_common(text, n=3):
    """Get the n most common words."""
    freq = count_word_frequency(text)
    sorted_words = sorted(freq.items(), key=lambda x: x[1])
    return sorted_words[:n]

# Test case that works (small dataset)
text1 = "hello world hello"
results = get_most_common(text1, 2)
print(results)  # Expected: [('hello', 2), ('world', 1)]
print(f'Expected [("hello", 2), ("world", 1)], but got {results}')

# Test case that fails
text2 = "the cat sat on the mat the dog ran fast the bird flew"
results = get_most_common(text2, 3)
print(results)
print(f'Expected [("the", 4), ("cat", 1), ("sat", 1)], but got {results}')
