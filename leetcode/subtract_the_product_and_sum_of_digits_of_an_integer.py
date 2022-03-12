class Solution:
    def subtract_product_and_sum(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n //= 10
        product = digits[0]
        addition = digits[0]
        for digit in digits[1:]:
            product *= digit
            addition += digit
        return product - addition

    def subtract_product_and_sum_easy(self, n: int) -> int:
        n = str(n)
        product = int(n[0])
        addition = int(n[0])
        for digit in n[1:]:
            product *= int(digit)
            addition += int(digit)
        return product - addition


n = 234
solution = Solution()
print(solution.subtract_product_and_sum(n))
print(solution.subtract_product_and_sum_easy(n))
