class Solution:
    def knightDialer(self, n: int) -> int:

        if n ==1:
            return 10
        
        mod = 10 ** 9 + 7

        A = 4
        B = 2
        C = 2
        D = 1

        for _ in range(n-1):
            A,B,C,D = (2*(B+C)) % mod, A, (A+2*D) % mod, C
        
        return (A+B+C+D) % mod