from collections import defaultdict
# numbers = list(map(int, input().split()))
nums = [4, 1, 2, 1, 2, 4, 6, 6, 7]


class Solution:

    def single_number(self, nums: list) -> int:
        table = dict()
        for num in nums:
            if table.__contains__(num):
                table[num] += 1
            else:
                table[num] = 1
        for key in table:
            if table[key] == 1:
                return key

    def single_number_3(self, nums: list) -> int:
        hashtable = defaultdict(int)

        for num in nums:
            hashtable[num] += 1

        for key in hashtable:
            if hashtable[key] == 1:
                return key

    def single_number_2 (self, nums: list) -> int:
        unique_nums = set(nums)
        table = {}
        for num in unique_nums:
            table[num] = 0
        for num in nums:
            table[num] += 1
        for key in unique_nums:
            if table[key] == 1:
                return key

    def single_number_1(self, nums: list) -> int:
        # bad solution
        for num in nums:
            count = 0
            for n in nums:
                if num == n:
                    count += 1
            if count == 2:
                continue
            else:
                return num

    def single_number_4(self, num: list) -> int:
        # bitwise
        """ Two the numbers become zero when ^ operator is used. Ex: 5^5 = 0"""
        res = 0
        for num in nums:
            res ^= num
        return res


solution = Solution()
print(solution.single_number_3(nums))
