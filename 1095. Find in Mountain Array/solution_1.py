class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        #In this approach we use three binary search first to find the peak element, then we run binary search on the left portion and then binary search on the right portion

        length = mountain_arr.length() # getting the length of the array

        #Logic for finding the peak 
        l, r = 1, length - 2 #here we are assuming that the first and the last element cannot be the peak element as it has form a mountain
        while l <= r:
            m = (l + r) //2
            left, mid, right = mountain_arr.get(m - 1), mountain_arr.get(m), mountain_arr.get(m + 1)
            if left < mid < right: #we are in the left side of the mountain
                l = m + 1
            elif left > mid > right: #we are in the right side of the moutain
                r = m - 1
            else:
                break
        peak = m

        #Searching in the left portion
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        #Searching in the right portion
        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1

            
        