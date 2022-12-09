# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))

        return validate(root)


tree_1 = TreeNode()
tree_1.val = 1

tree_3 = TreeNode()
tree_3.val = 3

tree_2 = TreeNode()
tree_2.val = 2
tree_2.left = tree_1
tree_2.right = tree_3

solve = Solution()
print(solve.isValidBST(root=tree_2))


# tree_1 = TreeNode()
# tree_1.val = 1

# tree_3 = TreeNode()
# tree_3.val = 3

# tree_6 = TreeNode()
# tree_6.val = 6

# tree_4 = TreeNode()
# tree_4.val = 4
# tree_4.left = tree_3
# tree_4.right = tree_6

# tree_5 = TreeNode()
# tree_5.val = 5
# tree_5.left = tree_1
# tree_5.right = tree_4


# solve = Solution()
# print(solve.isValidBST(root=tree_5))


# tree_1 = TreeNode()
# tree_1.val = 1

# tree_0 = TreeNode()
# tree_0.val = 0
# tree_0.rigth = tree_1


# solve = Solution()
# print(solve.isValidBST(root=tree_0))
