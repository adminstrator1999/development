# x = input()
# y = input()
import itertools


class Solution:
    def _add_helper(self, addition, collection):
        if addition >= 10:
            collection.append(str(addition)[-1])
            return 1
        else:
            collection.append(str(addition))
            return 0

    def add(self, x, y):
        x, y = str(x), str(y)
        bigger = x if len(x) >= len(y) else y
        lesser = x if len(x) < len(y) else y
        remain = 0
        collection = []
        for index in range(1, len(lesser) + 1):
            addition = int(bigger[-index]) + int(lesser[-index]) + remain
            remain = self._add_helper(addition, collection)
        for new_index in range(len(lesser) + 1, len(bigger) + 1):
            addition = int(bigger[-new_index]) + remain
            remain = self._add_helper(addition, collection)
        if remain == 1:
            collection.append("1")
        collection.reverse()
        return "".join(collection)

    def add_difficult_way(self, x, y):
        x, y = str(x), str(y)
        bigger = x if len(x) > len(y) else y
        lesser = x if len(x) < len(y) else y
        remain = 0
        collection = []
        for index in range(-1, -len(bigger) - 1, -1):
            if index < -len(lesser):
                if remain == 1:
                    add = int(bigger[index]) + 1
                    if add >= 10:
                        remain = 1
                        collection.append(str(add)[-1])
                    else:
                        remain = 0
                        collection.append(str(add))
                else:
                    collection.append(bigger[:index + 1])
                    break
            elif index >= -len(lesser):
                add = int(bigger[index]) + int(lesser[index]) + remain
                remain = 0
                if add >= 10:
                    collection.append(str(add)[-1])
                    remain += 1
                else:
                    collection.append(str(add))
        if remain:
            collection.append('1')
        collection.reverse()
        return "".join(collection)


x = 79999
y = 82388

solution = Solution()
print(solution.add(x, y))
