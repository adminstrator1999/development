class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        shuffled_list = []
        for i in range(n):
            shuffled_list.append(nums[i])
            shuffled_list.append(nums[n+i])
        return shuffled_list


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
# Output: [1,4,2,3,3,2,4,1]

solution = Solution()
result = solution.shuffle(nums, n)
print(result)
