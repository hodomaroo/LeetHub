class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [v for v in path.replace("//","/").split("/") if v and v != '.']
        stack = []
        for v in path:
            if v == "..":
                if stack:   stack.pop()
            else:
                stack.append(v)
        
        return "/" + "/".join(stack)
        

        
        
        
                    
            
            
            
                
            
            
            
            
            