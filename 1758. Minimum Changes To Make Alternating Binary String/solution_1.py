class Solution:
    def minOperations(self, s: str) -> int:

        #so in this approach we are assuming that the string in begining with 0 and the we are returning the min of count and len(s) - count to handle both the cases

        count = 0

        for i in range(len(s)):
            #we are iterating through the string 

            if i % 2 != 0: #odd index
                if s[i] == '0': #it is expected to be '1' so if it is '0' we increment the count
                    count +=1
            else: #even index
                if s[i] == '1': #in the even index position it is expected to be '0' so if it is '1' we increment the count
                    count += 1

        return min(count, len(s) - count) #we return the minimum of count and len(s) - count because we are assuming the string to begin with 0 so to handle the other case we have len(s) - count if it is the case to acheive the string with minimum operations