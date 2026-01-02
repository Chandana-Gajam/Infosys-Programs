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