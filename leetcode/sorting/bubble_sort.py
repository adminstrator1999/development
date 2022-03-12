"""In bubble sort we take biggest to the latest"""


def bubble_sort(nums: list) -> None:
    for num in range(len(nums) - 1, 0, -1):
        for i in range(num):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp


numbers = [1, 9, 3, 4, 2, 6]
bubble_sort(numbers)
print(numbers)
