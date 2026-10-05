class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            num = {}

            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                num[value] = num.get(value, 0) + 1

                if num[value] > 1:
                    return False

        # Check columns
        for i in range(9):
            num = {}

            for j in range(9):
                value = board[j][i]

                if value == ".":
                    continue

                num[value] = num.get(value, 0) + 1

                if num[value] > 1:
                    return False

        # Check 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                num = {}

                for i in range(3):
                    for j in range(3):
                        value = board[box_row + i][box_col + j]

                        if value == ".":
                            continue

                        num[value] = num.get(value, 0) + 1

                        if num[value] > 1:
                            return False

        return True