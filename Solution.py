from typing import List
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        max_y = len(board)
        max_x = len(board[0])
        new_board = copy.deepcopy(board)

        print("Source:")
        for row in board:
            print(row)
            
        for i in range(max_y):
            for j in range(max_x):
                x_count = 0
                if board[i][j] == "O":
                    if i == 0:
                        x_count += 1000
                    elif board[i - 1][j] == "X":
                        x_count += 1000

                    if i == (max_y - 1):
                        x_count += 100
                    elif board[i + 1][j] == "X":
                        x_count += 100

                    if j == 0:
                        x_count += 10
                    elif board[i][j - 1] == "X":
                        x_count += 10
                    if j==(max_y-1):
                        x_count+=1
                    elif board[i][j+1] == "X":
                        x_count+=1

                    if x_count!=1111:
                        print(i,j)
                        new_board[i][j] = "M"

        board = copy.deepcopy(new_board)


if __name__ == "__main__":
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solution = Solution()
    solution.solve(board)
    print("Result:")
    for row in board:
        print(row)
