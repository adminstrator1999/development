# nums = list(map(int, input().split()))
nums = [1, 0, 0, 0, 0, 3, 0, 5]


class Solution:
    def move_zeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        iterator = 0
        zero_pointer = 0
        while iterator < len(nums):
            if nums[zero_pointer] != 0:
                zero_pointer += 1
            if nums[iterator] != 0 and iterator > zero_pointer:
                nums[zero_pointer] = nums[iterator]
                nums[iterator] = 0
            iterator += 1

    def move_zeroes_2(self, nums: list) -> None:
        for index in range(len(nums)):
            if nums[index] == 0:
                for i in range(index, len(nums)):
                    if i + 1 < len(nums):
                        nums[i] = nums[i + 1]
                    else:
                        nums[i] = 0

    def move_zeroes_1(self, nums: list) -> list:
        # bad solution
        new_array = []
        for num in nums:
            if num != 0:
                new_array.append(num)
        difference = len(nums) - len(new_array)
        for _ in range(difference):
            new_array.append(0)
        return new_array


solution = Solution()
solution.move_zeroes(nums)
print(nums)
# print(solution.move_zeroes_1(nums))
