class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = "" #initializing res as an empty string this will store the palindrome string
        resLen = 0 #initializing this to 0

        #handling the no palindrome case
        if len(s) == 1:
            return s #in the case of single character in the string return the string


        for i in range(len(s)): #iterating through the string

            #handling string with odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1] #appending the palindrome string to the res
                    resLen = r - l + 1
                l -= 1 #decrementing the left pointer
                r += 1 #incrementing the right pointer

            #handling string with even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1  # Add this line to update resLen
                l -= 1 #decrementing the left pointer
                r += 1 #incrementing the right pointer


        return res #returning the longest palindrome string