from collections import deque
class Solution(object):
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]
        for f,t in connections:
            graph[f].append([t, True])
            graph[t].append([f, False])
        cost = 0

        q = deque()
        q.append((0))
        ans = 0
        visit = [0 for _ in range(n)]
        visit[0] = True
        while q:
            node = q.popleft()

            for nextnode,cost in graph[node]:
                if visit[nextnode]: continue
                visit[nextnode] = True
                ans += cost
                q.append(nextnode)
        return ans

