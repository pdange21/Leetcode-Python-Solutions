class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        total_sum = sum(nums)
        left_sum = 0
        res = []

        for i, n in enumerate(nums):

            right_sum = total_sum - n - left_sum

            res.append(i*n - left_sum + right_sum - (len(nums)-i-1)*n)

            left_sum += n

        return res
        