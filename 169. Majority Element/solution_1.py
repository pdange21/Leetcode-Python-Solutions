class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = Counter(nums)
        occ = len(nums) // 2

        for n, c in count.items():
            if c > occ:
                return n
        return -1 #this condition won't be executed as there will always be element repeated but keeping it for the safe side