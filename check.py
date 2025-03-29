from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for i in range(len(board)):
            sub_list = []
            for j in range(len(board)):
                sub_list.append(board[i][j])

            print(sub_list)
            for sub in sub_list:
                if sub_list.count(sub) > 1 and sub != '.':
                    return False

        for j in range(len(board)):
            sub_list = []
            for i in range(len(board)):
                sub_list.append(board[i][j])

            for sub in sub_list:
                if sub_list.count(sub) > 1 and sub != '.':
                    return False

        return True


a = Solution()
print(a.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                       [".", "4", ".", "3", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                       ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                       [".", ".", "2", ".", "7", ".", ".", ".", "."],
                       [".", "1", "5", ".", ".", ".", ".", ".", "."],
                       [".", ".", ".", ".", ".", "2", ".", ".", "."],
                       [".", "2", ".", "9", ".", ".", ".", ".", "."],
                       [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
