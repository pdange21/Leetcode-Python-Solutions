class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        l = r = k #assigning the left and right pointer to k as this is the position we will start our iteration
        res = nums[k]
        cur_min = nums[k]

        while l > 0 or r < len(nums) - 1:
            left = nums[l - 1] if l > 0 else 0 #decrementing the left pointer and also handling edge case
            right = nums[r + 1] if r < len(nums) - 1 else 0 #incrementing the right pointer and also handling the edge case

            if left > right: #the left value is greater
                l -= 1
                cur_min = min(cur_min, left)

            else: # the right value is greater
                r += 1
                cur_min = min(cur_min, right) 

            res = max(res, cur_min * (r - l + 1))
        
        return res