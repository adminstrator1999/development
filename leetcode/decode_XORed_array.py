class Solution:
    def decode(self, encoded: list, first: int) -> list:
        decoded = [first]
        for i in encoded:
            decoded.append(i ^ decoded[-1])
        return decoded


encoded = [6, 2, 7, 3]
first = 4
solution = Solution()
print(solution.decode(encoded, first))
