class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #requires slightly more space
        count = Counter(nums)
        occ = len(nums) // 3
        res = []

        for n, c in count.items():
            if c > occ:
                res.append(n)
        return res