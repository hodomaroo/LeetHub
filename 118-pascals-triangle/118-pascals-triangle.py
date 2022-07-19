class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            
            arr.append([1])
            for j in range(1,i):                
                arr[i].append(arr[i-1][j] + arr[i-1][j-1])
            
            if i:
                arr[i].append(1)
        return arr
            
                
            
            