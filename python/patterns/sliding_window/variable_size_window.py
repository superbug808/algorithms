#Problem: Longest Substring without repeating characters

#Description: Given a string s, find the length of the longest substring without repeating characters

def length_of_longest_substring(s):
    char_set = set()

    #left pointer
    l = 0

    #max length
    maxlen = 0

    for r in range(len(s)):
        while s[r] in char_set:
            #remove leftmost from tracker
            char_set.remove(s[l])

            #move pointer forward
            l += 1
        char_set.add(s[r])
        maxlen = max(maxlen, r - l + 1)
    return maxlen

if __name__ == "__main__":
    # Standard case
    print(f"Test 1 (Standard): {length_of_longest_substring('abcabcbb')}") 
    # Expected: 3 ('abc')

    # Edge Case: Empty string
    print(f"Test 2 (Empty String): {length_of_longest_substring('')}") 
    # Expected: 0

    # Edge Case: Single character
    print(f"Test 3 (Single Char): {length_of_substring_single := length_of_longest_substring('a')}") 
    # Expected: 1

    # Edge Case: All unique characters
    print(f"Test 4 (All Unique): {length_of_longest_substring('abcdef')}") 
    # Expected: 6 ('abcdef')

    # Edge Case: String with spaces
    print(f"Test 5 (With Spaces): {length_of_longest_substring('p w w k e w')}") 
    # Expected: 3 ('w k e' or 'k e w')