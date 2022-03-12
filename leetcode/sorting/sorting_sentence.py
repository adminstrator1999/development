class Solution:
    def sort_sentence_brute_force(self, s: str) -> str:
        split = s.split(" ")
        result = [None for _ in split]
        for i in split:
            result[int(i[-1])-1] = i[:-1]
        return " ".join(result)

s = "lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
solution = Solution()
print(solution.sort_sentence_brute_force(s))
