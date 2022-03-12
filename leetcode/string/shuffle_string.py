class Solution:
    def restore_string(self, s: str, indices: list) -> str:
        new_str = [j for j in s]
        for i in range(len(indices)):
            new_str[indices[i]] = s[i]
        return "".join(new_str)


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

solution = Solution()
print(solution.restore_string(s, indices))
