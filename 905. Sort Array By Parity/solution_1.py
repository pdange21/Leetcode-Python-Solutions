class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        #This was the first idea of implementation the approach here is to iterate through the given array and split it into two parts even and odd and in the end merge it in the order of even+odd.
        #The space and time complexity of this solution is O(n)
        nums_even = []
        nums_odd = []

        for n in nums:
            if n % 2 == 0:
                nums_even.append(n)
            else:
                nums_odd.append(n)   
        return (nums_even + nums_odd)
        