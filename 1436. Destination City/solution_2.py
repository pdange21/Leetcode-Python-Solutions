class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        outdegree = Counter()

        for u, v in paths:
            outdegree[u] += 1
            outdegree[v] += 0

        for key in outdegree.keys():
            if outdegree[key] == 0:
                return key