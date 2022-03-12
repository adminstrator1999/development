class Solution:
    def number_of_steps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps


num = 14
solution = Solution()
print(solution.number_of_steps(num))
