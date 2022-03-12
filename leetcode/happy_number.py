class Solution:
    def is_happy(self, n: int) -> bool:
        try:
            output = 0
            for num in str(n):
                output += int(num) ** 2
            if output == 1:
                return True
            return self.is_happy(output)
        except RecursionError:
            return False


n = 23
solution = Solution()
print(solution.is_happy(n))
