class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #First we append the 0 to the end because that is the location we want to reach, that is the goal

        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1): #we start from the second last element and iterate in reverse order till the first element
            cost[i] += min(cost[i+1], cost[i+2]) #min cost of single and double jump
        return min(cost[0], cost[1]) #return the minimum cost