class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        return n > 0 and log(n, 4) % 1 == 0
        #the above condition checks if n is not negative and the log to the base 4 is an integer