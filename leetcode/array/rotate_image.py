import copy


class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

    def rotate_1(self, matrix: list) -> None:
        length = len(matrix)
        for i in range(length // 2 + length % 2):
            for j in range(length // 2):
                target = matrix[i][i + j]
                matrix[i][i + j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = target

    def rotate_brute_force(self, matrix: list) -> None:
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                matrix[i][j], matrix[length - 1 - j][i] = matrix[length - 1 - j][i], matrix[i][j]


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

solution = Solution()
solution.rotate_1(matrix=matrix)
print(matrix)
# output = [[15,13,2,5],[14,4,8,1],[12,3,6,9],[16,7,10,11]]
