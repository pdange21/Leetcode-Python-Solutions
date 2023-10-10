class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums) #getting the size of the nums array
        nums = sorted(set(nums)) #making it unique and sorted
        res = n
        r = 0

        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l] + n:
                r += 1
            window = r - l
            res = min(res, n - window)
        return res