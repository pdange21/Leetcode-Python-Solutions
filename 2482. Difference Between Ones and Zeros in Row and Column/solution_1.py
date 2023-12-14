class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        R = len(grid)
        C = len(grid[0])

        rows = [0] * R
        cols = [0] * C

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        ans = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                ans[i][j] = rows[i] + cols[j] -(R - rows[i]) - (C - cols[j])
        
        return ans
        