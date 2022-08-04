class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcmVal = lcm(p,q)
        #q가 p를 몇번 왕복하는가? #lcm // q -> 딱 맞기까지 튕기는 횟수 
        
        if lcmVal // p % 2: #up 
            return 2 - (lcmVal // q) % 2
            
        else: #down #튕기는 횟수랑 관련이 있음
            return 0
            
            