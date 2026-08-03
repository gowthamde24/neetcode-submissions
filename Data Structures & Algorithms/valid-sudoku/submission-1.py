import collections
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares =collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val==".":
                    continue

                if (curr_val in rows[r] or curr_val in cols[c] or curr_val in squares[(r//3,c//3)]):
                    return False

                rows[r].add(curr_val)
                cols[c].add(curr_val)
                squares[(r//3,c//3)].add(curr_val)

        return True

                

        
        