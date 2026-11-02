class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashes_row = [set() for i in range(9)]
        hashes_col = [set() for i in range(9)]
        hashes_square = [[set() for _ in range(3)] for _ in range(3)]
        sq_i,sq_j=0,0
        for i in range(9):
            sq_i = i//3
            for j in range(9):
                curr = board[i][j]
                if curr==".":continue
                if curr in hashes_row[i] or curr in hashes_col[j]  :
                    # print(hashes_row)
                    # print(hashes_col)
                    # print(curr)
                    return False
                hashes_row[i].add(curr)
                hashes_col[j].add(curr)
                sq_j =j//3
                if curr in hashes_square[sq_i][sq_j] :
                    # print(hashes_square)
                    # print( hashes_square[sq_i][sq_j],curr)
                    return False
                hashes_square[sq_i][sq_j].add(curr)
           
        return True
                