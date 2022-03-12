# nums = list(map(int, input().split()))
nums = [1, 2, 3, 1]


class Solution:

    def contains_duplicate(self, nums: list) -> bool:
        # easy solution
        unique_nums = set(nums)
        return len(unique_nums) != len(nums)

    def contains_duplicate_1(self, nums: list) -> bool:
        # bad solution
        unique_nums = []
        for num in nums:
            if num not in unique_nums:
                unique_nums.append(num)
        print(unique_nums)
        return len(unique_nums) != len(nums)


solution = Solution()
print(solution.contains_duplicate(nums))
