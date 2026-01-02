You are given a string consisting of lowercase characters only. The letters can be duplicate or non-duplicate. Duplicate letters have multiple copies present in the string, where the non-duplicates are unique and occur once. Your task is to return the index of the first non-duplicate letter present in the string if we traverse it from left to right. Use the indexing starting from 1. If no such letter is present return -1. Constraints: 1<= length of the string <= 10^5

I/P: statistics
O/P: 3
I/P: hackthegame
O/P: 3

# Program #

def firstUniqueChar(s):
    count = {}
    for char in s:
        count[char] = count.get (char, 0) + 1

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i+ 1

    return -1

s= input() 

print(firstUniqueChar(s))
