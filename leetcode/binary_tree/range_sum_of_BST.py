# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def range_sum_BST(self, root, low: int, high: int) -> int:
        range_sum = 0
        if root:
            if low <= root.value <= high:
                range_sum += root.value
            range_sum += self.range_sum_BST(root=root.left, low=low, high=high)
            range_sum += self.range_sum_BST(root=root.right, low=low, high=high)
        return range_sum


root = [10, 5, 15, 3, 7, None, 18]
low = 7
high = 15
solution = Solution()
print(solution.range_sum_BST(root, low, high))
