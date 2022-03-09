class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [(-1,0)]    #인덱스는 -1로 취급
        answer = 0
        for i,height in enumerate(heights + [0]):
            while stack and stack[-1][1] > height:
                ri,rhei = stack.pop()   #popleft
                answer = max(answer,(i - stack[-1][0] - 1) * rhei)
            stack.append((i,height))
        return answer
                                
                
                
                
                
