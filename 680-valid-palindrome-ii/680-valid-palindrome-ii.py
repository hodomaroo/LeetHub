from collections import deque
class Solution:
    def validPalindrome(self, s: str) -> bool:
        q = deque([(0,len(s)-1,0)])

        while q:
            l,r,cnt = q.popleft()
            if r <= l: return True
            if s[l] == s[r]:
                q.append((l + 1, r - 1, cnt))
            elif not cnt:
                q.append((l + 1, r, 1))
                q.append((l, r - 1, 1))
        return False



