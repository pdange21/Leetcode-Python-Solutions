class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        events = collections.defaultdict(list)
        NP = len(people)
        F = 0
        P = 1

        for s, e in flowers:
            events[s].append((F, +1))
            events[e + 1].append((F, -1))


        for index, p in enumerate(people):
            events[p].append((P, index))


        ans = [None] * NP
        current = 0
        for k in sorted(events.keys()):
            events[k].sort()

            for t, p in events[k]:
                if t == F:
                    current += p
                else:
                    ans[p] = current
        return ans        