class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # set has O(1) membership check
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9): # 1 pass over grid
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]): # <-- see key
                    return False # num already in this row, col, square

                cols[c].add(board[r][c]) # add num to this row, col, square
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True