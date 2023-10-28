class Solution:
    def countVowelPermutation(self, n: int) -> int:

        dp = [[], [1, 1, 1, 1, 1]] # this is the mapping, it is empty for n=0, n=1 has all one values

        a, e, i, o, u = 0, 1, 2, 3, 4 #index mapping a maps to 0 index, e maps to 1 index and so on 

        mod = 10 ** 9 + 7 #mod value

        for j in range(2, n+1):
            dp.append([0,0,0,0,0]) #initially appending all the dummy values

            dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) % mod #these are the values that can be followed by a
            dp[j][e] = (dp[j-1][a] + dp[j-1][i]) % mod #these are the values that can be followed by e
            dp[j][i] = (dp[j-1][e] + dp[j-1][o]) % mod
            dp[j][o] = dp[j-1][i] #we are assuming any value stored in dp grid is already moded, so no mod needed
            dp[j][u] = (dp[j-1][i] + dp[j-1][o]) % mod
        
        return sum(dp[n]) % mod



        