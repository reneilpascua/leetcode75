from heapq import heapify, heappop, heappush

# used heap because i got this q from the heap problem series... got TLE 
class MedianFinder_Heap:

    def __init__(self):
        self.size = 0
        self.heap = [] # has a semblance of order while pushing to it

    def addNum(self, num: int) -> None: # O(logn)
        heappush(self.heap, num)
        self.size += 1

    def findMedian(self) -> float: # O(nlogn)
        # create a copy of self.heap so you can modify it
        h = self.heap[:]
        i = 0
        cur = 0
        while i < self.size//2:
            cur = heappop(h)
            i += 1
        return (cur + h[0])/2 if self.size%2 == 0 else h[0]

# used list this time, and still TLE, but went farther than the heap one
class MedianFinder_List:

    def __init__(self):
        self.size = 0
        self.nums = []

    def addNum(self, num: int) -> None: # O(n)
        if not self.size:
            self.nums = [num]
            self.size = 1
            return

        i = 0
        while num > nums[i]:
            i += 1
        self.nums = self.nums[:i] + [num] + self.nums[i:]
        self.size += 1


    def findMedian(self) -> float: # O(1)
        # assume this won't be asked when stream size is 0
        m = self.size//2
        return (self.nums[m] + self.nums[m-1])/2 if self.size%2 == 0 else self.nums[m]


# ok so heapify is only O(n), maybe use that knowledge to make this better
# TLE as well, made it to the same testcase as the _Heap version.
class MedianFinder_Heapify:

    def __init__(self):
        self.size = 0
        self.nums = [] # unordered list

    def addNum(self, num: int) -> None: # O(1)
        self.nums.append(num)
        self.size += 1

    def findMedian(self) -> float: # O(nlogn)
        # heapify self.nums and then extract from it
        nums = self.nums[:]
        heapify(nums) # O(n)

        i = 0
        cur = 0
        while i < self.size//2: # O(nlogn)
            cur = heappop(nums)
            i += 1
        return (cur + nums[0])/2 if self.size%2 == 0 else nums[0]


# TWO HEAP SOLUTION, this is so smart
class MedianFinder:

    def __init__(self):
        self.left = [float('inf')] # max heap, add negatives to this
        self.right = [float('inf')] # min heap
        self.size = 0

    def addNum(self, num: int) -> None: # O(logn)
        # peek at both
        left_max = -self.left[0]
        right_min = self.right[0]
        
        # 4 cases:
        # 1) size is even (want to add to self.right)
        #   a) number is smaller than left_max (reshuffle)
        #   b) number is bigger than or eq left_max (all good)
        # 2) size is odd (want to add to self.left)
        #   a) number is bigger than right_min (reshuffle)
        #   b) number is smaller than or eq right_min (all good)

        # EDIT: this if/else BS can be replaced by "heappushpop"...

        if self.size%2 == 0:
            if num < left_max: # reshuffle
                temp = -heappop(self.left)
                heappush(self.left, -num)
                heappush(self.right, temp)
            else: # num >= left_max, all good
                heappush(self.right, num)
        else:
            if num > right_min: # reshuffle
                temp = heappop(self.right)
                heappush(self.right, num)
                heappush(self.left, -temp)
            else: # num <= right_min, all good
                heappush(self.left, -num)
        self.size += 1

    def findMedian(self) -> float: # O(1)
        # remember to minus from self.left bc it uses negative nums
        return (self.right[0]-self.left[0])/2 if self.size%2 == 0 else self.right[0]
