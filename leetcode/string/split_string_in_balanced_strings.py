class Solution:
    def balanced_string_split(self, s: str) -> int:
        counter = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "R":
                counter += 1
            elif s[i] == "L":
                counter -= 1
            if counter == 0:
                result += 1
        return result


s = "RRRLRLLL"
solution = Solution()
print(solution.balanced_string_split(s))
