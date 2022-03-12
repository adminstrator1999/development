class Solution:
    def kids_with_candies(self, candies: list, extra_candies: int) -> list:
        maximum = max(candies)
        for i in range(len(candies)):
            if candies[i] + extra_candies >= maximum:
                candies[i] = True
            else:
                candies[i] = False
        return candies


candies = [2, 3, 5, 1, 3]
extraCandies = 3
solution = Solution()
print(solution.kids_with_candies(candies, extraCandies))
