# nums = list(map(int, input().split()))
# k = int(input())

nums = [1, 2, 3, 4, 5, 6, 7]
k = 6
print(id(nums))

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy_nums = nums.copy()
        length = len(nums)
        k = k % length
        for index in range(length):
            nums[index + k if index + k < length else (index + k) % length] = copy_nums[index]

    def rotate_2(self, nums: list, k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_1(self, nums: list, k: int) -> None:
        for _ in range(k % len(nums)):
            first = nums[-1]
            for index in range(len(nums) - 1, -1, -1):
                if index != 0:
                    nums[index] = nums[index - 1]
                else:
                    nums[index] = first
            print(nums)


solution = Solution()
solution.rotate_2(nums, k)
print(id(nums))
