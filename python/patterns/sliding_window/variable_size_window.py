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