class Solution:
    def reverseWords(self, s: str) -> str:
        #two pointer approach without using helper function

        s = list(s) #converting string to array so that we can use operation on it

        l = 0 #left pointer

        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1: #either we encouter space from where we need to reverse or the last character which is the edge case
                temp_l, temp_r = l, r - 1 # this is for space

                if r == len(s) - 1:
                    temp_r = r #last word reversing

                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r + 1

        return "".join(s) #converting the list back to string
        