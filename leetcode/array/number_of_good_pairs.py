class Solution:
    def _num_identical_pairs(self, nums: list) -> dict:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = 1
            else:
                hashtable[nums[i]] += 1
        return hashtable

    def num_identical_pairs(self, nums: list) -> int:
        hashtable = self._num_identical_pairs(nums)
        counter = 0
        for key, value in hashtable.items():
            if value > 1:
                counter += self._calculate_combinations(value)
        return counter

    def _calculate_combinations(self, count: int) -> int:
        output = 0
        if count > 1:
            count -= 1
            output = count + self._calculate_combinations(count)
        return output

    def num_identical_pairs_brute_force(self, nums: list) -> int:
        pairs = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and (i, j) not in nums and i != j:
                    pairs.append((i, j))
                    pairs.append((j, i))
        return pairs


nums = [1, 2, 3, 1, 1, 3]

# Output: 4
solution = Solution()
result = solution.num_identical_pairs_brute_force(nums)
print(solution.num_identical_pairs(nums))
# print(result)
# print(solution._calculate_combinations(5))
