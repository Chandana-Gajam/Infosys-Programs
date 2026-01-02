You have a array you need to perform the given task:

1. If the array length is greater than 1 then take any two numbers which are X != Y and remove X and Y
2. Else take X and remove X
Count the minimum number of step to remove all element from list.

I/P:12

O/P: 1
I/P: 22

O/P: 2
I/P: 22331

O/P: 3 (2,3)(2,3)(1)

# Program #

n = int(input())
arr = list(map(int, input().split()))
ans = 0
arr.sort()
while len(arr) != 0:
    if arr[0] != arr[-1]:
        arr.pop()
        arr.pop(0)
    else:
        arr.pop(0)
    ans += 1

print(ans)                    
