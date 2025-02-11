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
        positions: List[Tuple] = [(row, column)] # valid positions after i moves

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
                positions.append(neighbor)

        while i < k and positions:
            # unload the big stack into this iterative stack
            new_positions: List[Tuple] = []
            while positions:
                new_positions.append(positions.pop())

            for pos in new_positions:
                add_positions(*pos)
            i += 1
        
        return len(positions)/(8**i)

class Solution:
    
    MOVES: List[Tuple] = [ # (d_row, d_col)
        (2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)
    ]
    
    def knightProbability(self, n, k, row, column):
        # avoid mle by only keeping track of the current and next dp
        # and only the number of ways to reach a certain position
        # then sum the valid ending positions, divide by 8**k
        
        def inside(r, c):
            return (0 <= r < n) and (0 <= c < n)
        
        dp = [[0]*n for _ in range(n)]
        dp[row][column] = 1
        i = 0
        while i < k:
            dp_next = [[0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for move in self.MOVES:
                        nr, nc = r+move[0], c+move[1]
                        if inside(nr, nc):
                            dp_next[nr][nc] += dp[r][c]
            dp = dp_next
            i += 1
        
        return sum(sum(row) for row in dp) / (8**k)


if __name__ == "__main__":
    n = 8
    k = 10
    row = 6
    column = 4
    
    # sol = Solution_0()
    # MLE... positions list is getting too big, need to find a way to decouple my sol
    # from individual positions and think about numbers from certain positions instead
    
    sol = Solution()
    print(sol.knightProbability(n, k, row, column))