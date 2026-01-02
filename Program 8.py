Given an array of T length each index contains array of two binary strings, your task is to return their maximum sum(Also a binary string).

First Line contains T array Length, next n lines contain two string which shows binary space separated m,n. Find the sum of m and n in binary and print the maximum binary sum from the array elements.

Input:
3
101 100
110 10
1000 11

output:
1011

# Program #

t = int(input())
ans =[]

for i in range(t):
    m, n = input().split()
    M = int(m, 2)
    N = int(n, 2)
    temp = M + N
    ans.append(temp)

print(ans)
print(max(ans))

print(bin(max(ans)))
