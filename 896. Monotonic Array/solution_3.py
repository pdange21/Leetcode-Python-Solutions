class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] - nums[0] > 0: #this puts the array in increasing order if it is not
            nums.reverse()
        
        for i in range(len(nums) -1): 
            if not(nums[i] >= nums[i+1]): #if it is not in increasing order we return false
                return False
        return True