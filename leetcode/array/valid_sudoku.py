class Solution:

    def is_valid_sudoku(self, board: list) -> bool:
        column = {i: set() for i in range(9)}
        square = {i: set() for i in range(9)}
        for big_index, line in enumerate(board):
            row = set()
            for index, item in enumerate(line):
                if item != '.':
                    if item not in row:
                        row.add(item)
                    else:
                        return False
                    if item not in column[index]:
                        column[index].add(item)
                    else:
                        return False
                    square_index = index // 3
                    if 3 <= big_index < 6:
                        square_index += 3
                    elif big_index >= 6:
                        square_index += 6
                    if item not in square[square_index]:
                        square[square_index].add(item)
                    else:
                        return False
        return True

    def _brute_force_validator(self, board: list) -> bool:
        output = True
        for row in board:
            nums = []
            for item in row:
                if item in nums:
                    output = False
                    break
                elif item != ".":
                    nums.append(item)
        return output

    def _brute_force_validate_squares(self, board: list) -> list:
        new_board = []
        for i in range(0, 7, 3):
            counter = 0
            mega = []
            new_mega = []
            m, n, l = [i for i in board[i:i + 3]]
            for a, b, c in zip(m, n, l):
                counter += 1
                if counter <= 3:
                    mega += [a, b, c]
                else:
                    counter = 0
                    new_mega.append(mega)
                    mega = [a, b, c]
            new_mega.append(mega)
            new_board += (new_mega)
        return new_board

    def is_valid_sudoku_brute_force(self, board: list) -> bool:
        # check if any rows are invalid
        output = True
        output = self._brute_force_validator(board)
        if not output:
            return output
        new_board = []
        for a, b, c, d, e, f, g, h, i in board:
            new_board.append([a, b, c, d, e, f, g, h, i])
        output = self._brute_force_validator(new_board)
        if not output:
            return output
        new_board = self._brute_force_validate_squares(board)
        output = self._brute_force_validator(new_board)
        return output


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

solution = Solution()
print(solution.is_valid_sudoku(board))
