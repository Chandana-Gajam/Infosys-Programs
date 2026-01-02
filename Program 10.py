You are playing a card game where n cards of different colors are arranged in a list on a circular table. The player must move one card at a time, either to left or right. Since the cards are in a circular list, when the last card is reached in either direction, the next card is at the other end of the list.

You are given with one card color and one card index, determine the minimum number of left or right moves to reach the given target card from the given start index

Constraints:

1<=n<=100

0<=startIndex<= n-1

1<= card[i] & targetCard <=100

I/P:
4
["red", "blue", "green", "yellow"]
1
"yellow"
O/P:
2
I/P:
5
["black", "grey", "brown", "red", "pink"]
3
"black"
O/P:
2

# Program #

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
