class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        ans = 0

        nums.sort(reverse=True) #sorting the array in reverse

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                ans += i
        return ans