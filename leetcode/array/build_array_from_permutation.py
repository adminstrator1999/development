class Solution:
    def build_array(self, nums: list) -> list:
        for i in range(len(nums)):
            nums[i] += len(nums) * (nums[nums[i]] % len(nums))

        # for i in range(len(nums)):
        #     nums[i] //= len(nums)

        return nums

    def build_array_extra_memory(self, nums: list) -> list:
        return [nums[index] for index in nums]


nums = [0, 2, 1, 5, 3, 4]
# Output: [0,1,2,4,5,3]
solution = Solution()
result = solution.build_array(nums)
print(result)
