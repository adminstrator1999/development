class Solution:

    def _sum(self, account: list) -> int:
        output = 0
        for i in account:
            output += i
        return output

    def _max(self, accounts: list) -> int or None:
        if not accounts:
            return None
        maximum = accounts[0]
        for total_sum in accounts:
            if total_sum > maximum:
                maximum = total_sum
        return maximum

    def maximum_wealth(self, accounts: list) -> int:
        return self._max([self._sum(data) for data in accounts])

    def maximum_wealth_easy(self, accounts: list) -> int:
        return max(sum(data) for data in accounts)


accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
solution = Solution()
result = solution.maximum_wealth(accounts)
print(result)
