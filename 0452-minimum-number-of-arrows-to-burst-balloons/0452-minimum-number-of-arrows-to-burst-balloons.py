class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        lineStart = sorted([(i,v[0]) for i,v in enumerate(points)], reverse = True, key = lambda x : x[1])
        lineEnd = sorted([(i,v[1]) for i,v in enumerate(points)],key =  lambda x : x[1])
        
        
        dead = set()
        pop = 0
        
        for i,v in lineEnd:
            if i in dead: continue
            pop += 1
            
            dead.add(i)
            
            while lineStart and v >= lineStart[-1][1]:
                dead.add(lineStart.pop()[0])
                
            if not lineStart:
                return pop
        
                
                
            
        
        
        
        
    
                    
        