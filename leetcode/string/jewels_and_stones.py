class Solution:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        counter = 0
        for stone in stones:
            if stone in jewel_set:
                counter += 1
        return counter

    def num_jewels_in_stones_easy_brute_force(self, jewels: str, stones: str) -> int:
        counter = 0
        for stone in stones:
            if stone in jewels:
                counter += 1
        return counter


jewels = "aA"
stones = "aAAbbbb"
solution = Solution()
print(solution.num_jewels_in_stones(jewels, stones))
