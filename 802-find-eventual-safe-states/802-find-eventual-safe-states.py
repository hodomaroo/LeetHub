from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        finish = [False] * len(graph)
        visit = [False] * len(graph)
        dp = [True] * len(graph)

        def dfs(node : int):
            if finish[node]: return dp[node]

            visit[node] = True

            for nextnode in graph[node]:
                if not visit[nextnode]:
                    dp[node] = min(dfs(nextnode),dp[node])
                else:
                    dp[node] = min(dp[node],False if not finish[nextnode] else dp[nextnode])

            finish[node] = True
            return dp[node]

        for i in range(len(graph)):
            if finish[i]: continue
            dfs(i)

        return [i for i in range(len(graph)) if dp[i]]

