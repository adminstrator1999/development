class Solution:
    def final_value_after_operations(self, operations: list) -> int:
        x = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                x -= 1
            elif operation == "++X" or operation == "X++":
                x += 1
        return x


operations = ["++X", "++X", "X++"]
# Output: 3
solution = Solution()
result = solution.final_value_after_operations(operations)
print(result)
