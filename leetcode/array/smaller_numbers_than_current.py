class Solution:
    def smaller_numbers_than_current(self, nums: list) -> list:
        pass

    def smaller_numbers_than_current_brute_force(self, nums: list) -> list:
        new_list = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            new_list.append(counter)
        return new_list


nums = [8, 1, 2, 2, 3]
# Output: [4,0,1,1,3]
solution = Solution()
print(solution.smaller_numbers_than_current_brute_force(nums))
