class OrderedStream:
    """Optimal"""
    def __init__(self, n: int):
        self.n = n
        self.stream = [""]*self.n
        self.pointer = 0

    def insert(self, id_key: int, value: str) -> list:
        self.stream[id_key - 1] = value
        array = []
        while self.pointer < self.n and self.stream[self.pointer]:
            array.append(self.stream[self.pointer])
            self.pointer += 1
        return array


# my version
# class OrderedStream:
#     def __init__(self, n: int):
#         self.n = n
#         self.target = [None for _ in range(self.n)]
#         self.pointer = 1
#
#     def insert(self, id_key: int, value: str) -> list:
#         self.target[id_key - 1] = value
#         if self.pointer == id_key:
#             id_key -= 1
#             end_point = id_key + 1
#             for i in range(id_key + 1, self.n):
#                 if self.target[i] is not None:
#                     end_point += 1
#                 else:
#                     self.pointer = end_point + 1
#                     break
#             return self.target[id_key:end_point]
#         return []


# Your OrderedStream object will be instantiated and called as such:
data = [[3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
obj = OrderedStream(5)
for id_key, value in data:
    print(obj.insert(id_key, value))
