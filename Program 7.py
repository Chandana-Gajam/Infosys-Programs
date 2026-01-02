Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index 1 1 on the next row.

Example 1:

Input: triangle = [12],[3,4], [6,5,7), (4,1,8,31]

Output: 11

Explanation: The triangle Looks Like:
                                  2
                                3   4
                             6    5    7
                          4     1    8     3 

# Program #

from typing import List
def minimmTotal(self,triangle: List[List[int]]) ->int:
    n=len(triangle)

    for i in range(n-2,-1,-1):
        m=len(triangle[i])


        for  j in range(m):
            left=triangle[i+1][j]
            right=triangle[i+1][j+1]

            triangle[i][j] +=min(left,right)
    

    return triangle[0][0]
