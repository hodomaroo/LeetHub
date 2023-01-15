class UF:
    def __init__(self, n):
        self.root = list(range(n))
    def find(self, x):
        if self.root[x] != x: self.root[x] = self.find(self.root[x])
        return self.root[x]

class Solution:
    def numberOfGoodPaths(self, V: List[int], E: List[List[int]]) -> int:
        N  = defaultdict(set)
        ans, uf = len(V), UF(len(V))
        for a, b in E:
            N[a].add(b)
            N[b].add(a)    
        dic = defaultdict(dict)
        for i, v in enumerate(V):
            dic[i][v] = 1

        for val, cur in sorted([v, i] for i, v in enumerate(V)):
            for nxt in N[cur]:
                root_nxt, root_cur = uf.find(nxt), uf.find(cur)
                if V[nxt] <= val and root_nxt != root_cur:
                    uf.root[root_cur] = root_nxt
                    ans += dic[root_cur][val] * dic[root_nxt].get(val, 0)
                    dic[root_nxt][val] = dic[root_nxt].get(val, 0) + dic[root_cur][val]
		
        return ans