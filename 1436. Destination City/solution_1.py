class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        source_set = set() #this hash set will contain all the source location

        for p in paths:
            source_set.add(p[0]) #adding the source to the source_set as it is in p[0] location

        for p in paths: 
            if p[1] not in source_set: #checking if the destination is in the source hash set
                return p[1] #if not we return that element