class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        #Hashmap to get the number and occurence
        count = Counter(nums)
        res = 0

        for n, c in count.items(): #Iterate through the hashmap
            res += c * (c - 1) // 2
        return res
        