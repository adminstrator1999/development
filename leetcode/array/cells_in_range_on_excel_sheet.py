import string


class Solution:
    def cells_in_range(self, s: str) -> list:
        start_letter = ord(s[0])
        end_letter = ord(s[3])
        start_int = int(s[1])
        end_int = int(s[4])
        result = []
        for i in range(start_letter, end_letter+1):
            for j in range(start_int, end_int+1):
                result.append(f"{chr(i)}{j}")
        return result

    def cells_in_range_first_thoughts(self, s: str) -> list:
        alphabet = string.ascii_uppercase
        split = s.split(":")
        start_letter = split[0][0]
        end_letter = split[1][0]
        start_int = int(split[0][1])
        end_int = int(split[1][1])
        start_letter_index = alphabet.index(start_letter)
        end_letter_index = alphabet.index(end_letter)
        result = []
        for i in range(start_letter_index, end_letter_index+1):
            for j in range(start_int, end_int+1):
                result.append(f"{alphabet[i]}{j}")
        return result


s = "K1:L2"
solution = Solution()
print(solution.cells_in_range(s))
