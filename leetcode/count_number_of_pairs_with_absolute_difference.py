class Solution:
    def count_K_difference(self, nums: list, k: int) -> int:
        hashtable = {}
        counter = 0
        for i in nums:
            for j in nums:
                if j - i == k:
                    counter += 1
        return counter

    def count_K_difference_brute_force(self, nums: list, k: int) -> int:
        counter = 0
        for i in nums:
            for j in nums:
                if j - i == k:
                    counter += 1
        return counter


nums = [3, 2, 1, 5, 4]
k = 2
solution = Solution()
print(solution.count_K_difference(nums, k))
