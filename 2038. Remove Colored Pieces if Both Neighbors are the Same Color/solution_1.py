class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        countAAA, countBBB = 0, 0 #initializing count

        for a, b ,c in zip(colors, colors[1:], colors[2:]):
            if a == b == c == 'A':
                countAAA += 1
            if a == b == c == 'B':
                countBBB += 1
        
        return countAAA > countBBB #returning winner