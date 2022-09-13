class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = data[::-1]
        
        length = 0
        
        while data:    
            for i in range(8):
                if not (data[-1] >> (7 - i)) & 1: break                
            data.pop()

            if i == 1 or i > 4 or len(data) < i - 1:  return False
            
            for _ in range(i - 1):
                if (data.pop() >> 6) != 2: return False
                
        return True
            
            