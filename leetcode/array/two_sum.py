from collections import defaultdict


class Solution:
    def two_sum(self, nums: list, target: int) -> list:
        hashtable = defaultdict(int)
        for index, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[num], index]
            else:
                hashtable[num] = index

    def two_sum_1(self, nums: list, target: int) -> list:
        hashtable = dict()
        for index, num in enumerate(nums):
            if hashtable.__contains__(num):
                hashtable[num].append(index)
            else:
                hashtable[num] = [index]
        for key in hashtable:
            if len(hashtable[key]) == 1 and hashtable.__contains__(target-key) and key != target - key:
                return hashtable[key] + hashtable[target-key]
            elif len(hashtable[key]) > 1 and key * 2 == target:
                return hashtable[key]


# nums = list(map(int, input().split()))
# target = int(input())
nums = [2,7,11,15]
target = 9

solution = Solution()
print(solution.two_sum(nums, target))
