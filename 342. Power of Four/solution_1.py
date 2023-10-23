class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        #recursive solution

        if n == 1:
            return True
        if n <= 0 or n % 4:
            return False
        
        return self.isPowerOfFour(n // 4)