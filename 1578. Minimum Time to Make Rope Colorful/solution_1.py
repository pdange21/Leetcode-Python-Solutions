class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        #one thing we should remember is to remove the element with the lowest needTime because we are minimizing this result

        res = 0 #initializaing the result to 0

        #we will be taking a two pointer approach where the left pointer starts from 0 and right from 1 and when we encounter same color i.e same element we add the minimum to res

        l = 0 #initializing the left pointer

        for r in range(1, len(colors)):

            if colors[l] == colors[r]:
                #if the elements are same

                if neededTime[l] < neededTime[r]:
                    res += neededTime[l] #adding the min element to the res
                    l = r #modifying the pointer
                else:
                    res += neededTime[r] #adding the min element ot the res

            else:
                l = r #the elements are not same so we modify the left pointer and keep iterating
        return res