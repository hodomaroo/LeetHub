from heapq import heappop,heappush

class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        def dijkstra(node,Graph):
            heap = []
            heappush(heap, (0, node))
            visit = [False for _ in range(n)]
            dist = [float("inf") for _ in range(n)]
            dist[node] = 0

            while heap:
                cost, node = heappop(heap)
                #print(cost,node)
                if visit[node]: continue
                visit[node] = True

                for nextnode, pay in Graph[node]:
                    nextcost = cost + pay

                    if not visit[nextnode] and dist[nextnode] > nextcost:
                        dist[nextnode] = nextcost
                        heappush(heap, (nextcost, nextnode))
            return dist

        graph = [set() for _ in range(n)]
        rv_graph = [set() for _ in range(n)]
        for f,t,w in edges:
            graph[f].add((t,w))
            rv_graph[t].add((f,w))   #역간선그래프 구현
        #print(graph)

        c1 = dijkstra(src1,graph)
        c2 = dijkstra(src2, graph)
        c3 = dijkstra(dest, rv_graph)
        #print(c1,c2,c3)

        ans = float("inf")
        for i in range(n):
            ans = min(ans,c1[i] + c2[i] + c3[i])
        return ans if ans != float("inf") else -1




