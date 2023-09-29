class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        #brute force approach
        nums_asc = sorted(nums)
        nums_desc = sorted(nums, reverse=True)

        if nums == nums_asc or nums == nums_desc:
            return True
        else:
            return False