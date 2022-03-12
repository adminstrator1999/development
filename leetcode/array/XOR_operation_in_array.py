class Solution:
    def xor_operation(self, n: int, start: int) -> int:
        output = start
        for i in range(1, n):
            output ^= start + 2 * i
        return output

    def xor_operation_easy(self, n: int, start: int) -> int:
        array = []
        for i in range(n):
            array.append(start + 2 * i)
        output = array[0]
        for j in array[1:]:
            output ^= j
        return output


n = 5
start = 0
solution = Solution()
print(solution.xor_operation(n, start))
