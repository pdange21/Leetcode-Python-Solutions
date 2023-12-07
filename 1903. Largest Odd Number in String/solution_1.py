class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        #we will be starting on the right side of the string in reverse order

        for i in range(len(num) - 1, -1, -1): #iterating the string in reverse order
          if int(num[i]) % 2 != 0: #checking if the digit is odd
            return num[:i+1] #if it is odd we return from starting to this point
        return "" #we return empty string if we are not able get a odd integer in the string