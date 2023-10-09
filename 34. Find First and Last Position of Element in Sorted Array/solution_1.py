class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # As the nums array is sorted the first thought that came in my mind is binary search
        left = self.binsearch(nums, target, True) #getting the left range
        right = self.binsearch(nums, target, False) #getting the right range

        return [left, right]
       
    def binsearch(self, nums, target, leftbias):
            l, r = 0, len(nums) - 1
            i = -1 #handling the null and not existing case

            while l <= r:
                m = (l + r) // 2

                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    i = m
                    if leftbias:
                        r = m -1
                    else:
                        l = m + 1
            return i

        