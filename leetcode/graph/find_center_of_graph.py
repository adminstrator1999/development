class Solution:
    def find_center(self, edges: list) -> int:
        node_a = edges[0][0]
        node_b = edges[0][1]
        if edges[1][0] == node_a or edges[1][1] == node_a:
            return node_a
        elif edges[1][0] == node_b or edges[1][1] == node_b:
            return node_b

    def find_center_brute_force(self, edges: list) -> int:
        hashtable = {}
        for edge in edges:
            if edge[0] not in hashtable:
                hashtable[edge[0]] = 1
            else:
                hashtable[edge[0]] += 1
            if edge[1] not in hashtable:
                hashtable[edge[1]] = 1
            else:
                hashtable[edge[1]] += 1
        for i in hashtable:
            if hashtable[i] > 1:
                return i


edges = [[1, 3], [2, 3]]
solution = Solution()
print(solution.find_center(edges))
