from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        pos = [0]+rungs
        diffs = [p[1]-p[0] for p in zip(pos,pos[1:])]
        
        return sum([((diff-1)//dist if diff>dist else 0) for diff in diffs])


if __name__ == '__main__':
    pass
    ex1 = ([1,3,5,9], 2) # 2
    ex2 = ([3,6,8,10], 3) # 0
    ex3 = ([3,4,6,7], 2) # 1
    ex4 = ([3], 1) # 1
    print(Solution().addRungs(*ex4))