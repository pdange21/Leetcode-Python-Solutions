class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #This is two pointer quicksort approach where we have left, and right pointer and if it is number at right is even we swap it with left
        #The space complexity is O(1) and the time complexity is O(n)
        l = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 0: #checking if the number is even
                nums[l], nums[r] = nums[r], nums[l] #swapping the elements
                l += 1 #incrementing the left pointer
        return nums