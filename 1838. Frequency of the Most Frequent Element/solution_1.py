class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  #sorting the list

        res, total = 0, 0
        l, r = 0, 0

        #(r - l + 1) is the size of the window
        while r < len(nums):

            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
            
        return res