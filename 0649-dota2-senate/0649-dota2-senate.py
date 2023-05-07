class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:           # current R being banned
                        ban_r -= 1
                        banned[i] = True
                    else:                   # if current R is valid, it will ban D
                        ban_d += 1
                        s.add('R')
                else:        
                    if ban_d > 0:           # current D being banned
                        ban_d -= 1
                        banned[i] = True
                    else:                   # if current D is valid, it will ban R
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'