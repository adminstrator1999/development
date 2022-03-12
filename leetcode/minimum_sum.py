class Solution:
    def minimum_sum(self, num: int) -> int:
        pass

    def three_number_combinations(self, addition: int, num: str) -> list:
        output = [addition + int(num), addition + int(num[2] + num[1] + num[0]),
                  addition + int(num[1] + num[2] + num[0]), addition + int(num[1] + num[2] + num[0])]
        return output

    def minimum_sum_brute_force(self, num: int) -> int:
        num_str = str(num)
        possible_pairs = [int(num_str[:2]) + int(num_str[3:]), int(num_str[1] + num_str[0]) + int(num_str[3:]),
                          int(num_str[1] + num_str[0]) + int(num_str[3] + num_str[2]),
                          int(num_str[3] + num_str[2]) + int(num_str[:2])]
        possible_pairs += self.three_number_combinations(int(num_str[0]), num_str[1:])
        possible_pairs += self.three_number_combinations(int(num_str[3]), num_str[:3])
        return min(possible_pairs)


num = 2932
solution = Solution()
print(solution.minimum_sum_brute_force(num))
