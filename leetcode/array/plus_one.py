class Solution:

    def plus_one(self, digits: list) -> list:
        number = 1
        for index in range(len(digits) - 1, -1, -1):
            if number:
                add = digits[index] + number
                if add >= 10:
                    digits[index] = add % 10
                    number = 1
                else:
                    digits[index] = add
                    return digits
        if number:
            digits.insert(0, 1)
        return digits

    def plus_one_2(self, digits: list) -> list:
        remain = 0
        number = 1
        for index in range(len(digits) - 1, -1, -1):
            if number or remain:
                add = digits[index] + number + remain
                number = 0
                if add >= 10:
                    digits[index] = add % 10
                    remain = 1
                else:
                    digits[index] = add
                    remain = 0
                    break
        if remain:
            digits[:] = [1] + digits
        return digits

    def plus_one_1(self, digits: list) -> list:
        number = "".join(list(map(str, digits)))
        number = int(number) + 1
        return [int(i) for i in str(number)]


# digits = list(map(int, input().split()))
digits = [4, 3, 2, 1]

solution = Solution()
print(solution.plus_one(digits))
