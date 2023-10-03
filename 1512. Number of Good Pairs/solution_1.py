class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        #Brute force approach with complexity O(n^2) for time
        res = 0

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res