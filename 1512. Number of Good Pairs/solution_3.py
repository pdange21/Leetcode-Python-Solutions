class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        res = 0 #initial res = 0

        count = {} #Hashmap

        for n in nums: #iterate through the array
            if n in count: #if it already exist
                res += count[n] #we add the count till this occurence
                count[n] += 1 #increment the counter in the hashmap
            else:
                count[n] = 1 #this element does not exist in the hashmap so we add it
        return res
        