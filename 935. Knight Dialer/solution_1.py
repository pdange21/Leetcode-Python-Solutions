class Solution:
    def knightDialer(self, n: int) -> int:

        if n == 1:
            return 10

        mod = 10 ** 9 + 7

        jumps = [
            [4,6], #0 from 0 we can go to 4 and 6
            [6,8], #1
            [7,9], #2
            [4,8], #3
            [0,3,9], #4
            [], #5
            [0,7,1],#6
            [2,6], #7
            [1,3], #8
            [2,4] #9
        ]

        dp = [1] * 10 #ways to land on ith digit
        for _ in range(n-1):
            next_dp = [0] * 10
            for n in range(10):
                for j in jumps[n]:
                    next_dp[j] = (next_dp[j] + dp[n]) % mod
            dp = next_dp

        return sum(dp) % mod
        