class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
#현재 가능한 가장 작은걸로 점수를 얻고 -> 더 큰놈으로 power 얻기?
        maxHeap = []
        minHeap = []
        
        tokens.sort()
        score = 0
        ans = 0
        left,right = 0, len(tokens) - 1
        
        while left < len(tokens):
            while left < len(tokens) and power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            
            ans = max(ans, score)
            
            if not score:   break
            power += tokens.pop()
            score -= 1
            
            
        return ans
                
    