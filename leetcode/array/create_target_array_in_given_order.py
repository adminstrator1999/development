class Solution:
    def create_target_array(self, nums: list, index: list) -> list:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

    def create_target_array_brute_force(self, nums: list, index: list) -> list:
        target = []
        for i, num in enumerate(nums):
            for j in range(i, len(target), 1):
                target.insert(j+1, target[j])
            target.insert(index[i], num)
        return target


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
solution = Solution()
print(solution.create_target_array(nums, index))
