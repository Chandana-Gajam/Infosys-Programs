def shiftCards(cards, s, target):
    e=cards.index(target)
    n=len(cards)


    if e==s:
        return 0
    
    if abs(s-e)==1:
        return 1
    
    if s<e:
        forward=e-s
        backward=s+(n-1-e)+1
    else:
        forward=e+(n-1-s)+1
        backward=s-e
    return min(forward,backward)

n=int(input())
cards=input().split()
s=int(input())
target=input()
print(shiftCards(cards, s, target))