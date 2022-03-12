# nums = list(map(int, input().split()))


class Solution:
    def remove_duplicates(self, nums: list) -> int:
        unique_pointer = 0
        for index in range(1, len(nums)):
            if nums[unique_pointer] == nums[index]:
                nums[index] = '_'
            elif nums[unique_pointer] != nums[index]:
                unique_pointer += 1
                nums[unique_pointer] = nums[index]
        return unique_pointer + 1

    def remove_duplicates_1(self, nums: list) -> int:
        for index in range(len(nums) - 1, 0, -1):
            if nums[index] == nums[index - 1]:
                nums[index] = '_'
                nums[:] = nums[:index] + nums[index + 1:]
        return len(nums)

    def remove_duplicates_brute_force(self, nums: list) -> int:
        unique_nums = list()
        for num in nums:
            if num not in unique_nums:
                unique_nums.append(num)
        nums[:] = unique_nums
        return len(unique_nums)


nums = [1, 2]
solution = Solution()
print(solution.remove_duplicates(nums), nums)
