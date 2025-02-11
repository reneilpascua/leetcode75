from typing import Dict, Tuple, List

class Solution_0:

    MOVES: List[Tuple] = [ # (d_row, d_col)
        (2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)
    ]
    NEIGHBOURS: Dict[Tuple, List[Tuple]] = dict() # to help cache neighbors

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.NEIGHBOURS.clear()
        def inside(r, c):
            return (0 <= r < n) and (0 <= c < n)

        if k == 0:
            return 1.0 if inside(row, column) else 0.0

        i = 0 # number of moves taken
        stack: List[Tuple] = [(row, column)] # valid positions after i moves

        def _add_new_positions(r, c):
            self.NEIGHBOURS[r,c] = []
            for move in self.MOVES:
                nr, nc = r+move[0], c+move[1]
                if inside(nr, nc):
                    self.NEIGHBOURS[r,c].append((nr, nc))

        def add_positions(r, c):
            if (r,c) not in self.NEIGHBOURS:
                _add_new_positions(r, c) # will fill out self.NEIGHBORS[(r,c)]
            
            for neighbor in self.NEIGHBOURS[(r,c)]:
                stack.append(neighbor)

        while i < k and stack:
            # unload the big stack into this iterative stack
            positions: List[Tuple] = []
            while stack:
                positions.append(stack.pop())

            for pos in positions:
                add_positions(*pos)
            i += 1
        
        return len(stack)/(8**i)
        

if __name__ == "__main__":
    n = 8
    k = 30
    row = 6
    column = 4
    sol = Solution_0()
    # MLE... stack is getting too big, need to find a way to decouple my sol
    # from individual positions and think about numbers from certain positions instead
    print(sol.knightProbability(n, k, row, column))