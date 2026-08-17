class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                square_id = (r // 3) * 3 + (c // 3)
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[square_id]):
                    return False    
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[square_id].add(board[r][c])
        
        return True