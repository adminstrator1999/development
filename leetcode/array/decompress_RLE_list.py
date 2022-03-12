class Solution:
    def decompress_RLE_list(self, nums: list) -> list:
        decompressed_array = []
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                decompressed_array.append(nums[i])
        return decompressed_array

nums = [1, 1, 2, 3]
# nums = [1, 2, 3, 4]
solution = Solution()
print(solution.decompress_RLE_list(nums))
