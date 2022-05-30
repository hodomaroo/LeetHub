class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for word in list(s):
            if not stack or stack[-1][0] != word:
                stack.append([word,1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        return "".join([v * c for v,c in stack])
            
                