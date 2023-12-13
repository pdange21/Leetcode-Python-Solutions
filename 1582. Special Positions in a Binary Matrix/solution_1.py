class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        r = len(mat) #no of rows
        c = len(mat[0]) #no of columns

        rows = [0] * r
        cols = [0] * c

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count