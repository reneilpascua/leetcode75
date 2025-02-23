from typing import List
from heapq import heappop, heappush
from sys import getsizeof

from utils.performance import timer
from utils.temp_testcase import buildings

class Solution:
    
    
    def getSkyline_1(self, buildings: List[List[int]]) -> List[List[int]]:
        print(f'buildings is {len(buildings)} long')
        points_set = set()
        for l, r, _ in buildings:
            points_set.add(l)
            points_set.add(r)
        
        points = sorted(list(points_set))
        del points_set
        np = len(points)
        print(f'points is {len(points)} long')
        # print(f'points size = {getsizeof(points)}') # 80KB

        heap = []
        j = 0 # iteration offset
        ans = []
        seen = set()
        def pop_to_ans():
            nonlocal heap, j, ans, seen
            cur = heappop(heap)
            seen.add(cur[0])
            if (not ans) or (-cur[1] != ans[-1][1]):
                ans.append((cur[0], -cur[1]))
            while heap and (heap[0][0] == cur[0]): # eliminate the rest of the heap on this x
                heappop(heap)


        LIMIT = 5
        for k, (l, r, h) in enumerate(buildings):
            if k > LIMIT: break
            while j < np and points[j] < l:
                pop_to_ans()
                j += 1

            i = j
            while i < np and l <= points[i] < r:
                heappush(heap, (points[i], -h))
                i += 1
            heappush(heap, (r, 0))
            print(f'ans after step {k}: {ans}')
            # print(f'heap after step {k}: {heap}')
            # print(f'size after step {k}: {getsizeof(heap)}')
        
        while heap: # add the rest that wasn't processed in the loop
            pop_to_ans()
            
        return ans # still MLE


    def getSkyline_0(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for l, r, _ in buildings:
            points.append(l)
            points.append(r)
        points.sort()
        np = len(points)
        # print(f'points = {getsizeof(points)}') # 173KB

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
        # print(f'heap = {getsizeof(heap)}') # 411MB

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
        return ans # MLE (heap is gigantic)

@timer
def main():
    buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    buildings2 = [[0,2,3],[2,5,3]]
    buildings3 = [[0,2,3],[2,4,3],[4,6,3]]
    Solution().getSkyline_0(buildings1)
    Solution().getSkyline_0(buildings2)
    Solution().getSkyline_0(buildings3)
    
    # big test case:
    # Solution().getSkyline(buildings)

if __name__ == '__main__':
    main()