class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[0] * i for i in range(1, numRows + 1)]
        
        for i in range(numRows):
            arr[i][0] = arr[i][-1] = 1
            
            for j in range(1,i):                
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

        return arr
            
                
            
            