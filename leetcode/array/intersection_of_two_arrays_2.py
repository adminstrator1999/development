class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        count = {}
        res = []
        for n in nums1:
            count[n] = count.get(n, 0) + 1
        for n in nums2:
            if n in count.keys():
                res.append(n)
                count[n] = count[n] - 1
                if count[n] == 0: count.pop(n)

        return res

    def intersect_brute_force(self, nums1: list, nums2: list) -> list:
        hashtable_1 = dict()
        hashtable_2 = dict()
        for num1 in nums1:
            if num1 in hashtable_1:
                hashtable_1[num1].append(num1)
            else:
                hashtable_1[num1] = [num1]
        for num2 in nums2:
            if num2 in hashtable_2:
                hashtable_2[num2].append(num2)
            else:
                hashtable_2[num2] = [num2]
        smaller = hashtable_1 if len(hashtable_1) <= len(hashtable_2) else hashtable_2
        bigger = hashtable_1 if len(hashtable_1) > len(hashtable_2) else hashtable_2
        output = []
        for key in smaller:
            if key in bigger and len(smaller[key]) >= len(bigger[key]):
                output += bigger[key]
            elif key in bigger and len(smaller[key]) < len(bigger[key]):
                output += smaller[key]
        return output


# nums1 = list(map(int, input().split()))
# nums2 = list(map(int, input().split()))
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
solution = Solution()
print(solution.intersect_brute_force(nums1, nums2))
