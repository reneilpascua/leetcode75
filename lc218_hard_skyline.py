from typing import List
from heapq import heappop, heappush

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for l, r, _ in buildings:
            points.append(l)
            points.append(r)
        points.sort()
        np = len(points)

        heap = []
        j = 0 # iteration offset
        for l, r, h in buildings:
            while j < np and points[j] < l:
                j += 1

            i = j
            while i < np and l <= points[i] < r:
                heappush(heap, (points[i], -h))
                i += 1
            heappush(heap, (r, 0))
        
        # now you have a heap with the correct answers in it, just pick out the right ones.
        cur = heappop(heap)
        ans = [(cur[0], -cur[1])]
        seen = {cur[0]}
        while heap:
            cur = heappop(heap)
            if cur[0] in seen: continue
            seen.add(cur[0])
            if -cur[1] != ans[-1][1]:
                ans.append((cur[0], -cur[1]))
        return ans # MLE