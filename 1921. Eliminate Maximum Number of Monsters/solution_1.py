class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        #building the minutes reached array which is basically the d/s

        min_reach = []

        for d,s in zip(dist, speed):
            minutes = math.ceil(d/s)
            min_reach.append(minutes)
        
        min_reach.sort() #sorting the array to eliminate the fastest comming monster
        res = 0 #counts the monster which are eliminated

        for minute in range(len(min_reach)):
            if minute >= min_reach[minute]:
                return res
            res += 1
        return res
