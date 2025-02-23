from typing import List
from heapq import heappop, heappush
from sys import getsizeof

from utils.performance import timer
from utils.temp_testcase import buildings

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # create sorted list of left-biased segments from buildings (L,R,H)
        # switch places for R and H --> (L,H,R) so that H is the second sort var.
        # the right side of a building is the left of imaginary building with H=0
        segments = sorted(
            # use -h bc gonna use max heap          inf is placeholder
            [(l,-h,r) for l,r,h in buildings] + [(r,0,'inf') for _,r,__ in buildings]
        )

        ans = [[0,0]]
        max_heap = [(0, float('inf'))] # (negative height, x)
        # priority is biggest height, then leftest x.
        
        for x, negH, r in segments:
            while x >= max_heap[0][1]:
                heappop(max_heap)
                # only care about heap items to the right of x
            if negH: # non-zero height
                heappush(max_heap, (negH, r)) # why r? because
                # later, when we process x2 < r1, we may see that it is towered
                # by a building from x1 where h1>h2 (due to max heap)
            max_at_x = -max_heap[0][0] # the earlier popping ensures this.
            if ans[-1][1] != max_at_x:
                ans.append([x, max_at_x])
            # else it's the same height and part of the same continuous seg
        return ans[1:] # dont include the origin
    
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
    # buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    # buildings2 = [[0,2,3],[2,5,3]]
    # buildings3 = [[0,2,3],[2,4,3],[4,6,3]]
    # print(Solution().getSkyline(buildings1))
    # print(Solution().getSkyline(buildings2))
    # print(Solution().getSkyline(buildings3))
    
    # big test case:
    print(Solution().getSkyline(buildings))

if __name__ == '__main__':
    main()