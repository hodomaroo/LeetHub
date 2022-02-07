class Solution(object):
    def findTheDifference(self, s, t):
        ans = 0
        for w in s + t: ans ^= ord(w)
        return chr(ans)


