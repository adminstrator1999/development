class Solution:
    def most_words_found(self, sentences: list) -> int:
        return max(len(sentence.split(' ')) for sentence in sentences)

    def most_words_found_expected(self, sentences: list) -> int:
        return self._max([self._count_words(sentence) for sentence in sentences])

    def _count_words(self, sentence: list) -> int:
        count = 0
        for letter in sentence:
            if letter == " ":
                count += 1
        if count:
            return count + 1
        return count

    def _max(self, numbers: list) -> int or None:
        if not numbers:
            return None
        maximum = numbers[0]
        for number in numbers:
            if number > maximum:
                maximum = number
        return maximum


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6

solution = Solution()
result = solution.most_words_found(sentences)
print(result)
