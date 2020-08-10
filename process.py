
class Solve:
    def __init__(self, path):
        self.INF = 10**9
        self.row = 0
        self.col = 0
        self.tot_v = 0
        self.parent = []
        self.visited = []
        self.graph = path[:]
        # self.sol()

    def print_mat(self):
        for row in self.graph:
            print(row)

    def dfs(self, edge, v):
        self.visited[v] = 1
        for i in range(self.tot_v):
            if edge[v][i] > 0:
                if self.visited[i] == 0:
                    self.parent[i] = v
                    self.dfs(edge, i)

    def dfs_driver(self, edge, s, t):
        self.visited = [0 for _ in range(self.tot_v)]
        self.parent = [-1 for _ in range(self.tot_v)]
        # for i in range(self.tot_v):
        #     self.visited[i] = 0
        #     self.parent[i] = -1
        self.dfs(edge, s)
        return self.visited[t] == 1

    def ford(self, s, t):
        # print(s,t)
        rGraph = self.graph[:]
        max_flow = 0

        while self.dfs_driver(rGraph, s, t):
            path_flow = self.INF
            v = t
            while v != s:
                u = self.parent[v]
                path_flow = min(path_flow, rGraph[u][v])
                v = self.parent[v]

            v = t
            while v != s:
                u = self.parent[v]
                rGraph[u][v] -= path_flow
                rGraph[v][u] += path_flow
                v = self.parent[v]
            max_flow += path_flow
        return max_flow

    def sol(self, s, t):
        self.row = len(self.graph)
        self.col = len(self.graph[0])
        self.tot_v = self.row
        # self.print_mat()
        return self.ford(s, t)


def solution(path, s, t):
    soln = Solve(path)
    max_flow = soln.sol(s, t)
    return max_flow
