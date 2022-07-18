from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i:
                    matrix[i][j] += matrix[i - 1][j]

        count = 0
        for i in range(len(matrix)):
            for j in range(i + 1): #구간 한정하기 [j, i]
                diction = {0 : 1}
                tot = 0
                for k in range(len(matrix[0])):
                    tot += matrix[i][k]
                    
                    if j: 
                        tot -= matrix[j - 1][k]
                    
                    
                    if tot - target in diction:
     #                   print(i,j,k)
                        count += diction[tot - target]
                    
                    if tot not in diction:
                        diction[tot] = 1
                    else:
                        diction[tot] += 1
                        
                    
                    
                    
                    
       #         print(diction)
        return count
# 010
# 111
# 010