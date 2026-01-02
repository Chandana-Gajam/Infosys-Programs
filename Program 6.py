M = int(input())
min_base = 2

def all_digits_same(M, B):
    digits = []
    temp = M
    while temp > 0:
        digits.append(temp % B)
        temp //= B
    return len(set(digits)) == 1

for B in range(min_base, M):
    if all_digits_same(M, B):
        print(B)
        break        
