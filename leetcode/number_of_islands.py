class Solution:

    def number_islands(self, grid: list) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    count += 1
                    self.remove_islands(x, y, grid)
        return count

    def is_outside_border(self, x, y, grid: list) -> bool:
        if x > len(grid[0]) - 1 or y > len(grid) - 1:
            return True
        return False

    def remove_islands(self, x, y, grid: list) -> list:
        steps = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        )

        if grid[x][y] == '1':
            grid[x][y] = '#'
            for new_x, new_y in steps:
                new_x += x
                new_y += y
                if not self.is_outside_border(new_x, new_y, grid):
                    self.remove_islands(new_x, new_y, grid)
        return grid


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
solution = Solution()
print(solution.number_islands(grid))
print(grid)
